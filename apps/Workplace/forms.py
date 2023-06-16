from dataclasses import field
from pyexpat import model
from django import forms
from .models import Workplace
from django.contrib.auth.forms import UserCreationForm


class WorkplaceForm(forms.ModelForm):

    class Meta:
        model = Workplace
        fields = '__all__'

