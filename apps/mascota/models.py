from django.db import models

# Create your models here.

class Mascota(models.Model):
	foto = models.ImageField()
	nombre = models.CharField(max_length=10)
	raza = models.CharField(max_length=20)
	descripcion = models.TextField()
	estado = models.CharField(max_length=10)