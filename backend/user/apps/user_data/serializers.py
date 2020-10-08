"""
Autogenerate serializers file
"""
from rest_framework import serializers
from .models import Profile, UserMovie, UserBook, UserSerie	# pylint: disable=relative-beyond-top-level
import requests, json

class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model Profile
        """

        model = Profile
        fields = '__all__'

class UserMovieSerializer(serializers.ModelSerializer):
    """
    UserMovie Serialzier
    """
    movie_data = serializers.SerializerMethodField()

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model UserMovie
        """

        model = UserMovie
        fields = ('user', 'movie', 'movie_name', 'movie_data')

    @staticmethod
    def get_movie_data(obj):
        result = "not found"
        url = "http://footage:8001/movies/{}/".format(obj.movie)
        resp = requests.get(url)
        if resp.status_code == 200:
            result = json.loads(resp.content)
        return result

class UserBookSerializer(serializers.ModelSerializer):
    """
    UserBook Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model UserBook
        """

        model = UserBook
        fields = '__all__'

class UserSerieSerializer(serializers.ModelSerializer):
    """
    UserSerie Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model UserSerie
        """

        model = UserSerie
        fields = '__all__'
