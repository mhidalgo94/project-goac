from django import forms

from core.talleres.models import ResumenesTallerModel, TallerModel, ParticipantesTallerModel

class TallerForm(forms.ModelForm):


    class Meta:
        model = TallerModel
        fields = '__all__'

        widgets = {
			'titulo':forms.TextInput(
				attrs={
					'class': 'input is-normal',
					'placeholder': 'Ingrese el titulo del Taller',
					'autocomplete': 'off'
				}),
			'descripcion':forms.Textarea(
				attrs={
					'class': 'textarea',
					'placeholder': 'Descripcion del Taller',
				}),
            'participantes':forms.SelectMultiple(
				attrs={
					'class': 'select2 is-multiple',
					'multiple': 'multiple',
                    'placeholder': 'Seleccione Participantes del Taller'
				})
        }

class ParticipantesTallerForm(forms.ModelForm):


    class Meta:
        model = ParticipantesTallerModel
        fields = '__all__'

        widgets = {
			'participantes':forms.SelectMultiple(
				attrs={
					'class': 'select2 is-multiple',
					'multiple': 'multiple'
				})
        }

class ResumenesTForm(forms.ModelForm):

	class Meta:
		model = ResumenesTallerModel
		fields = ['titulo','resumen', 'taller','participantes']

		widgets = {
			'titulo':forms.TextInput(
				attrs={
					'class': 'input is-normal',
					'placeholder': 'Ingrese el titulo del Resumen',
					'autocomplete': 'off'
				}),
			'taller':forms.SelectMultiple(
				attrs={
					'class': 'select2 is-multiple',
					'multiple': 'multiple',
                    'placeholder': 'Seleccione Taller Relacionado'
				}),
            'participantes':forms.SelectMultiple(
				attrs={
					'class': 'select2 is-multiple',
					'multiple': 'multiple',
                    'placeholder': 'Seleccione Participantes del Taller'
				})
        }
		



