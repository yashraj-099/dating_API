from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
