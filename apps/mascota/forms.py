from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota

		fields = [
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',
		]

		label = {
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad_aproximada': 'Edad Aproximada',
			'fecha_rescate': 'Fecha rescate',
			'persona': 'Persona',
			'vacuna': 'Vacuna',

		}

		widgets = {
			'nombre': forms.TextInput(attrs={'clas':'form-control'}),
			'sexo': forms.TextInput(attrs={'clas':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs={'clas':'form-control'}),
			'fecha_rescate': forms.TextInput(attrs={'clas':'form-control'}),
			'persona': forms.Select(attrs={'clas':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),


		}