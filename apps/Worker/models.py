from django.db import models
from apps.Company.models import Company
from apps.Estado.models import Estado
from apps.Generoworker.models import Generoworker
from apps.Workplace.models import Workplace
from apps.Discapacidad.models import Discapacidad
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
    email = models.EmailField (verbose_name='Email')
    id_company = models.ForeignKey(Company,verbose_name='Empresa', on_delete=models.PROTECT)
    estado_worker = models.ForeignKey(Estado,verbose_name='Estado', on_delete=models.PROTECT)
    id_Genworker = models.ForeignKey(Generoworker,verbose_name='Género', on_delete=models.PROTECT)
    id_workplace = models.ForeignKey(Workplace,verbose_name='Centro',on_delete=models.PROTECT)
    id_Discapacidad = models.ForeignKey(Discapacidad,verbose_name='Tiene Alguna DIscapacidad',on_delete=models.PROTECT)
    #id_tipo_discapacidad
    #fec_nac
    #fec_ing
    
    
    
    def __str__(self) :
        return f"{self.name_worker}"
    