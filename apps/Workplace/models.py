from django.db import models
from apps.Estado.models import Estado
from apps.Company.models import Company

class Workplace (models.Model):
    id_workplace = models.AutoField(primary_key=True)
    name_workplace = models.CharField (max_length=50)
    adress = models.CharField(max_length=50)
    comuna = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    estado_workplace = models.ForeignKey(Estado, on_delete=models.PROTECT)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT)
    
    def __str__(self) :
        return f"{self.name_workplace} - {self.adress}"
