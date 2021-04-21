from core.usuarios.models import Usuarios
from django import forms
from django.contrib.auth.views import UserModel



class PwdResetForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nombre de usuario para enviarle un correo',
        'class': 'input',
        'autocomplete': 'off'
    }))

    def clean(self):
        cleaned =  super().clean()
        if not Usuarios.objects.filter(username=cleaned['username']).exists():
            raise forms.ValidationError('El usuario no existe')
        else:
            raise forms.ValidationError("Esta accion esta en desarrollo")