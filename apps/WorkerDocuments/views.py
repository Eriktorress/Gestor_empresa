from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkerDocuments


# Create your views here.
def documents(request):
    listado = WorkerDocuments.objects.all();
    return render(request, 'WorkerDocuments/documents.html', {'listado':listado})