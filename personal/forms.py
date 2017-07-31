from django import forms
from django.contrib.auth.models import User
from .models import Personal
from kalaapp.models import Usuario, Rol


class UsuarioForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput, label="Email", required=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'cedula', 'direccion', 'telefono', 'ocupacion', 'genero', 'edad', 'foto']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget= forms.EmailField)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class PersonalForm(forms.ModelForm):
    ROLES=(
        (1, "Fisioterapista"),
        (2, "Nutricionista"),
    )
    email = forms.EmailField(widget=forms.EmailInput, label="Email")
    ocupacion=forms.ChoiceField(choices=ROLES, required=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'cedula', 'direccion', 'telefono', 'genero', 'edad', 'foto']



