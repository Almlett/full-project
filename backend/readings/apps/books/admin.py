"""
Autogenerate admin file
"""
from django.contrib import admin
from .models import Genre, Book	# pylint: disable=relative-beyond-top-level

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
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Book Admin
    """

    fields = (
        "name","provider","genre","year","pages",
    )
    list_display = (
        "name","provider","genre","year","pages",
    )
