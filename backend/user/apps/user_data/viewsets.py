"""
Autogenerate viewsets file
"""
from rest_framework import viewsets
from .models import Profile, UserMovie, UserBook, UserSerie 	# pylint: disable=relative-beyond-top-level
from .serializers import ProfileSerializer, UserMovieSerializer, UserBookSerializer, UserSerieSerializer # pylint: disable=relative-beyond-top-level

class ProfileViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    Profile ViewSet
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserMovieViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    UserMovie ViewSet
    """

    queryset = UserMovie.objects.all()
    serializer_class = UserMovieSerializer

class UserBookViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    UserBook ViewSet
    """

    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer

class UserSerieViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    UserSerie ViewSet
    """

    queryset = UserSerie.objects.all()
    serializer_class = UserSerieSerializer
