
from django.urls import path, include
from .views import list_worker, form_worker,edit_worker,delet_worker, home

urlpatterns = [

    #-------- Companies ----------
    path ('List_worker/', list_worker, name='list_worker'),
    path ('Form_worker/', form_worker, name='form_worker'),
    path ('Edit_worker/<id>/', edit_worker, name='edit_worker'),
    path ('Delete_worker/<id>/', delet_worker, name='delet_worker'),
    
]
