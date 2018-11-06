from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota

		fields = [
			'foto',
			'nombre',
			'raza',
			'descripcion',
			'estado',
		]

		labels = {
			'foto': 'Foto',
			'nombre': 'Nombre',
			'raza': 'Raza',
			'descripcion': 'Descripción',
			'estado': 'Estado',
		}

		widgets = {
			'foto': forms.FileInput(),
			'nombre': forms.TextInput(attrs={'class':'form-control col-xs-12'}),
			'raza': forms.TextInput(attrs={'class':'form-control col-xs-12'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control col-xs-12'}),
			'estado': forms.TextInput(attrs={'class':'form-control col-xs-12'}),
		} 