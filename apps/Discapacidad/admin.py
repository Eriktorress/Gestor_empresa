from django.contrib import admin
from .models import Discapacidad

class DiscapacidadAdmin (admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Discapacidad,DiscapacidadAdmin)