"""
Autogenerate serializers file
"""
from rest_framework import serializers
from .models import Genre, Serie	# pylint: disable=relative-beyond-top-level

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

class SerieSerializer(serializers.ModelSerializer):
    """
    Serie Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model Serie
        """

        model = Serie
        fields = '__all__'
