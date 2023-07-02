from django.db import models
from apps.Worker.models import Worker
from apps.Maintainers.models import Tipodocumento

class WorkerDocuments (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre',max_length=100)
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    descripcion = models.TextField(verbose_name='Descripción')
    id_worker = models.ForeignKey(Worker,on_delete=models.PROTECT)
    id_tipo_doc = models.ForeignKey(Tipodocumento,on_delete=models.PROTECT)
    
    
    def __str__(self) :
        return f"{self.name}"
    