from django.contrib import admin
from django.urls import path, re_path, include
from apps.Company.views import delet_company, form_company,list_company,edit_company,\
    home


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path ('', home, name='home'),
    path('apps/', include('apps.Company.urls')),
    
    path ('List_company/', list_company, name='list_company'),
    path ('Form_company/', form_company, name='form_company'),
    path ('Edit_company/<id>/', edit_company, name='edit_company'),
    path ('Delete_company/<id>/', delet_company, name='delet_company'),
]
