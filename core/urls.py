from django.contrib import admin
from django.urls import path, re_path, include
<<<<<<< HEAD
from apps.Company.views import delet_company, form_company,list_company,edit_company,\
    home, company_workplaces
from apps.Users.views import signup,signout, signin
from apps.Workplace.views import list_workplace,form_workplace, edit_workplace,\
    delet_workplace
=======
from apps.Company.views import list_company, form_company,edit_company,delet_company,\
    home
from apps.Worker.views import list_worker, form_worker,edit_worker,delet_worker

>>>>>>> DB-MySQL

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path ('', home, name='home'),
<<<<<<< HEAD
    
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

   #-------- Users --------

    path ('List_workplace/', list_workplace, name='list_workplace'),
    path ('Form_workplace/', form_workplace, name='form_workplace'),
    path ('Edit_workplace/<id>/', edit_workplace, name='edit_workplace'),
    path ('Delete_workplace/<id>/', delet_workplace, name='delet_workplace'),

    
=======
#-----Company-----
    path('apps/', include('apps.Company.urls')),
    path ('List_company/', list_company, name='list_company'),
    path ('Form_company/', form_company, name='form_company'),
    path ('Edit_company/<id>/', edit_company, name='edit_company'),
    path ('Delet_company/<id>/', delet_company, name='delet_company'),
#-----Worker-----
    path ('List_worker/', list_worker, name='list_worker'),
    path ('Form_worker/', form_worker, name='form_worker'),
    path ('Edit_worker/<id>/', edit_worker, name='edit_worker'),
    path ('Delete_worker/<id>/', delet_worker, name='delet_worker'),
>>>>>>> DB-MySQL
    
]
