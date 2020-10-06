"""
Autogenerate viewsets file
"""
from rest_framework import viewsets
from .models import Genre, Book 	# pylint: disable=relative-beyond-top-level
from .serializers import GenreSerializer, BookSerializer # pylint: disable=relative-beyond-top-level

class GenreViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    Genre ViewSet
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    Book ViewSet
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
