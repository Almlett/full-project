# -*- encoding: utf-8 -*-
"""
Autogenerate urls file
"""
from rest_framework.routers import DefaultRouter
from .viewsets import ProfileViewSet, UserMovieViewSet, UserBookViewSet, UserSerieViewSet # pylint: disable=relative-beyond-top-level

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'usermovies', UserMovieViewSet)
router.register(r'userbooks', UserBookViewSet)
router.register(r'userseries', UserSerieViewSet)

urlpatterns = router.urls
