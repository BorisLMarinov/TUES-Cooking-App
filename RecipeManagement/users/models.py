from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    app_label = "users"
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    picture = models.ImageField(default="")
