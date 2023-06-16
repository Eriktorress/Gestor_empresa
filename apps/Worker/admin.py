from django.contrib import admin
from .models import *

# Register your models here.
class WorkerAdmin (admin.ModelAdmin):
    list_display = ('id_worker', 'name', 'rut',)

admin.site.register(Worker,WorkerAdmin)