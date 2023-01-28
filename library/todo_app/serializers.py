from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from authors.models import Author
from todo_app.models import Project, Todo


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ProjectModelSerializer(HyperlinkedModelSerializer):
    # author = AuthorModelSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class ProjectModelSerializerBase(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
