# app/movies/urls.py

from django.urls import path
from .views import MovieList, MovieDetail

urlpatterns = [
    path("movies/", MovieList.as_view()),
    path("movies/<int:pk>/", MovieDetail.as_view()),
]