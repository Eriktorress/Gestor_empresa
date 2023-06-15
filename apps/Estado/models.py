from django.db import models

# Create your models here.
class Estado (models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.estado}"