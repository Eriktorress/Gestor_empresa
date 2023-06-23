from rest_framework import serializers
from .models import Tipodocumento


class TipodocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tipodocumento
        fields = '__all__'

