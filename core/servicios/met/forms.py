from django import forms
from django.db.models import fields
from django.forms import widgets

from core.servicios.met.models import MetModel, MetAPITokenModel, MetHistoricosModel

class MetAPIKeyForms(forms.ModelForm):

    class Meta:
        model = MetAPITokenModel
        fields = '__all__'

        widgets = {
            'user': forms.Select(
                attrs={
                    'class':'select'
                }
            )
        }

class MetForm(forms.ModelForm):

    class Meta:
        model = MetModel
        fields = '__all__'

        widgets = {
            'fecha': forms.DateTimeInput(
                attrs={
                    'class': 'input',
                    'placeholder':'Dia/Mes/Año H/M/S'
                }
            ),
            'ta': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'hr': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'vv': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'dv': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'ri': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'hi': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'rc': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'hc': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'pr': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),

        }

class MetHistoricosForm(forms.ModelForm):

    class Meta:
        model = MetHistoricosModel
        fields = '__all__'

        widgets = {
            'fecha': forms.DateTimeInput(
                attrs={
                    'class':'input',
                    'type': 'datetime',
                    'placeholder': 'D/M/Y H:M:S'
                }
            ),
            'variable': forms.TextInput(
                attrs={
                    'class':'input',
                    'placeholder': 'Nombre variable'
                }
            ),
            'tipo': forms.Select(
                attrs={
                    'class':'select'
                }
            ),
            'valor': forms.NumberInput(
                attrs={
                    'class':'input',
                    'placeholder': 'Datos correspondiente'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'input',
                    'placeholder': 'Nombre Asignado'
                }
            ),
            'unidad_medida': forms.TextInput(
                attrs={
                    'class':'input',
                    'placeholder':'Unidad de Medida'
                }
            )
        }
