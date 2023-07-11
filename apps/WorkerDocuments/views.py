from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render
from .forms import WorkerDocumentsForm,WorkerDocuments
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def list_workdoc(request):
    listado = WorkerDocuments.objects.all();
    return render(request, 'WorkerDocuments/list_workdoc.html', {'listado':listado})

#Formulario 
@login_required
def form_workdoc(request):
    data = {
        'form': WorkerDocumentsForm()
    }

    if request.method == 'POST':
        formulariowd = WorkerDocumentsForm(request.POST, request.FILES)
        if formulariowd.is_valid():
            formulariowd.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect('list_workdoc')
        else:
            data["form"] = formulariowd

    return render(request, 'WorkerDocuments/form_workdoc.html', data)


#Editar 
@login_required
def edit_workdoc(request, id):
    document = get_object_or_404(WorkerDocuments, id=id)
    data = {
        'form': WorkerDocumentsForm(instance=document)
    }
    
    if request.method == 'POST':
        form = WorkerDocumentsForm(data=request.POST, instance=document)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
            return redirect('list_workdoc')
        data["form"] = form

    return render(request, 'WorkerDocuments/edit_workdoc.html', data)

@login_required
def delet_workdoc(request, id):
    document = get_object_or_404(WorkerDocuments, id=id)
    document.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect('list_workdoc')

