from django import forms
from django.forms import ModelForm

from core.servicios.pyra_par.models import PyParAPIToken

class APITokenForm(ModelForm):
    class Meta:
        model = PyParAPIToken
        fields = '__all__'

        widgets = {
            'user': forms.Select(
                attrs={
                    'class':'select'
                }
            )
        }