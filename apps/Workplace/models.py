from django.db import models
from apps.Company.models import Company
from apps.Maintainers.models import Estado, Region, Comuna
class Workplace (models.Model):
    id_workplace = models.AutoField(primary_key=True)
    name_workplace = models.CharField (max_length=50)
    address = models.CharField(max_length=50)
    region = models.ForeignKey(Region, null=True, verbose_name='Región', on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, null=True, verbose_name='Comuna', on_delete=models.PROTECT)
    phone = models.CharField(max_length=10)
    estado_workplace = models.ForeignKey(Estado, on_delete=models.PROTECT)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT)
    
    def __str__(self) :
        return f"{self.name_workplace} - {self.address}"
