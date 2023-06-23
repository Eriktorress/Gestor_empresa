from django.contrib import admin
from .models import Tipodiscapacidad

class TipodiscapacidadAdmin (admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Tipodiscapacidad,TipodiscapacidadAdmin)