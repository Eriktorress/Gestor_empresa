from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render
from .models import Company
from apps.Workplace.models import Workplace
from apps.Worker.models import Worker
from .forms import CompanyForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
import plotly.graph_objects as go
from django.db.models import Count

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
            return redirect(to="list_company")
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

#Buscador de 

def search_company(request):
    id_company = request.GET.get('id_company')
    if id_company is None:
        print("Empresa no tomada")  # Imprime el mensaje en la consola del servidor
    else:
        print(id_company)  # Imprime el valor del ID de la empresa en la consola del servidor

    query = request.GET.get('q', '')

    if query:
        results = Company.objects.filter(name_company__icontains=query)
        results = [
            {
                'id_company': company.id_company,
                'name_company': company.name_company,
                'worker_count': Worker.objects.filter(id_company=company.id_company).count(),
                'workerplace_count': Workplace.objects.filter(id_company=company.id_company).count(),
                'male_count': Worker.objects.filter(id_company=company.id_company, sexo__name='Masculino').count(),
                'female_count': Worker.objects.filter(id_company=company.id_company, sexo__name='Femenino').count(),
                'disability_count_yes': Worker.objects.filter(id_company=company.id_company, id_Discapacidad__name='Si').count(),
                'disability_count_no': Worker.objects.filter(id_company=company.id_company, id_Discapacidad__name='No').count(),
                'workerplace_count_act': Worker.objects.filter(id_company=company.id_company, estado_worker__name='Activo').count(),
                'disability_count_Intelectual': Worker.objects.filter(id_company=company.id_company, id_Tipo_discapacidad__name='Intelectual o Cognitiva').count(),
                'disability_count_Sensorial_Visual': Worker.objects.filter(id_company=company.id_company, id_Tipo_discapacidad__name='Sensorial Visual').count(),
                'disability_count_Sensorial_Auditiva': Worker.objects.filter(id_company=company.id_company, id_Tipo_discapacidad__name='Sensorial Auditiva').count(),
                'disability_count_Psíquica_Mental': Worker.objects.filter(id_company=company.id_company, id_Tipo_discapacidad__name='Psíquica o Mental').count(),
                'disability_count_Visceral': Worker.objects.filter(id_company=company.id_company, id_Tipo_discapacidad__name='Visceral').count(),
                'disability_count_Física': Worker.objects.filter(id_company=company.id_company, id_Tipo_discapacidad__name='Física').count(),
            
            }
            for company in results
        ]
    else:
        results = []

    # Verifica si la solicitud es una petición AJAX (por ejemplo, realizada por el buscador)
    if request.is_ajax():
        return JsonResponse(results, safe=False)

    # Si no es una petición AJAX, renderiza la plantilla del Dashboard.html con los resultados de búsqueda y el gráfico de torta
    return render(request, 'dashboard.html', {'results': results, 'id_company': id_company})





