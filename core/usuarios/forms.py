from django.forms import ModelForm
from django import forms

from core.usuarios.models import Usuarios

class UsuariosForm(ModelForm):
	class Meta:
		model = Usuarios
		fields = '__all__'
		exclude = ['groups','user_permissions', 'last_login', 'date_joined', 'is_active', 'is_staff']

		widgets = {
			'first_name':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Ingrese su nombre',
					'autocomplete': 'off'
				}),
			'last_name':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Ingrese su nombre',
					'autocomplete': 'off'
				}),
			'username':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Ingrese su nombre',
					'autocomplete': 'off'
				}),
			'imagen':forms.FileInput(
				attrs={
					'class':"input is-success",
					'autocomplete': 'off',
					'autofocus': 'on'
				}),
			'password':forms.PasswordInput(render_value=True,
				attrs={
					'class': 'input is-normal',
					'placeholder': 'Ingrese su contraseña',
					'autocomplete': 'off'
				}),
			'email':forms.EmailInput(
				attrs={
					'class':"input is-normal ml-1",
					'placeholder': 'Correo electrónico',
					'autocomplete': 'off'
				}),
			'is_staff': forms.CheckboxInput(),
			
		}


	def save(self,*args, **kwargs):
		form =super()
		if form.is_valid():
			passw = self.cleaned_data['password']
			a = form.save(commit = False)
			if a.pk is None:
				a.set_password(passw)
			else:
				user = Usuarios.objects.get(pk=a.pk)
				if user.password != passw:
					a.set_password(passw)
			a.save()
		return super().save(*args, **kwargs)

class UsuariosPerfilForm(ModelForm):
	class Meta:
		model = Usuarios
		fields = 'username', 'first_name', 'last_name', 'imagen', 'email', 'sexo', 'miembro'
		exclude = ['groups','user_permissions', 'last_login', 'date_joined', 'is_superuser','is_active', 'is_staff', 'password']

		widgets = {
			'first_name':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Ingrese su nombre',
					'autocomplete': 'off'
				}),
			'last_name':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Ingrese su nombre',
					'autocomplete': 'off'
				}),
			'username':forms.TextInput(
				attrs={
					'class': 'input is-normal ml-2',
					'placeholder': 'Ingrese su nombre',
					'autocomplete': 'off'
				}),
			'imagen':forms.FileInput(
				attrs={
					'class':"input is-success",
					'autocomplete': 'off',
					'autofocus': 'on'
				}),
			'email':forms.EmailInput(
				attrs={
					'class':"input is-normal ml-1",
					'placeholder': 'Correo electrónico',
					'autocomplete': 'off'
				}),
		}

	# def save(self,*args, **kwargs):
	# 	form =super()
	# 	if form.is_valid():
	# 		passw = self.cleaned_data['password']
	# 		a = form.save(commit = False)
	# 		if a.pk is None:
	# 			a.set_password(passw)
	# 		else:
	# 			user = Usuarios.objects.get(pk=a.pk)
	# 			if user.password != passw:
	# 				a.set_password(passw)
	# 		a.save()
	# 	return super().save(*args, **kwargs)