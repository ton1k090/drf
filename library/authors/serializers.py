from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers
from .models import Author


class AuthorModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
