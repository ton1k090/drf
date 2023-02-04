import graphene
from graphene_django import DjangoObjectType
from todo_app.models import Todo, Project
from authors.models import Author


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)
    all_authors = graphene.List(AuthorType)

    def resolve_all_todos(root, info):
        return Todo.objects.all()

    def resolve_all_authors(root, info):
        return Author.objects.all()


schema = graphene.Schema(query=Query)
