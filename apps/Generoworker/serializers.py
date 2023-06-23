from rest_framework import serializers
from .models import Generoworker 


class GeneroworkerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Generoworker
        fields = '__all__'

