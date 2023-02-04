from django.contrib.auth.models import AbstractBaseUser, User
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers
from .models import Author


class AuthorModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class AuthorModelSerializer2(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_login')
