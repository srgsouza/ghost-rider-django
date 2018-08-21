from rest_framework import serializers
from .models import Car, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'cars', 'comments')


class CarSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    images = serializers.ImageField(allow_null=True)
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year', 'description', 'img_url', 'images', 'owner')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'car', 'owner' )

