from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=30, null = True)
    apellido = models.CharField(max_length=30, null = True)
    numero_id = models.IntegerField()
    fecha_ingreso = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    