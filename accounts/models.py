
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    nickname=models.CharField(max_length=15)

    def __str__(self):
        return self.username
