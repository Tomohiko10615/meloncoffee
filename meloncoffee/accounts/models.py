
# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


#from django.contrib.auth.models import User
#User._meta.get_field('email')._unique = True

class CustomUser(AbstractUser):
    class Meta:
        unique_together = ('email',)
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    phone = models.PositiveIntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    
    #is_active = models.BooleanField(default=False)


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