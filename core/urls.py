from django.contrib import admin
from django.urls import path, re_path, include
from apps.Company.views import delet_company, form_company,list_company,edit_company,\
    home, company_workplaces
from apps.Users.views import signup,signout, signin
from apps.Workplace.views import list_workplace,form_workplace, edit_workplace,\
    delet_workplace
from apps.Worker.views import list_worker, form_worker,edit_worker,delet_worker
from apps.WorkerDocuments.views import list_workdoc,form_workdoc,edit_workdoc,delet_workdoc


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path ('', home, name='home'),
    
    
    #-------- Commpany --------
    path ('List_company/', list_company, name='list_company'),
    path ('Form_company/', form_company, name='form_company'),
    path ('Delete_company/<id>/', delet_company, name='delet_company'),
    path('Edit_company/<id>/', edit_company, name='edit_company'),
    
    path('company/<id>/', company_workplaces, name='company_workplaces'),

    #-------- Users --------
    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),

   #-------- Centros --------

    path ('List_workplace/', list_workplace, name='list_workplace'),
    path ('Form_workplace/', form_workplace, name='form_workplace'),
    path ('Edit_workplace/<id>/', edit_workplace, name='edit_workplace'),
    path ('Delete_workplace/<id>/', delet_workplace, name='delet_workplace'),

    #-----Worker-----
    path ('List_worker/', list_worker, name='list_worker'),
    path ('Form_worker/', form_worker, name='form_worker'),
    path ('Edit_worker/<id>/', edit_worker, name='edit_worker'),
    path ('Delete_worker/<id>/', delet_worker, name='delet_worker'),
    
    #-----WorkerDocuments-----
    path ('List_workdoc/', list_workdoc, name='list_workdoc'),
    path ('Form_workdoc/', form_workdoc, name='form_workdoc'),
    path ('Edit_workdoc/<id>/', edit_workdoc, name='edit_workdoc'),
    path ('Delet_workdoc/<id>/', delet_workdoc, name='delet_workdoc'),
]
