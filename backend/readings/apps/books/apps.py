"""
Autogenerate apps file
"""
from django.apps import AppConfig

class GenreConfig(AppConfig):
    """
    Genre App
    """

    name = 'genres'

class BookConfig(AppConfig):
    """
    Book App
    """

    name = 'books'
