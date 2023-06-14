from django.contrib import admin
from .models import *

# Register your models here.
class CompanyAdmin (admin.ModelAdmin):
    list_display = ('id_company', 'name_company', 'rut_company',)

admin.site.register(Company,CompanyAdmin)