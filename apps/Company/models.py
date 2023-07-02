from django.db import models
from apps.Maintainers.models import Estado, Region, Comuna


class Company (models.Model):
    id_company = models.AutoField(primary_key=True)
    name_company = models.CharField (max_length=50)
    rut_company = models.CharField(max_length= 9)
    address = models.CharField(max_length=50)
    region = models.ForeignKey(Region, null=True, verbose_name='Región', on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, null=True, verbose_name='Comuna', on_delete=models.PROTECT)
    phone = models.CharField(max_length=10)
    email = models.EmailField ()
    estado_company = models.ForeignKey(Estado, on_delete=models.PROTECT)
    
    def __str__(self) :
        return f"{self.name_company} - {self.rut_company}"

