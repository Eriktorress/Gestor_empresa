from dataclasses import field
from pyexpat import model
from django import forms
from .models import Company
from django.contrib.auth.forms import UserCreationForm


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'

