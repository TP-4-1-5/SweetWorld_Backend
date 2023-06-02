from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentAddSerializer(serializers.ModelSerializer):
    product = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    product_id = serializers.IntegerField()
    class Meta:
        model = Comment
        fields = ["product", "username", "description", "product_id"]


class CommentDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    product_id = serializers.CharField(max_length=100)
    class Meta:
        model = Comment
        fields = ["id", "product_id"]