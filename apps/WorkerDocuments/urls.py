from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='documents'),
    path('documents',views.documents,name='documents'),
]
