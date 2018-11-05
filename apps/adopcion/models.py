from django.db import models
from apps.mascota.models import Mascota

# Create your models here.

class Region(models.Model):
	nombre_region = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre_region)

class Ciudad(models.Model):
	nombre_ciudad = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre_ciudad)

class Vivienda(models.Model):
	tipo_vivienda = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.tipo_vivienda)


class Persona(models.Model):
	email = models.EmailField()
	run = models.CharField(primary_key=True, max_length=12)
	nombre = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	telefono = models.CharField(max_length=12)
	Region = models.ManyToManyField(Region, blank=True)
	Ciudad = models.ManyToManyField(Ciudad, blank=True)
	Vivienda = models.ManyToManyField(Vivienda, blank=True)

