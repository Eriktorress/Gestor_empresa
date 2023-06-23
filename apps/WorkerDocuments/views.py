from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render
from .forms import WorkerDocuments
from django.contrib import messages


# Create your views here.
def list_workdoc(request):
    listado = WorkerDocuments.objects.all();
    return render(request, 'WorkerDocuments/list_workdoc.html', {'listado':listado})

#Formulario 


def form_workdoc(request):

    data = {
        'form': WorkerDocuments() 
             }
    if request.method == 'POST':
        formulariowd = WorkerDocuments (data=request.POST)
        if formulariowd.is_valid():
            formulariowd.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="form_workdoc")
        else:
            data["form"] = formulariowd
    return render(request, 'WorkerDocuments/form_workdoc.html', data)

#Editar 
def edit_workdoc(request, id):
    documents= get_object_or_404(WorkerDocuments, id=id)

    data = {
        'form': WorkerDocuments(instance=documents)
    }
    
    if request.method == 'POST':
        formulariowd = WorkerDocuments (data=request.POST, instance=documents)
        if formulariowd.is_valid():
            formulariowd.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="list_workdoc")
        data["form"] = formulariowd

    
    return render (request, 'WorkerDocuments/edit_workdoc.html', data)
#Editar eliminar 
def delet_workdoc(request, id):
    workerdocuments = get_object_or_404(WorkerDocuments, id=id)
    workerdocuments.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="list_workdoc")
