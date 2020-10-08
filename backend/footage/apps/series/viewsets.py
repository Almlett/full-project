"""
Autogenerate viewsets file
"""
from rest_framework import viewsets
from .models import Genre, Serie 	# pylint: disable=relative-beyond-top-level
from .serializers import GenreSerializer, SerieSerializer # pylint: disable=relative-beyond-top-level

class GenreViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    Genre ViewSet
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class SerieViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    Serie ViewSet
    """

    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
