from django.db import models
from apps.Worker.models import Worker
from apps.Tipodocumento.models import Tipodocumento

class WorkerDocuments (models.Model):
    id = models.AutoField(primary_key=True)
    id_worker = models.ForeignKey(Worker,on_delete=models.PROTECT)
    id_tipo_doc = models.ForeignKey(Tipodocumento,on_delete=models.PROTECT)
    
    
    def __str__(self) :
        return f"{self.name}"
    