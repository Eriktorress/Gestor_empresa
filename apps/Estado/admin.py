from django.contrib import admin
from .models import *

class EstadoAdmin (admin.ModelAdmin):
    list_display = ('estado',)

admin.site.register(Estado,EstadoAdmin)