from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkerDocuments
from .forms import WorkerDocuments
from .views import WorkerDocuments
from django.contrib import messages



# Create your views here.
def list_workdoc(request):
    listado = WorkerDocuments.objects.all();
    return render(request, 'WorkerDocuments/list_workdoc.html', {'listado':listado})

#Formulario centro de trabajo
def form_workdoc(request):
    return render(request, 'WorkerDocuments/form_workdoc.html')
#Editar centro de trabajo
def edit_workdoc(request):
    return render(request, 'WorkerDocuments/edit_workdoc.html')
#Editar eliminar centro
def delet_workdoc(request):
    return render(request, 'WorkerDocuments/list_workdoc.html')
def crear_workdoc(request):
    return render(request, 'WorkerDocuments/crear_workdoc.html')
