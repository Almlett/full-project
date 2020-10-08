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


class Movie(models.Model):
    """
    Movie Model
    """
    name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name}"
        