
from django.db import models

# Create your models here.

# Score objects point to a parent User object if the user is logged in - ATTENTION that for some reason this does not yet store the score properly.
class Score(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    score = models.IntegerField()

# User object is created when the user form is submitted with valid details
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # score = models.ForeignKey(Score, on_delete=models.CASCADE)