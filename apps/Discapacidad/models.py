from django.db import models

# Create your models here.
class Discapacidad (models.Model):
    id_Discapacidad = models.AutoField(primary_key=True)
    name= models.CharField (verbose_name='Descripcion',max_length=20 )
       
    
    def __str__(self) :
        return f"{self.name}"
