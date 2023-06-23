from rest_framework import serializers
from .models import Tipodiscapacidad 


class TipodiscapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tipodiscapacidad
        fields = '__all__'

