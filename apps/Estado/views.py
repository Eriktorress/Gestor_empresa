from django.shortcuts import render
from django.db import models
from .serializers import EstadocompanySerializer
from .models import Estado
# Create your views here.


#class EstadocompanySerializer(viewsets.ModelViewSet):
#    queryset = Estado.objects.all()
#    serializer_class = EstadocompanySerializer