from django.db import models

# Create your models here.
class Book(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=False)
    genre       = models.CharField(max_length=80, blank=False)
    