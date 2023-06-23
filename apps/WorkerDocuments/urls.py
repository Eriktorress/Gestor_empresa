from django.urls import path
from . import views

urlpatterns = [
    path('documents',views.list_workdoc,name='list_workdoc'),
]
