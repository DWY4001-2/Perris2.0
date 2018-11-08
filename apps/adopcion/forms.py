from django import forms

from apps.adopcion.models import Persona
from django.forms import extras 

class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona

		fields = [
		'email',
		'run',
		'nombre',
		'fecha_nacimiento',
		'telefono',
		'Region',
		'Ciudad',
		'Vivienda',
		]

		labels = {
			'email': 'Email',	
			'run': 'Rut',	
			'nombre': 'Nombre',
			'fecha_nacimiento': 'Fecha de Nacimiento',
			'telefono': 'Teléfono',
			'Region': 'Región',
			'Ciudad': 'Ciudad',
			'Vivienda': 'Tipo de Vivienda',
		}

		widgets = {
			'email': forms.EmailInput(),
			'run': forms.TextInput(),
			'nombre': forms.TextInput(),
			'fecha_nacimiento': forms.SelectDateWidget(years = 
				('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', 
     			'1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', 
     			'1996', '1997', '1998', '1999', '2000')),
			'telefono': forms.TextInput(),
			'Region': forms.Select(),
			'Ciudad': forms.Select(),
			'Vivienda': forms.Select(),

		}
