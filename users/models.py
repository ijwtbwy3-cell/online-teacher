from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    role = models.CharField(max_length = 20, default = 'teacher')
    phone = models.CharField(max_length = 20, blank = True)
    avatar = models.ImageField(upload_to = 'avatars/', blank = True, null = True)
    def __str__(self):
        return self.username
    