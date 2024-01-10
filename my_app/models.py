from django.db import models


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=30, unique=True)
    author = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=500)
    method = models.CharField(max_length=500)

    def __str__(self):
        return self.author + '' + self.title
