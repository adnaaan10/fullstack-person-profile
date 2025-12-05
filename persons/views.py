from rest_framework import viewsets,permissions,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Person.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user
        serializer.save(user=self.request.user)

# User Registration API

@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")

    # Validation
    if not username or not password:
        return Response({"error": "Username and password required"},
                        status=status.HTTP_400_BAD_REQUEST)

    # Prevent duplicate usernames
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken"},
                        status=status.HTTP_400_BAD_REQUEST)

    # Create user
    user = User.objects.create_user(username=username, password=password)

    return Response({"message": "User registered successfully"},
                    status=status.HTTP_201_CREATED)