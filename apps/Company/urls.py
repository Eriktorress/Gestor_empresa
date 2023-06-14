from django.urls import path, include
from .views import delet_company, form_company,list_company,edit_company, home

urlpatterns = [

    #-------- Companies ----------
    path ('', home, name='home'),
    path ('List_company/', list_company, name='list_company'),
    path ('Form_company/', form_company, name='form_company'),
    path ('Edit_company/<id>/', edit_company, name='edit_company'),
    path ('Delete_company/<id>/', delet_company, name='delet_company'),

]