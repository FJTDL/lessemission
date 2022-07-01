from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# User object is created when the user form is submitted with valid details
class CarbonScore(models.Model):
    value = models.IntegerField()
    parent = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class User(models.Model):
    name = models.CharField(max_length=20)
    score = models.ForeignKey(CarbonScore, on_delete=models.CASCADE, null=True, blank=True)