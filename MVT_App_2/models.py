from django.db import models

# Create your models here.

class Autos(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    conductor = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="foto")

    def __str__(self):
        return f'Marca: {self.marca} - Modelo:{self.modelo}'