# -*- encoding: utf-8 -*-
"""
Autogenerate urls file
"""
from rest_framework.routers import DefaultRouter
from .viewsets import GenreViewSet, SerieViewSet # pylint: disable=relative-beyond-top-level

router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'series', SerieViewSet)

urlpatterns = router.urls
