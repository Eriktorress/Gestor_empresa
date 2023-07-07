from django import forms
from .models import Worker
from apps.Maintainers.models import Discapacidad

class WorkerForm(forms.ModelForm):
    id_Discapacidad = forms.ModelChoiceField(
        queryset=Discapacidad.objects.all(),
        label='Tiene discapacidad',
        widget=forms.Select(attrs={'id': 'id_Discapacidad'}),  # Se elimina el argumento `choices`
        required=False
    )

    class Meta:
        model = Worker
        fields = '__all__'


