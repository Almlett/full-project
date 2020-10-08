# -*- encoding: utf-8 -*-
"""
Autogenerate urls file
"""
from rest_framework.routers import DefaultRouter
from .viewsets import GenreViewSet, MovieViewSet # pylint: disable=relative-beyond-top-level

router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = router.urls
