from django.contrib import admin
from .models import Tipodocumento

class TipodocumentoAdmin (admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Tipodocumento,TipodocumentoAdmin)