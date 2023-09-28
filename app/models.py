from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Note(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, null=True, blank=True)
