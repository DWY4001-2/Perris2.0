from django import forms

from apps.adopcion.models import Persona

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
			'email': forms.TextInput(attrs={'class':'form-comtrol'}),
			'run': forms.TextInput(attrs={'class':'form-comtrol'}),
			'nombre': forms.TextInput(attrs={'class':'form-comtrol'}),
			'fecha_nacimiento': forms.SelectDateWidget(attrs={'class':'form-comtrol'}),
			'telefono': forms.TextInput(attrs={'class':'form-comtrol'}),
			'Region': forms.Select(attrs={'class':'form-comtrol'}),
			'Ciudad': forms.Select(attrs={'class':'form-comtrol'}),
			'Vivienda': forms.Select(attrs={'class':'form-comtrol'}),
		}