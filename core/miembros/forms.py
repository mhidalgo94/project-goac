from django.forms import ModelForm
from django import forms

from core.miembros.models import MiembrosModel, SCientificaModel

class SCientificaForm(ModelForm):
    # miembro = forms.ModelChoiceField(queryset=MiembrosModel.objects.all())
    class Meta:
        model = SCientificaModel
        fields = ['nombre', 'url', 'desc']

        widgets = {
            
            'nombre':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Nombre Sociedad',
					'autocomplete': 'off'
				}),
            'url' : forms.URLInput(
                attrs={
					'class':"input is-normal ml-2",
					'placeholder': 'Dirección de la Sociedad Científica',
					'autocomplete': 'off'
				}),
			 'desc':forms.Textarea(
				attrs={
					'class': 'textarea is-normal ml-2',
					'placeholder': 'No es requerido',
					'autocomplete': 'off',
					'rows': '7',
					'autocomplete': 'off',
				}),
        }

class MiembrosForm(ModelForm):
	class Meta:
		model = MiembrosModel
		fields = ['estado','nombre','apellidos','imagen','correo','telefono','fech_nacido','sexo','t_trabajo','biografia', 'curriculo','ocupacion', 'scientifca']

		widgets = {
			'nombre':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Ingrese su nombre',
					'autocomplete': 'off'
				}),
			'apellidos':forms.TextInput(
				attrs={
					'class':"input is-normal ml-2",
					'placeholder': 'Ingrese sus apellidos',
					'autocomplete': 'off'
				}),
			'imagen':forms.FileInput(
				attrs={
					'class':"input is-success",
					'autocomplete': 'off',
					'autofocus': 'on'
				}),
			'correo':forms.EmailInput(
				attrs={
					'class':"input is-normal ml-1",
					'placeholder': 'Correo electrónico',
					'autocomplete': 'off'
				}),
			'telefono':forms.TextInput(
				attrs={
					'class':"input is-normal ml-1",
					'placeholder': 'Número Telefónico',
					'autocomplete': 'off'
				}),
			'ocupacion':forms.TextInput(
				attrs={
					'class':"input is-normal ml-1",
					'placeholder': 'Ocupación Laboral',
					'autocomplete': 'off'
				}),
			'biografia':forms.Textarea(
				attrs={
					'class':'textarea ml-2',
					'placeholder':'Contenido...',
					'rows': '7',
					'autocomplete': 'off'
				}),
			'curriculo':forms.URLInput(
				attrs={
					'class':'input ml-2',
					'placeholder':'Ingrese URL',
					'rows': '7',
					'autocomplete': 'off'
				}),
			'scientifca': forms.SelectMultiple(
				attrs={
					'class': 'select is-multiple select2',
					'multiple': 'multiple',
					'size' : '8'
				})
			
		}

