from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    completed = models.BooleanField(default=False)
    owner = models.TextField(blank=True)
