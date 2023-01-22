from django.db import models

from authors.models import Author


class Project(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField(max_length=128, default=None)
    users = models.ManyToManyField(Author, default=None)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Todo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'