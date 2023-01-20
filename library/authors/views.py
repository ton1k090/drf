from django.shortcuts import render
from rest_framework import mixins, viewsets

from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
