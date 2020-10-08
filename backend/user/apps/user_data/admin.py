"""
Autogenerate admin file
"""
from django.contrib import admin
from .models import Profile, UserMovie, UserBook, UserSerie	# pylint: disable=relative-beyond-top-level

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Profile Admin
    """

    fields = (
        "auth_user","read_time","viewing_time",
    )
    list_display = (
        "auth_user","read_time","viewing_time",
    )
@admin.register(UserMovie)
class UserMovieAdmin(admin.ModelAdmin):
    """
    UserMovie Admin
    """

    fields = (
        "user","movie","movie_name",
    )
    list_display = (
        "user","movie","movie_name",
    )
@admin.register(UserBook)
class UserBookAdmin(admin.ModelAdmin):
    """
    UserBook Admin
    """

    fields = (
        "user","book","book_name",
    )
    list_display = (
        "user","book","book_name",
    )
@admin.register(UserSerie)
class UserSerieAdmin(admin.ModelAdmin):
    """
    UserSerie Admin
    """

    fields = (
        "user","serie","serie_name",
    )
    list_display = (
        "user","serie","serie_name",
    )
