from django.forms import ModelForm
from django import forms

from core.web.models import CatInvestigacionesModel, InvestigacionesModel, PublArtArbitrajeModel, PublEventosModel, WebModelo, ContactoModel, InstrumentoModel, NoticiasModels, PublReportesModel

class PortadaForm(ModelForm):

    class Meta:
        model = WebModelo
        field = '__all__'
        exclude = ['user_creacion','date_update']

        # labels = {
        #     'titulo_banner' : 'Titulo del B',
        #     'desc' : 'Descripcion'
        # }

        widgets = {
			'logo':forms.FileInput(
				attrs={
					'class':"input is-large",
					'placeholder': 'Inserte logotipo',
					'autocomplete': 'off',
                    'autofocus': 'on'
				}),
			'img_banner':forms.FileInput(
			attrs={
				'class':"input is-large",
				'placeholder': 'Inserte la banner',
				'autocomplete': 'off',
				'autofocus': 'on'
			}),
            'titulo_banner':forms.TextInput(
				attrs={
					'class':"input is-success",
					'placeholder': 'Ingrese el titulo del banner',
					'autocomplete': 'off',
                    'autofocus': 'on'
				}),
            'frase':forms.TextInput(
            attrs={
                'class':"input is-success",
                'placeholder': 'Ingrese la frase del banner',
                'autocomplete': 'off'
            }),
            'direccion':forms.TextInput(
				attrs={
					'class':"input is-normal is-success",
					'placeholder': '',
					'autocomplete': 'off'
				}),
            'postal':forms.TextInput(
            attrs={
                'class':"input is-normal is-success",
                'placeholder': '',
                'autocomplete': 'off'
            }),

            'nosotros': forms.Textarea(
                attrs={
                    'class': 'textarea is-success',
                    'placeholder': 'Inserte el texto',
                    'rows': '6',
                    'cols': '10'

                }
            ),
			'telefono':forms.TextInput(
                attrs={
					'class':"input is-normal is-success",
					'placeholder': '',
					'autocomplete': 'off'
                }),
			'correo':forms.EmailInput(
				attrs={
					'class':"input is-normal is-success",
					'placeholder': '',
					'autocomplete': 'off'
				}),
            'url_facebook' : forms.URLInput(
                attrs={
					'class':"input is-normal is-success",
					'placeholder': 'URL',
					'autocomplete': 'off'
				}),
            'url_Twitter' : forms.URLInput(
                attrs={
					'class':"input is-normal is-success",
					'placeholder': 'URL',
					'autocomplete': 'off'
				}),
            'url_Instagram' : forms.URLInput(
                attrs={
					'class':"input is-normal is-success",
					'placeholder': 'URL',
					'autocomplete': 'off'
				}),
            'footer_copyright': forms.TextInput(
            attrs={
                'class':"input is-normal is-success",
                'placeholder': 'Ingrese copyright del footer',
                'autocomplete': 'off'
            }),
		}


class InstrumentoForm(ModelForm):

	class Meta:
		model = InstrumentoModel
		fields = ['nombre', 'imagen', 'desc', 'contenido']
		labels = {
			'nombre': 'Nombre',
			'imagen': 'Imagen Instrumento',
			'desc': 'Descripcion'
		}
		widgets = {
			'nombre':forms.TextInput(
				attrs={
					'class':"input is-normal",
					'placeholder': 'Nombre del instrumento',
					'autocomplete': 'off',
					'autofocus': 'on'
				}),
			'imagen':forms.FileInput(
				attrs={
					'class':"input is-success",
					'placeholder': 'Ingrese el titulo del banner',
					'autocomplete': 'off',
					'autofocus': 'on'
				}),
			'desc': forms.Textarea(
				attrs={
					'class': 'textarea',
					'placeholder': 'Inserte el texto',
					'rows': '6',
					'cols': '10'

				}),
		}


class ContactoForm(ModelForm):
	
	class Meta:
		model = ContactoModel
		fields = ['nombre', 'subject', 'correo', 'mensaje']

		labels={
		'apellidos': 'Apellidos',
		'asunto': 'Asunto'
		}

		widgets = {
			'nombre':forms.TextInput(
				attrs={
					'class': 'input is-normal',
					'placeholder': 'Input full name',
					'autocomplete': 'off'
				}
			),
			'subject':forms.TextInput(
				attrs={
					'class':"input is-normal",
					'placeholder': 'Input Subject',
					'autocomplete': 'off'
				}),
			'correo':forms.EmailInput(
				attrs={
					'class':"input is-normal",
					'placeholder': 'Input email',
					'autocomplete': 'off'
				}),
			'mensaje':forms.Textarea(
				attrs={
					'class':'textarea',
					'placeholder':'Text...',
					'rows': '7',
					'autocomplete': 'off'
				}),
		}


class NoticiasForm(ModelForm):

	class Meta:
		model = NoticiasModels
		fields = ['titulo', 'desc', 'imagen', 'contenido', 'autor', 'doc','estado',]

		widgets ={
			'titulo': forms.TextInput(
				attrs={
					'class': 'input',
					'autocomplete': 'off',
				}
			),
			'desc': forms.Textarea(
				attrs={
					'class': 'textarea',
					'placeholder': 'Texto',
					'rows': '3',
				}
			),
			'imagen':forms.FileInput(
				attrs={
					'class':"input is-large",
					'placeholder': 'Inserte La Imagen',
					'autocomplete': 'off',
				}),
			'doc':forms.URLInput(
				attrs={
					'class':"input",
					'placeholder': 'Inserte URL Documento',
					'autocomplete': 'off',
				}),
		}


class PublReportesForm(ModelForm):

	class Meta:
		model = PublReportesModel
		fields = ['texto', 'doc', 'miembro','estado','anio', 'invest',]

		widgets ={
			'texto': forms.Textarea(
				attrs={
					'class': 'textarea',
					'placeholder': 'Texto',
					'rows': '4',
				}
			),
			'doc':forms.URLInput(
				attrs={
					'class':"input",
					'placeholder': 'Inserte URL Documento',
					'autocomplete': 'off',
				}),
			'miembro': forms.SelectMultiple(
				attrs={
					'class': 'select is-multiple select2',
					'multiple': 'multiple',
					'size' : '8'
				}),
			'anio': forms.NumberInput(
				attrs={
					'class':"input",
				}),
		}


class PublArtArbitrajeForm(ModelForm):

	class Meta:
		model = PublArtArbitrajeModel
		fields = ['texto', 'doc', 'miembro','estado','anio', 'invest',]

		widgets ={
			'texto': forms.Textarea(
				attrs={
					'class': 'textarea',
					'placeholder': 'Texto',
					'rows': '4',
				}
			),
			'doc':forms.URLInput(
				attrs={
					'class':"input",
					'placeholder': 'Inserte URL Documento',
					'autocomplete': 'off',
				}),
			'miembro': forms.SelectMultiple(
				attrs={
					'class': 'select is-multiple select2',
					'multiple': 'multiple',
					'size' : '8'
				}),
			'anio': forms.NumberInput(
				attrs={
					'class':"input",
				}),
		}


class PublEventosForm(ModelForm):

	class Meta:
		model = PublEventosModel
		fields = ['texto', 'doc', 'miembro','estado','anio', 'invest',]

		widgets ={
			'texto': forms.Textarea(
				attrs={
					'class': 'textarea',
					'placeholder': 'Texto',
					'rows': '4',
				}
			),
			'doc':forms.URLInput(
				attrs={
					'class':"input",
					'placeholder': 'Inserte URL Documento',
					'autocomplete': 'off',
				}),
			'miembro': forms.SelectMultiple(
				attrs={
					'class': 'select is-multiple select2',
					'multiple': 'multiple',
					'size' : '8'
				}),
			'anio': forms.NumberInput(
				attrs={
					'class':"input",
				}),
		}


class CatInvestigacionForm(ModelForm):

	class Meta:
		model = CatInvestigacionesModel
		fields = ['nombre',]

		widgets = {
			'nombre': forms.TextInput(
				attrs={
					'class':'input is-noraml',
					'placeholder': 'Ingrese el nombre nueva categoria',
					'autocomplete': 'off',
                    'autofocus': 'on'
				}
			)
		}

class InvestigacionesForm(ModelForm):
	class Meta:
		model = InvestigacionesModel
		fields = ['titulo', 'cat', 'texto','doc', 'miembro','estado','resumen','anio_inicial', 'anio_final',]

		labels = {
			"titulo": "Titulo"
		}

		widgets ={
			'titulo': forms.TextInput(
				attrs={
					'class':"input",
					'placeholder': 'Titulo de la investigacion',
					'autocomplete': 'off',
                    'autofocus': 'on'
				}
			),
			'texto': forms.Textarea(
				attrs={
					'class': 'textarea',
					'placeholder': 'Texto',
					'rows': '4',
				}
			),
			'doc':forms.URLInput(
				attrs={
					'class':"input",
					'placeholder': 'Inserte URL Documento',
					'autocomplete': 'off',
				}),
			'miembro': forms.SelectMultiple(
				attrs={
					'class': 'select is-multiple select2',
					'multiple': 'multiple',
					'size' : '8'
				}),
			'anio_inicial': forms.NumberInput(
				attrs={
					'class':"input",
				}),
			'anio_final': forms.NumberInput(
				attrs={
					'class':"input",
				}),			
		}