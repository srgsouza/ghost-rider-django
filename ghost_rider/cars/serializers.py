from rest_framework import serializers
from .models import Car, Comment
from django.contrib.auth.models import User



####
from rest_framework.validators import UniqueValidator

#####

class UserSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, default=[], allow_null=True, queryset=Car.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, default=[], allow_null=True, queryset=Comment.objects.all())
    email = serializers.EmailField(
            required=False,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=1)


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'cars', 'comments' )


class CarSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # images = serializers.ImageField(allow_null=True)
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year', 'description', 'img_url', 'owner')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'car', 'owner' )

