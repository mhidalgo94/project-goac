from django.db.models import fields
from django.forms import ModelForm

from core.servicios.pyra_par.models import APIToken

class APITokenForm(ModelForm):
    class Meta:
        model = APIToken
        fields = ['user',]
