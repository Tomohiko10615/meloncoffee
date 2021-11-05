
# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    phone = models.PositiveIntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

"""
class CustomUser(models.Model):

    REQUIRED_FIELDS = ('username', 'nombre', 'apellido', 'email', 'password')

    username = models.CharField(unique=True)
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    phone = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
"""