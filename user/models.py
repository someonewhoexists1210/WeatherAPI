from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUser(AbstractUser):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    objects = UserManager()
