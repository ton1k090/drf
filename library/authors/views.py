from django.shortcuts import render
from rest_framework import mixins, viewsets, permissions

from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer, AuthorModelSerializer2


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return AuthorModelSerializer2

        return AuthorModelSerializer
