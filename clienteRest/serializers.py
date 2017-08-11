from django.contrib.auth.models import User
from rest_framework import serializers
from kalaapp.models import Usuario
from paciente.models import Paciente
from personal.models import Personal
from diagnostico.models import DiagnosticoNutricion, DiagnosticoFisioterapia, Subrutina, PlanNutDiario, Rutina, Dieta
from fisioterapia.models import Ficha
from nutricion.models import ficha_nutricion

## Serializers para los modelos que usaremos en la API
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
##Modelos de Usuario, paciente y Personal
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'cedula', 'usuario')

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('usuario', 'estado')

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ('usuario', 'estado', )


##########################################################
#        Serializadores de fichas y diagnosticos         #
##########################################################
class FichaFisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = '__all__'

class FichaNutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ficha_nutricion
        fields = '__all__'

class DiagnosticoNutSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticoNutricion
        fields = '__all__'

class DiagnosticoFisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticoFisioterapia
        fields = '__all__'

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = '__all__'

class DietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dieta
        fields = '__all__'

class SubrutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subrutina
        fields = '__all__'


class PlanNutDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanNutDiario


