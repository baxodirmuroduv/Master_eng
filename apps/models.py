from django.contrib.auth.hashers import make_password
from django.db import models
from django.db.models import Model


# Create your models here.

class Register(Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=255)


class Student(Model):
    fullname = models.CharField(max_length=255)
    fathers_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    passport_id = models.CharField(max_length=9, unique=True)
    passport_jshr = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    group_name = models.ForeignKey('apps.Groups', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-create_at"]

    def __str__(self):
        return self.fullname


class Groups(Model):
    title = models.CharField(max_length=128, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
