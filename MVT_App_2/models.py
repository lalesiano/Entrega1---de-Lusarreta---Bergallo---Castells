from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Autos(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    ano = models.IntegerField()