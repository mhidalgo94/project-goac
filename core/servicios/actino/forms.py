from django import forms
from core.servicios.actino.models import ActinoEstacionesModel, ActinoObservadorModel,ActinoHorarioVeranoModel

class EstacionesForm(forms.ModelForm):

	class Meta:
		model = ActinoEstacionesModel
		fields = "__all__"

		widgets = {
			'codigo': forms.TextInput(
				attrs={
				'class': 'input',
			}),
			'imagen':forms.FileInput(
				attrs={
					'class':"input",
					'autocomplete': 'off',
					'autofocus': 'on'
				}),
			'provincia': forms.TextInput(
				attrs={
				'class': 'input',
			}),
			'tipo': forms.TextInput(
				attrs={
				'class': 'input',
			}),
			'estacion': forms.TextInput(
				attrs={
				'class': 'input',
			}),
			'altura': forms.NumberInput(
				attrs={
				'class': 'input',
			}),
			'longitud': forms.NumberInput(
				attrs={
				'class': 'input',
			}),
			'latitud': forms.NumberInput(
				attrs={
				'class': 'input',
			}),
			
			'estado': forms.Select(
				attrs={
				'class': 'select',
			}),
		}

class ActinoHorarioVeranoForm(forms.ModelForm):

	class Meta:
		model = ActinoHorarioVeranoModel
		fields = ['horario_verano',]

		widgets = {
			'horario_verano': forms.CheckboxInput()
		}

class ObservadorForms(forms.ModelForm):

    class Meta:
        model = ActinoObservadorModel
        fields = '__all__'

        widgets = {
            'id':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Ingrese codigo de observador',
					'autocomplete': 'off'
				}
			),
			'nombre':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Ingrese su nombre',
					'autocomplete': 'off'
				}
			),
            'estacion':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Nombre Estacion',
					'autocomplete': 'off'
				}
			),
		}