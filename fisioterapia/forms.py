from django import forms
from paciente.models import Paciente
from kalaapp.models import Usuario, Rol
from django.contrib.auth.models import User


class ComentarioForm(forms.Form):
     Destino= forms.ModelMultipleChoiceField(queryset=Paciente.objects.all())
     comentario = forms.CharField(widget=forms.Textarea)