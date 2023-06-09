from django.db import models

# Create your models here.
class Socio(models.Model):
    id = models.AutoField(primary_key=True)
    compania = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100, null=True)
    cedula = models.IntegerField(null=True)
    ruc = models.BigIntegerField()
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    email = models.CharField(max_length=100)