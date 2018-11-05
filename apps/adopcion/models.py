from django.db import models

# Create your models here.

class Persona(models.Model):
	email = models.EmailField()
	run = models.CharField(primary_key=True, max_length=12)
	nombre = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	telefono = models.CharField(max_length=12)
	region = models.TextField()
	ciudad = models.TextField()
	tipo_vivienda = models.TextField()

