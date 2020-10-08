from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    auth_user = models.OneToOneField(User, on_delete = models.CASCADE)
    read_time = models.CharField(max_length=255)
    viewing_time = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.auth_user}"

class UserMovie(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    movie = models.CharField(max_length=255)
    movie_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user}"

class UserBook(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    book = models.CharField(max_length=255)
    book_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user}"

class UserSerie(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    serie = models.CharField(max_length=255)
    serie_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user}"