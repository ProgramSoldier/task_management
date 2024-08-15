from django.db import models
from django.contrib.auth.models import User


class ProjectModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} {self.title}'

    objects = models.Manager()

class TaskModel(models.Model):
    title = models.CharField(max_length=180)
    dat = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    comment = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    is_ready = models.BooleanField(default=False)

    def __str__(self):
        return f'Название: {self.title} Проект: {self.project.title}'

    objects = models.Manager()

class Project_UserModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        res = f'Пользователь: {self.user.username} Проект: {self.project.title}'
        if self.is_author:
            res += ' АВТОР'
        return res

    objects = models.Manager()


class Temporary_links(models.Model):
    pass
