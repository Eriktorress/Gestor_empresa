from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render
from .models import Company
from apps.Workplace.models import Workplace
from apps.Worker.models import Worker
from .forms import CompanyForm
from django.contrib import messages

#Home
def home(request):
    return render(request, 'home.html')

#Listar empresa
def list_company(request):
    listado = Company.objects.all();
    return render(request, 'Company/list_company.html', {'listado':listado})

#Formulario empresa
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

#Eliminar empresa

def delet_company(request, id):
    company = get_object_or_404(Company, id_company=id)
    company.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="list_company")

#Editar empresa 
def edit_company(request, id):
    company = get_object_or_404(Company, id_company=id)
    workplaces = Workplace.objects.filter(id_company=id)
    workers = Worker.objects.filter(id_company=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
            return redirect('list_company')
    else:
        form = CompanyForm(instance=company)
    context = {
        'form': form,
        'company': company,
        'workplaces': workplaces,
        'workers': workers
    }
    return render(request, 'Company/edit_company.html', context)


#Filtrado de centros de la empresa 

def company_workplaces(request, company_id):
    company = get_object_or_404(Company, id_company=company_id)
    workplaces = Workplace.objects.filter(id_company=company_id)
    context = {
        'company': company,
        'workplaces': workplaces,
    }
    return render(request, 'Company/company_workplaces.html', context)


#Filtrado de trabajadores de la empresa 
def company_workers(request, company_id):
    company = get_object_or_404(Company, id_company=company_id)
    workers = Worker.objects.filter(id_company=company_id)
    context = {
        'company': company,
        'workers': workers,
    }
    return render(request, 'Company/company_workers.html', context)