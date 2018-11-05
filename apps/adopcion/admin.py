from django.contrib import admin

from apps.adopcion.models import Persona, Ciudad, Region, Vivienda

# Register your models here.

admin.site.register(Persona)
admin.site.register(Ciudad)
admin.site.register(Region)
admin.site.register(Vivienda)