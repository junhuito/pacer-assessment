from django.db import models

# Create your models here.

class Score(models.Model):
    name = models.TextField()
    score = models.IntegerField()
    field2 = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

