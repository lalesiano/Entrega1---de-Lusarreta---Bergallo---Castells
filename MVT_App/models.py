from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_id = models.IntegerField()
    fecha_ingreso = models.DateField(null=True)