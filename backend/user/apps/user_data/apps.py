"""
Autogenerate apps file
"""
from django.apps import AppConfig

class ProfileConfig(AppConfig):
    """
    Profile App
    """

    name = 'profiles'

class UserMovieConfig(AppConfig):
    """
    UserMovie App
    """

    name = 'usermovies'

class UserBookConfig(AppConfig):
    """
    UserBook App
    """

    name = 'userbooks'

class UserSerieConfig(AppConfig):
    """
    UserSerie App
    """

    name = 'userseries'
