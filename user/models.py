from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUser(AbstractUser):
    objects = UserManager()
