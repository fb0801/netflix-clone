from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

AGE_CHOICES = (
    ('All','All'),
    ('Kids','Kids')
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('profile', null=True, blank=True)


class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)
