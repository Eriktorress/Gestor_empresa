from rest_framework import serializers
from .models import Estado 


class EstadocompanySerializer(serializers.ModelSerializer):
    class Meta:
        model= Estado
        fields = '__all__'

