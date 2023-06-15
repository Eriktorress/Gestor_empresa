from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render
from .models import Company
from .forms import CompanyForm
from django.contrib import messages

# Create your views here.

def home(request):  #PAGINA 1
    return render(request, 'home.html')

#Listar company de trabajos
def list_company(request):
    listado = Company.objects.all();
    return render(request, 'Company/list_company.html', {'listado':listado})

#Formulario centro de trabajo
def form_company(request):

    data = {
        'form': CompanyForm()
        
    }

    if request.method == 'POST':
        formulario2 = CompanyForm (data=request.POST)
        if formulario2.is_valid():
            formulario2.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="list_company")
        else:
            data["form"] = formulario2
    return render(request, 'Company/form_company.html', data)

#Editar centro de trabajo
def edit_company(request, id_company):
    company= get_object_or_404(Company, id_company)

    data = {
        'form': CompanyForm(instance=company)
    }
    
    if request.method == 'POST':
        formulario2 = CompanyForm (data=request.POST, instance=company)
        if formulario2.is_valid():
            formulario2.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="list_company")
        data["form"] = formulario2

    
    return render (request, 'Company/edit_company.html', data)

#Editar eliminar centro

def delet_company(request, id):
    company = get_object_or_404(Company, id_company=id)
    company.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="list_company")