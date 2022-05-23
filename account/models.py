from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone=models.TextField()
    nickname=models.CharField(max_length=15,null=False,blank=False)
    def __str__(self):
        return self.nickname

