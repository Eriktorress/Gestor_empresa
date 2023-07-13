from django.contrib import admin
from django.urls import path, re_path, include
from apps.Company.views import delet_company, form_company,list_company,edit_company,\
    company_workplaces,company_workers, search_company, buscar_company
from apps.Users.views import signup,signout, list_usuarios,eliminar_usuario,editar_usuario,form_usuario,\
    buscar_usuarios
from apps.Workplace.views import list_workplace, form_workplace, edit_workplace,\
    delet_workplace
from apps.Worker.views import list_worker, form_worker,edit_worker,delet_worker,worker_documents,buscar_worker,\
    download_excel
from apps.WorkerDocuments.views import list_workdoc,form_workdoc,edit_workdoc,delet_workdoc
from apps.Maintainers.views import dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', dashboard, name='dashboard'),
    
    #-------- Users --------

    path('signin/', auth_views.LoginView.as_view(template_name='User/signin.html'), name='signin'),
    path('logout/', signout, name='logout'),
    path('signup/', signup, name='signup'),
    
    #-------- Usuarios --------
    path ('Listado_usuarios/', list_usuarios, name='list_usua'),
    path ('Formulario_Usuario/', form_usuario, name='form_Usuario'),
    path ('Editar_usuario/<id>/', editar_usuario, name='edit_usuario'),
    path ('Eliminar_usuario/<id>/', eliminar_usuario, name='elim_usuario'),
    path('buscar_usuarios/', buscar_usuarios, name='buscar_usuarios'),
    
     path('download_excel/', download_excel, name='download_excel'),
    #-------- Commpany --------
    path ('List_company/', list_company, name='list_company'),
    path ('Form_company/', form_company, name='form_company'),
    path ('Delete_company/<id>/', delet_company, name='delet_company'),
    path('Edit_company/<int:id>/', edit_company, name='edit_company'),

    path('company_workplaces/<int:company_id>/', company_workplaces, name='company_workplaces'),
    path('company_workers/<int:company_id>/', company_workers, name='company_workers'),
    
    path('search_company/', search_company, name='search_company'),
    path('buscar_company/', buscar_company, name='buscar_company'),


   #-------- Centros --------

    path ('List_workplace/', list_workplace, name='list_workplace'),
    path ('Form_workplace/', form_workplace, name='form_workplace'),
    path ('Edit_workplace/<id>/', edit_workplace, name='edit_workplace'),
    path ('Delete_workplace/<id>/', delet_workplace, name='delet_workplace'),

    #-----Worker-----
    path ('List_worker/', list_worker, name='list_worker'),
    path ('Form_worker/', form_worker, name='form_worker'),
    path ('Edit_worker/<int:id>/', edit_worker, name='edit_worker'),
    path ('Delete_worker/<id>/', delet_worker, name='delet_worker'),

    path('worker_documents/<int:worker_id>/', worker_documents, name='worker_documents'),
    path('buscar_worker/', buscar_worker, name='buscar_worker'),
    
    #-----WorkerDocuments-----
    path ('List_workdoc/', list_workdoc, name='list_workdoc'),
    path ('Form_workdoc/', form_workdoc, name='form_workdoc'),
    path ('Edit_workdoc/<id>/', edit_workdoc, name='edit_workdoc'),
    path ('Delet_workdoc/<id>/', delet_workdoc, name='delet_workdoc'),

  

]
