"""Serializers for the user API"""
from colorama import Style
from django.contrib.auth import get_user_model
from django.utils.translation import trim_whitespace
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """serializer for the user object"""
    class Meta:
        model = get_user_model()
        fields = ["email", "password", "name"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """create and return a user with an encrypted password"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """serializer for the user auth token"""
    email = serializers.EmailField()
    password = serializers.CharField(
        Style ={'input_style':'password'},
        trim_whitespace=False
    )