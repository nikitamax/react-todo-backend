from django.db import models

class Snippet(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    completed = models.BooleanField(default=False)
