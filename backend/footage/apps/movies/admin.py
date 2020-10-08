"""
Autogenerate admin file
"""
from django.contrib import admin
from .models import Genre, Movie	# pylint: disable=relative-beyond-top-level

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Genre Admin
    """

    fields = (
        "name",
    )
    list_display = (
        "name",
    )
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    Movie Admin
    """

    fields = (
        "name","genre",
    )
    list_display = (
        "name","genre",
    )
