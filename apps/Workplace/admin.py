from django.contrib import admin
from .models import *

# Register your models here.
class WorkplaceAdmin (admin.ModelAdmin):
    list_display = ('id_workplace','id_company', 'name_workplace', 'address',)

admin.site.register(Workplace,WorkplaceAdmin)