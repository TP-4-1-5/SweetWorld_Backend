from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductAddFavoriteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ["username", "id"]


class ProductDeleteFavoriteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ["username", "id"]


class ProductViewSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ["username"]