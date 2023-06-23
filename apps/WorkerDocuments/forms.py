from dataclasses import field
from pyexpat import model
from django import forms
from .models import WorkerDocuments
from django.contrib.auth.forms import UserCreationForm


class WorkerDocumentsForm(forms.ModelForm):

    class Meta:
        model = WorkerDocuments
        fields = '__all__'
