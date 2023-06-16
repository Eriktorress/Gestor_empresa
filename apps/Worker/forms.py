from dataclasses import field
from pyexpat import model
from django import forms
from .models import Worker
from django.contrib.auth.forms import UserCreationForm


class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = '__all__'
