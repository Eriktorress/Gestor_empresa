from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render
from .models import Worker
from .forms import WorkerForm
from django.contrib import messages

# Create your views here.

#Listar company de trabajos
def list_worker(request):
    listado = Worker.objects.all();
    return render(request, 'Worker/list_worker.html', {'listado':listado})

#Formulario centro de trabajo
def form_worker(request):

    data = {
        'form': WorkerForm()
    }

    if request.method == 'POST':
        formulario_worker = WorkerForm (data=request.POST)
        if formulario_worker.is_valid():
            formulario_worker.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="list_worker")
        else:
            data["form"] = formulario_worker
    return render(request, 'Worker/form_worker.html', data)

#Editar centro de trabajo
def edit_worker(request, id):
    worker= get_object_or_404(Worker, id_worker=id)

    data = {
        'form': WorkerForm(instance=worker)
    }
    
    if request.method == 'POST':
        formulario2 = WorkerForm (data=request.POST, instance=worker)
        if formulario2.is_valid():
            formulario2.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="list_worker")
        data["form"] = formulario2

    return render (request, 'Worker/edit_worker.html', data)

#Editar eliminar centro

def delet_worker(request, id):
    worker = get_object_or_404(Worker, id_worker=id)
    worker.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="list_worker")