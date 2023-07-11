from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render
from .models import Workplace
from .forms import WorkplaceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#Listar centros de trabajo
@login_required
def list_workplace(request):
    listado = Workplace.objects.all();
    return render(request, 'Workplace/list_workplace.html', {'listado':listado})

#Formulario centro de trabajo
@login_required
def form_workplace(request):

    data = {
        'form': WorkplaceForm()
        
    }

    if request.method == 'POST':
        formworplace = WorkplaceForm (data=request.POST)
        if formworplace.is_valid():
            formworplace.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="list_workplace")
        else:
            data["form"] = formworplace
    return render(request, 'Workplace/form_workplace.html', data)

#Editar centro de trabajo
@login_required
def edit_workplace(request, id):
    workplace= get_object_or_404(Workplace, id_workplace=id)

    data = {
        'form': WorkplaceForm(instance=workplace)
    }
    
    if request.method == 'POST':
        formworplace = WorkplaceForm (data=request.POST, instance=workplace)
        if formworplace.is_valid():
            formworplace.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="list_workplace")
        data["form"] = formworplace

    
    return render (request, 'Workplace/edit_workplace.html', data)

#Editar eliminar centro
@login_required
def delet_workplace(request, id):
    workplace = get_object_or_404(Workplace, id_workplace=id)
    workplace.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="list_workplace")

