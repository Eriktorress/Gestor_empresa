from django.db import models

# Create your models here.
class Generoworker (models.Model):
    id_Genworker = models.AutoField(primary_key=True)
    name= models.CharField (verbose_name='Descripcion',max_length=20 )
       
    
    def __str__(self) :
        return f"{self.name}"
