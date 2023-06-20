from django.contrib import admin
from .models import Generoworker

class GeneroworkerAdmin (admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Generoworker,GeneroworkerAdmin)