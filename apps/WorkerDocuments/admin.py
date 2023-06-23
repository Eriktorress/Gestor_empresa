from django.contrib import admin
from .models import WorkerDocuments

class WorkerDocumentsAdmin (admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(WorkerDocuments,WorkerDocumentsAdmin)