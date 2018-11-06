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
			'email': forms.EmailInput(attrs={'class':'form-group-sm col-xs-6 center-xs'}),
			'run': forms.TextInput(attrs={'class':'form-group col-xs-6 center-xs'}),
			'nombre': forms.TextInput(attrs={'class':'form-group col-xs-6 center-xs'}),
			'fecha_nacimiento': forms.SelectDateWidget(attrs={'class':'form-group col-xs-6 center-xs'}),
			'telefono': forms.TextInput(attrs={'class':'form-group col-xs-6 center-xs'}),
			'Region': forms.Select(attrs={'class':'form-group col-xs-6 center-xs'}),
			'Ciudad': forms.Select(attrs={'class':'form-group col-xs-6 center-xs'}),
			'Vivienda': forms.Select(attrs={'class':'form-group col-xs-6 center-xs'}),
		}