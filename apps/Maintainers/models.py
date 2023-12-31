from django.db import models

# Modelo de genero.
class Sexo(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Sexo', max_length=10)
    
    def __str__(self):
        return f"{self.name}"
    
# Modelo de estado.
class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Estado', max_length=10)

    def __str__(self):
        return f"{self.name}"
    
# Modelo de Discapacidad.
class Discapacidad(models.Model):
    id_Discapacidad = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Discapacidad', max_length=2)

    def __str__(self):
        return self.name

# Modelo de Tipo Discapacidad.
class Tipodiscapacidad(models.Model):
    id_Tipo_discapacidad = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Tipo discapacidad', max_length=40)

    def __str__(self):
        return f"{self.name}"
    
# Modelo de Región .
class Region(models.Model):
    id_Region = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Región', max_length=50)

    def __str__(self):
        return f"{self.name}"
    
# Modelo de Comuna.
class Comuna(models.Model):
    id_Comuna = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Comunas', max_length=20)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

# Modelo de Comuna.
class Tipodocumento(models.Model):
    id_Tipo_doc= models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Archivo', max_length=40)

    def __str__(self):
        return f"{self.name}"