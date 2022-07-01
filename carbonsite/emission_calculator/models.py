from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# User object is created when the user form is submitted with valid details
class CarbonScore(models.Model):
    value = models.IntegerField()
    # parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

class CustomUser(AbstractUser):
    name = models.CharField(max_length=20)
    score = models.ForeignKey(CarbonScore, on_delete=models.CASCADE, null=True, blank=True)