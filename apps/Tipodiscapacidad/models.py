from django.db import models

# Create your models here.
class Tipodiscapacidad (models.Model):
    id_tipo_discapacidad = models.AutoField(primary_key=True)
    name= models.CharField (verbose_name='Descripcion',max_length=40 )
       
    
    def __str__(self) :
        return f"{self.name}"
