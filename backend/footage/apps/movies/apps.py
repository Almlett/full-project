"""
Autogenerate apps file
"""
from django.apps import AppConfig

class GenreConfig(AppConfig):
    """
    Genre App
    """

    name = 'genres'

class MovieConfig(AppConfig):
    """
    Movie App
    """

    name = 'movies'
