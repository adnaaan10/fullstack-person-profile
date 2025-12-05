from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet,register

router = DefaultRouter()
router.register(r"persons",PersonViewSet,basename="person")

urlpatterns = [path("register/",register),
               path("",include(router.urls)),
               ]