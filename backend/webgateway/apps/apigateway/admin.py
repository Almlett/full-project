from django.contrib import admin
from .models import Proyect, Consumer, Api	# pylint: disable=relative-beyond-top-level



@admin.register(Proyect)
class ProyectAdmin(admin.ModelAdmin):
    """
    Consumer Admin
    """

    fields = (
        "name",
        "host",
        "port",
    )
    list_display = (
        "name",
        "host",
        "port",
    )

@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    """
    Consumer Admin
    """

    fields = (
        "user","apikey",
    )
    list_display = (
        "user","apikey",
    )

@admin.register(Api)
class ApiAdmin(admin.ModelAdmin):
    """
    Api Admin
    """

    fields = (
        "name",
        "request_path",
        "origin",
        "plugin",
        "consumers",
    )
    list_display = (
        "name",
        "request_path",
        "origin",
        "plugin",
    )