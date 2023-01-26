import django_filters
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import Project, Todo
from .serializers import TodoModelSerializer, ProjectModelSerializer
from authors.serializers import AuthorModelSerializer
from .filters import ProjectFilter


class ProjectPaginator(LimitOffsetPagination):
    default_limit = 10


class TodoPaginator(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPaginator
    filterset_class = ProjectFilter


class TodoModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoPaginator
    filterset_fields = ['text', 'project', 'user']

    def destroy(self, request, *args, **kwargs):  # переопределяем метод destroy
        instance = self.get_object()
        if instance.is_done is False:
            instance.is_done = True
            instance.save()
            return Response()
        return Response()


