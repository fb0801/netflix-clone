from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('profile', null=True, blank=True)



class Profile(models.Model):
    name = models.CharField(max_length=255)
