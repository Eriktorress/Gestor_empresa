from django.contrib import admin
from django.urls import path, re_path, include
from apps.Company.views import list_company, form_company,edit_company,delet_company,\
    home
from apps.Worker.views import list_worker, form_worker,edit_worker,delet_worker


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path ('', home, name='home'),
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
    
]
