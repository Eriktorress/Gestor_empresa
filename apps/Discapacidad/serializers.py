from rest_framework import serializers
from .models import Discapacidad 


class DiscapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model= Discapacidad
        fields = '__all__'

