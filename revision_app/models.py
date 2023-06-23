from django.db import models

# Create your models here.

class GatoModel(models.Model):
    nombre=models.CharField(max_length=10)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField(null=True)