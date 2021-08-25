from django import forms

from .models import  Pregunta, ElegirRespuesta, PreguntasRespondidas

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, get_user_model

#Powered by Nemo with help from Google
User = get_user_model()

class ElegirInlineFormset(forms.BaseInlineFormSet):
	def clean(self):
		super(ElegirInlineFormset, self).clean()

		respuesta_correcta = 0
		for formulario in self.forms:
			if not formulario.is_valid():
				return

			if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
				respuesta_correcta += 1

		try:
			assert respuesta_correcta == Pregunta.NUMER_DE_RESPUESTAS_PERMITIDAS
		except AssertionError:
			raise forms.ValidationError('Exactamente una sola respuesta es permitida')
#Powered by Nemo with help from Google

class UsuarioLoginFormulario(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Este usuario No existe")
			if not user.check_password(password):
				raise forms.ValidationError("Contraseña incorrecta")
			if not user.is_active:
				raise forms.ValidationError("Este Usuario No está activo")

		return super(UsuarioLoginFormulario, self).clean(*args, **kwargs)

#Powered by Nemo with help from Google

class RegistroFormulario(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)

	class Meta:
		model = User 

		fields = [

			'first_name',
			'last_name',
			'username',
			'email',
			'password1',
			'password2'

		]

#Powered by Nemo with help from Google
