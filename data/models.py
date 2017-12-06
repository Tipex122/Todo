
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# XLHfrom .managers import PersonManager

from datetime import datetime, timedelta


class Person(User):
    # XLH objects = PersonManager()
    class Meta:
        proxy = True
        ordering = ('first_name', )

    # profile_pic = models.ImageField(upload_to = 'user/',null=True)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Todo(models.Model):
    todo_job = models.CharField(max_length=200)
    todo_job_detail = models.TextField(default='Todo detail')
    user = models.ForeignKey('Person', on_delete=True)
    category = models.ForeignKey('Category', on_delete=False)
    is_finished = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.todo_job

