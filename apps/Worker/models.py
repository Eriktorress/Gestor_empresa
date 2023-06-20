from django.db import models
from apps.Company.models import Company
from apps.Estado.models import Estado
from apps.Generoworker.models import Generoworker
from apps.Workplace.models import Workplace
import email 


# Create your models here.
class Worker (models.Model):
    id_worker = models.AutoField(primary_key=True)
    name= models.CharField (verbose_name='Nombres',max_length=20 )
    lastname= models.CharField (verbose_name='Apellidos',max_length=40)
    rut = models.CharField(verbose_name='RUT',max_length= 9)
    adress = models.CharField(verbose_name='Dirección',max_length=50)
    region = models.CharField(verbose_name='Región',max_length=20)
    comuna = models.CharField(verbose_name='Comuna',max_length=20)
    phone = models.CharField(verbose_name='Teléfono',max_length=10)
    email = models.EmailField ()
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT)
    estado_worker = models.ForeignKey(Estado, on_delete=models.PROTECT,null=True)
    id_Genworker = models.ForeignKey(Generoworker, on_delete=models.PROTECT,null=True)
    id_workplace = models.ForeignKey(Workplace,on_delete=models.PROTECT,null=True,)
    #discapacidad = models.CharField(verbose_name='Tiene Alguna Discapacidad',max_length=1)
    #id_discapacidad
    #fec_nac
    #fec_ing
    
    
    
    def __str__(self) :
        return f"{self.name_worker}"
    