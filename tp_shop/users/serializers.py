from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'favorites')


class UserLogin(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class UserSignUp(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class UserFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["favorites"]


class UserUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]