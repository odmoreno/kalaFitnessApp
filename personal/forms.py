from django import forms
from django.contrib.auth.models import User
from .models import Personal
from kalaapp.models import Usuario, Rol
from paciente.models import Paciente


class UsuarioForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput, label="Email", required=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'estado_civil' , 'cedula', 'direccion', 'telefono', 'ocupacion', 'genero', 'edad', 'foto']

class UsuarioEditForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput, label="Email", required=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido','estado_civil', 'direccion', 'telefono', 'ocupacion', 'genero', 'edad', 'foto']


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
    ocupacion = forms.ChoiceField(choices=ROLES, required=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'estado_civil', 'cedula', 'direccion', 'telefono', 'genero', 'edad', 'foto']


class ComentarioForm(forms.Form):
    CHOICES=Paciente.objects.all()
    Destino = forms.ChoiceField(choices=((x.usuario, x.usuario.nombre +" "+ x.usuario.apellido) for x in CHOICES))
    mensaje = forms.CharField(widget=forms.Textarea)

class PersonalEditForm(forms.ModelForm):
    ROLES=(
        (1, "Fisioterapista"),
        (2, "Nutricionista"),
    )
    email = forms.EmailField(widget=forms.EmailInput, label="Email")
    ocupacion = forms.ChoiceField(choices=ROLES, required=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'direccion','estado_civil', 'telefono', 'genero', 'edad', 'foto']

