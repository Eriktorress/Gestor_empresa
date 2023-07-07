from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render
from .models import Worker
from .forms import WorkerForm
from apps.WorkerDocuments.models import WorkerDocuments


#Listar company de trabajos
def list_worker(request):
    listado = Worker.objects.all();
    
    return render(request, 'Worker/list_worker.html', {'listado':listado})

#Formulario centro de trabajo
def form_worker(request):

    data = {
        'form': WorkerForm(),
    }

    if request.method == 'POST':
        formulario_worker = WorkerForm (data=request.POST)
        if formulario_worker.is_valid():
            formulario_worker.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="list_worker")
        else:
            data["form"] = formulario_worker
            messages.error(request, "Error al guardar el formulario")
    return render(request, 'Worker/form_worker.html', data)

#Editar Trabajador
def edit_worker(request,id):
    worker = get_object_or_404(Worker, id_worker=id)
    workerdocuments = WorkerDocuments.objects.filter(id_worker=id)
    if request.method == 'POST':
        form = WorkerForm (request.POST, instance=worker)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="list_worker")
        else:
            messages.error(request, "Error al editar el formulario")
    else:
        form = WorkerForm(instance=worker)
        
    context = {
        'form': form,
        'worker': worker,
        'workerdocuments': workerdocuments
    }
    return render(request, 'Worker/edit_worker.html', context)

#Editar eliminar Trabajador

def delet_worker(request, id):
    worker = get_object_or_404(Worker, id_worker=id)
    worker.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="list_worker")

#Filtrado de Documentos del trabajador
def worker_documents(request, worker_id):
    worker = get_object_or_404(Worker, id_worker=worker_id)
    workerdocuments = WorkerDocuments.objects.filter(id_worker_id=worker_id)
    context = {
        'worker': worker,
        'workerdocuments': workerdocuments,
    }
    return render(request, 'Worker/worker_documents.html', context)