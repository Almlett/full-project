"""
Autogenerate admin file
"""
from django.contrib import admin
from .models import Genre, Serie	# pylint: disable=relative-beyond-top-level

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
@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    """
    Serie Admin
    """

    fields = (
        "name","provider","genre","year",
    )
    list_display = (
        "name","provider","genre","year",
    )
