"""Views for the user API"""
from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create new users in the system"""
    serializer_class = UserSerializer