"""
Autogenerate viewsets file
"""
from rest_framework import viewsets
from .models import Genre, Movie 	# pylint: disable=relative-beyond-top-level
from .serializers import GenreSerializer, MovieSerializer # pylint: disable=relative-beyond-top-level

class GenreViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    Genre ViewSet
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    Movie ViewSet
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
