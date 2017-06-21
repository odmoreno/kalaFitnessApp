from django import forms
from django.contrib.auth.models import User
from .models import Personal
from kalaapp.models import Usuario, Rol


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'cedula', 'direccion', 'telefono', 'ocupacion', 'genero', 'edad', 'foto']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']




