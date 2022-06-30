from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# User object is created when the user form is submitted with valid details
class User(models.Model):
    name = models.CharField(max_length=20)
    score = models.IntegerField()