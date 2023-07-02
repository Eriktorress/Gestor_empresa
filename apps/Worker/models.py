from django.db import models
from apps.Company.models import Company
from apps.Workplace.models import Workplace
from apps.Maintainers.models import Sexo, Estado, Discapacidad, Tipodiscapacidad, Region, Comuna
from django.core.exceptions import ValidationError
from django.db.models import Q

 #Modelo de trabajador.
class Worker(models.Model):
    id_worker = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombres', max_length=20)
    lastname = models.CharField(verbose_name='Apellidos', max_length=40)
    rut = models.CharField(verbose_name='RUT', max_length=9)
    address = models.CharField(verbose_name='Dirección', max_length=50)
    region = models.ForeignKey(Region, null=True, verbose_name='Región', on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, null=True, verbose_name='Comuna', on_delete=models.PROTECT)
    phone = models.CharField(verbose_name='Teléfono', max_length=10)
    email = models.EmailField(verbose_name='Email')
    id_company = models.ForeignKey(Company, verbose_name='Empresa', on_delete=models.PROTECT)
    estado_worker = models.ForeignKey(Estado, verbose_name='Estado', on_delete=models.PROTECT)
    sexo = models.ForeignKey(Sexo, verbose_name='Género', on_delete=models.PROTECT)
    id_workplace = models.ForeignKey(Workplace, null=True, blank=True, verbose_name='Centro', on_delete=models.PROTECT)
    id_Discapacidad = models.ForeignKey(Discapacidad, null=True,verbose_name='Tiene Alguna Discapacidad', on_delete=models.PROTECT)
    id_Tipo_discapacidad = models.ForeignKey(Tipodiscapacidad, null=True,verbose_name='Indique la que corresponda', on_delete=models.PROTECT)
    fec_nac = models.DateField(verbose_name='Fecha de Nacimiento (Formato año/mes/dia)', null=True)
    fec_ing = models.DateField(verbose_name='Fecha de Ingreso (Formato año/mes/dia)', null=True)

    def __str__(self):
        return f"{self.name}"
    
    def clean(self):
        validate_unique_rut(self.rut, self.id_company)
        super().clean()

def validate_unique_rut(value, company):
    # Validar la unicidad del RUT dentro del contexto de la empresa
    existing_workers = Worker.objects.filter(Q(rut=value) & Q(id_company=company))
    if existing_workers.exists():
        raise ValidationError('Ya existe un Worker con este RUT en la misma compañía.')
