from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

