"""
Autogenerate serializers file
"""
from rest_framework import serializers
from .models import Genre, Book	# pylint: disable=relative-beyond-top-level

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

class BookSerializer(serializers.ModelSerializer):
    """
    Book Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model Book
        """

        model = Book
        fields = '__all__'
