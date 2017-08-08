from django import forms
from django.contrib.auth.models import User
from .models import Personal
from kalaapp.models import Usuario, Rol
from paciente.models import Paciente
'''

Formulario para la creacion de un nuevo Usuario
*Se definen los campos que seran visualizados y se definen reglas especiales para ciertos campos

'''

class UsuarioForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput, label="Email", required=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'cedula', 'email', 'estado_civil', 'direccion', 'telefono', 'ocupacion',
                  'genero', 'edad', 'foto']
        CHOICES=(
            ('M', 'Masculino'),
            ('F', 'Femenino'),
            ('O', 'Otro')
        )
        widgets = {
            'edad': forms.NumberInput(attrs={'min': '0', 'max': '100'}),
            'genero': forms.Select(choices=CHOICES)
        }
'''

Formulario para la Edicion de un Usuario

'''
class UsuarioEditForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput, label="Email", required=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'cedula', 'email', 'estado_civil', 'direccion', 'telefono', 'ocupacion',
                  'genero', 'edad', 'foto']
        CHOICES = (
            ('M', 'Masculino'),
            ('F', 'Femenino'),
            ('O', 'Otro')
        )
        widgets = {
            'edad': forms.NumberInput(attrs={'min': '0', 'max': '100'}),
            'genero': forms.Select(choices=CHOICES)
        }
'''

Formulario para la creacion de un nuevo User
*Se definen los campos que seran visualizados y se definen reglas especiales para ciertos campos

'''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget= forms.EmailField)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

'''

Formulario para la creacion de un nuevo Personal
*Se definen los campos que seran visualizados y se definen reglas especiales para ciertos campos

'''
class PersonalForm(forms.ModelForm):
    ROLES=(
        (1, "Fisioterapista"),
        (2, "Nutricionista"),
    )
    email = forms.EmailField(widget=forms.EmailInput, label="Email")
    ocupacion = forms.ChoiceField(choices=ROLES, required=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'cedula', 'email', 'estado_civil', 'direccion', 'telefono', 'ocupacion',
                  'genero', 'edad', 'foto']
        CHOICES = (
            ('M', 'Masculino'),
            ('F', 'Femenino'),
            ('O', 'Otro')
        )
        widgets = {
            'edad': forms.NumberInput(attrs={'min': '0', 'max': '100'}),
            'genero': forms.Select(choices=CHOICES)
        }
'''

Formulario para la creacion de un Mensaje


'''
class ComentarioForm(forms.Form):
    CHOICES = Paciente.objects.all()
    C=[]
    for p in CHOICES:
        if p.usuario.estado !="I":
            C.append(p)
    Destino = forms.ChoiceField(choices=((x.usuario.id, x.usuario.nombre +" "+ x.usuario.apellido) for x in C))
    mensaje = forms.CharField(widget=forms.Textarea)
'''

Formulario para la creacion de un nuevo Mensaje


'''
class ComentarioPersonalForm(forms.Form):
    CHOICES = Personal.objects.all()
    C=[]
    for p in CHOICES:
        if p.usuario.estado !="I":
            C.append(p)

    Destino = forms.ChoiceField(choices=((x.usuario.id, x.usuario.nombre +" "+ x.usuario.apellido) for x in C))
    mensaje = forms.CharField(widget=forms.Textarea)
'''

Formulario para la Edicion de un Personal


'''
class PersonalEditForm(forms.ModelForm):
    ROLES=(
        (1, "Fisioterapista"),
        (2, "Nutricionista"),
    )
    email = forms.EmailField(widget=forms.EmailInput, label="Email")
    ocupacion = forms.ChoiceField(choices=ROLES, required=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'cedula', 'email', 'estado_civil', 'direccion', 'telefono', 'ocupacion',
                  'genero', 'edad', 'foto']
        CHOICES = (
            ('M', 'Masculino'),
            ('F', 'Femenino'),
            ('O', 'Otro')
        )
        widgets = {
            'edad': forms.NumberInput(attrs={'min': '0', 'max': '100'}),
            'genero': forms.Select(choices=CHOICES)
        }
