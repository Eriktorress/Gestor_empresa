from django.db import models
from apps.Estado.models import Estado


class Company (models.Model):
    id_company = models.AutoField(primary_key=True)
    name_company = models.CharField (max_length=50)
    rut_company = models.CharField(max_length= 9)
    adress = models.CharField(max_length=50)
    comuna = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField ()
    estado_company = models.ForeignKey(Estado, on_delete=models.PROTECT)
    
    def __str__(self) :
<<<<<<< HEAD
        return f"{self.name_company} - {self.rut_company}"
=======
        return f"{self.name_company}"
    
>>>>>>> DB-MySQL

