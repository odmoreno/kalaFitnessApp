from django.contrib.auth.models import User
from rest_framework import serializers
from kalaapp.models import Usuario
from paciente.models import Paciente
from personal.models import Personal
from diagnostico.models import DiagnosticoNutricion, DiagnosticoFisioterapia, Subrutina, PlanNutDiario, Rutina, Dieta
from fisioterapia.models import Ficha, Horario
from directmessages.models import Message
from nutricion.models import ficha_nutricion, HorarioNut

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

class RutinaNestedSerializer(serializers.ModelSerializer):
    subrutina=serializers.SerializerMethodField('obtenerRutinas')
    def obtenerRutinas(self, diagnosticos):
        rutinas = []
        for y in diagnosticos.rutina.subrutina.all():
            rutinas.append(y)
        response = SubrutinaSerializer(rutinas, many=True)
        return response.data
    class Meta:
        model = DiagnosticoFisioterapia
        fields = ('id','condiciones_previas','subrutina')


class PlanNutDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanNutDiario
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class PlanNutDiarioNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanNutDiario
        fields = ('dia','desayuno','almuerzo','cena')

class DietasNestedSerializer(serializers.ModelSerializer):
    plan_diario = serializers.SerializerMethodField('obtenerDietas')

    def obtenerDietas(self, dieta):
        plan = PlanNutDiario.objects.filter(dieta=dieta.dieta)
        response = PlanNutDiarioSerializer(plan, many=True)
        return response.data
    class Meta:
        model=DiagnosticoNutricion
        fields=('id','condiciones_previas','plan_diario')

class HorarioFisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields=('personal','fecha','hora','detalle','estado','id')
class HorarioNutSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioNut
        fields=('personal','fecha','hora','detalle','estado','id')




