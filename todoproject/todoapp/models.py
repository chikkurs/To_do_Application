from django.db import models

# Create your models here.
class Todo(models.Model):
    task=models.CharField(max_length=100)
    priority=models.CharField(max_length=100)
    date=models.DateField()

