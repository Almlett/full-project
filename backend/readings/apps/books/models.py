"""
MODEL
"""
from django.db import models


class Genre(models.Model):
    """
    Genre Model
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    """
    Serie Model
    """
    name = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    year = models.DateField()
    pages = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
        