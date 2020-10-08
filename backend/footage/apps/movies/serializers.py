"""
Autogenerate serializers file
"""
from rest_framework import serializers
from .models import Genre, Movie	# pylint: disable=relative-beyond-top-level

class GenreSerializer(serializers.ModelSerializer):
    """
    Genre Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model Genre
        """

        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    """
    Movie Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model Movie
        """

        model = Movie
        fields = '__all__'
