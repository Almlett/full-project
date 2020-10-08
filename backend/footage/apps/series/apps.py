"""
Autogenerate apps file
"""
from django.apps import AppConfig

class GenreConfig(AppConfig):
    """
    Genre App
    """

    name = 'genres'

class SerieConfig(AppConfig):
    """
    Serie App
    """

    name = 'series'
