from django import forms
from django.forms import widgets

from core.servicios.seoc.models import SeocAPIToken, SeocModel

class SeocAPIKeyForms(forms.ModelForm):

    class Meta:
        model = SeocAPIToken
        fields = '__all__'

        widgets = {
            'user': forms.Select(
                attrs={
                    'class':'select'
                }
            )
        }

class SeocForm(forms.ModelForm):

    class Meta:
        model = SeocModel
        fields = '__all__'

        widgets = {
            'estacion': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'input',
                    'placeholder':'Dia/Mes/Año'
                }
            ),
            'tiempo': forms.TimeInput(
                attrs={
                    'class': 'input',
                    'placeholder':'H:M:S'
                }
            ),
            'dc': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'dw': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'dnt': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'eoa': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            ),
            'eoan': forms.NumberInput(
                attrs={
                    'class': 'input',
                }
            )

        }
