from django.db import models
from django.utils import timezone
from datetime import date, time, datetime

# Create your models here.

class Recurso(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)

class Info_Sesion(models.Model):
    fecha = models.DateField("Fecha Creación", default=date.today())
    hora = models.TimeField("Hora Creación", default=timezone.now)
    descripcion = models.TextField(max_length=8000)
    recurso = models.ForeignKey(Recurso, on_delete=models.DO_NOTHING, null=True)
