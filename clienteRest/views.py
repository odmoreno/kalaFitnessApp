# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from kalaapp.models import Usuario
from paciente.models import Paciente, PacientePersonal
from personal.models import Personal
from diagnostico.models import DiagnosticoNutricion, DiagnosticoFisioterapia, Subrutina, PlanNutDiario, Rutina, Dieta
from fisioterapia.models import Ficha, Horario
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.renderers import JSONRenderer
from nutricion.models import ficha_nutricion, HorarioNut
from directmessages.apps import Inbox
from directmessages.models import Message
from .serializers import HorarioFisSerializer, HorarioNutSerializer, RutinaNestedSerializer, DietasNestedSerializer, PacienteSerializer,FichaFisSerializer, FichaNutSerializer, PersonalSerializer, UsuarioSerializer, DiagnosticoNutSerializer, DiagnosticoFisSerializer, RutinaSerializer, SubrutinaSerializer, DietaSerializer, PlanNutDiarioSerializer, MessageSerializer
# Vistas que definiran la funcionalidad del API REST de cliente
# Seguir Las Historias de Usuario de Cliente
# Mi progreso, Mis Mensajes, Enviar Mensajes, Recibir Mensajes, Ver Citas, Separar Citas.
from rest_framework.authtoken.models import Token

from rest_framework.authentication import BasicAuthentication

#AUTH
# http POST http://127.0.0.1:8000/api/api-token-auth/ -- username=carlos password=carlos123
#Devuelve JSON como:
#{
  #  "token": "valorvalorvalor"
#}




# A todos los requerimientos agregarles'Authorization: Token valor-del-token'


class QuietBasicAuthentication(BasicAuthentication):
    # disclaimer: once the user is logged in, this should NOT be used as a
    def authenticate_header(self, request):
        return 'xBasic realm="%s"' % self.www_authenticate_realm

class UsuarioDatos(APIView):

    def get(self, request, token):

        t=get_object_or_404(Token, key=token)
        user=t.user
        usuario=get_object_or_404(Usuario, usuario=user)
        response = UsuarioSerializer(usuario )
        return Response(response.data or None)

class PersonalList(APIView):
    def get(self, request):
        print request.user
        personal=Personal.objects.filter(estado="A")
        usuarios=[]
        for x in personal:
            if x.usuario.estado == "A":
                usuarios.append(x.usuario)
        response=UsuarioSerializer(usuarios, many=True)
        return Response(response.data)

class PersonalAsignadoList(APIView):
    def get(self, request, paciente_us):
        print request.user
        personal = PacientePersonal.objects.filter(personal_estado="A", paciente__usuario__cedula=paciente_us)
        usuarios = []
        for x in personal:
            usuarios.append(x.personal.usuario)
        response = UsuarioSerializer(usuarios, many=True)
        return Response(response.data)

## Estas dos funciones retornan todos los diagnosticos en la base de datos
class DiagnosticoNutList(APIView):

    def get(self, request, paciente_us=None):
        #5555555557
        try:
            paciente = get_object_or_404(Paciente, usuario__cedula=paciente_us)
            diagnosticos = DiagnosticoNutricion.objects.filter(paciente=paciente)
            dieta=[]
            for d in diagnosticos:
                dieta.append(d)
            response2=DietaSerializer(dieta, many=True)
            response = DiagnosticoNutSerializer(diagnosticos, many=True)
            print response2
            print response
            return Response(response.data or None)
        except:
            return Response( {"data":"No es un paciente"})


class DiagnosticoFisList(APIView):

    def get(self, request, paciente_us=None):
        try:
            paciente =get_object_or_404(Paciente, usuario=request.user)
            diagnosticos=DiagnosticoFisioterapia.objects.filter(paciente=paciente)
            response=DiagnosticoFisSerializer(diagnosticos, many=True)
            return Response(response.data or None)

        except:
            return Response({"data": "No es un paciente"})
##############################################################################

#Estas dos funciones retornas respectivamente todas las rutinas o Dietas que han sido asigndas a un paciente
class RutinasList(APIView):
    def get(self, request, paciente_us):
        #try:
        paciente = get_object_or_404(Paciente, usuario__cedula=paciente_us)
        diagnosticos = DiagnosticoFisioterapia.objects.filter(paciente=paciente)
        rutinas=[]
        for x in diagnosticos:
            rut=x.rutina
            for y in rut.subrutina.all():
                rutinas.append(y)
        response=SubrutinaSerializer(rutinas, many=True)
        return Response(response.data or {"mensaje":"No hay rutinas"})

        #except:
        #return Response({"mensaje": "No es un paciente"})
class RutinasNestedList(APIView):
    def get(self, paciente_us):
        paciente = get_object_or_404(Paciente, usuario__cedula=paciente_us)
        diagnosticos = DiagnosticoFisioterapia.objects.filter(paciente=paciente)
        response = RutinaNestedSerializer(diagnosticos, many=True)
        return Response(response.data or None)


class DietasList(APIView):

    def get(self, request, paciente_us):
        try:
            paciente = get_object_or_404(Paciente, usuario__cedula=paciente_us)
            diagnosticos = DiagnosticoNutricion.objects.filter(paciente=paciente)
            dietas=[]
            for x in diagnosticos:
                dieta=x.dieta
                plan=PlanNutDiario.objects.filter(dieta=dieta)
                for y in plan:
                    dietas.append(y)
            response=PlanNutDiarioSerializer(dietas, many=True)
            return Response(response.data or None)
        except:
            return Response({"data": "No es un paciente"})

class DietasNestedList(APIView):

    def get(self, request, paciente_us):
        paciente = get_object_or_404(Paciente, usuario__cedula=paciente_us)
        diagnosticos = DiagnosticoNutricion.objects.filter(paciente=paciente)
        response = DietasNestedSerializer(diagnosticos, many=True)
        return Response(response.data or None)

class FichaFisList (APIView):
    def get(self, request, paciente_us):
        try:
            paciente = get_object_or_404(Paciente, usuario__cedula=paciente_us)
            ficha = Ficha.objects.filter(paciente=paciente)
            fichas=[]
            for x in ficha:
                fichas.append(x)
            response=FichaFisSerializer(fichas, many=True)
            return Response(response.data or None)
        except:
            return Response({"data": "No es un paciente"})
class FichaNutList (APIView):
    def get(self, request, paciente_us):
        try:
            paciente = get_object_or_404(Paciente, usuario__cedula=paciente_us)
            ficha = ficha_nutricion.objects.filter(paciente=paciente)
            fichas=[]
            for x in ficha:
                fichas.append(x)
            response=FichaNutSerializer(fichas, many=True)
            return Response(response.data or None)
        except:
            return Response({"data": "No es un paciente"})

class MensajesList(APIView):

    #Para obtener los mensajes delPaciente
    def get(self, request, paciente_us):
        user=User.objects.filter(username=paciente_us)
        mensajes = Message.objects.filter(recipient=user)
        response=MessageSerializer(mensajes, many=True)
        return Response(response.data or None)

    #Para enviar un mensaje
    def post(self, request, paciente_us):
        pass





class HorariosFisList(APIView):
    def get(self, request):
        citasLibres=Horario.objects.filter(estado="1")
        response=HorarioFisSerializer(citasLibres, many=True)
        return Response(response.data)

    #ENVIAR EN POST ID DE LA CITA A SER SEPARADA Y LA CEDULA DEL PACIENTE

    def post(self, request):
        citaASeparar=Horario.objects.filter(pk=request.POST['citaID'])
        paciente = get_object_or_404(Paciente, usuario__cedula=request.POST['paciente_us'])
        try:
            citaASeparar.paciente=paciente
            citaASeparar.estado="2"
            citaASeparar.save()
            return({"Mensaje":"Cita Guardada!"})
        except:
            return Response({"Mensaje":"Se produjo un error al separa la cita"}, status= 300)

class HorariosNutList(APIView):
    def get(self, request):
        citasLibres=HorarioNut.objects.filter(estado="1")
        response=HorarioNutSerializer(citasLibres, many=True)
        return Response(response.data)

    #ENVIAR EN POST ID DE LA CITA A SER SEPARADA Y LA CEDULA DEL PACIENTE

    def post(self, request):
        citaASeparar=HorarioNut.objects.filter(pk=request.POST['citaID'])
        paciente = get_object_or_404(Paciente, usuario__cedula=request.POST['paciente_us'])
        try:
            citaASeparar.paciente=paciente
            citaASeparar.estado="2"
            citaASeparar.save()
            return({"Mensaje":"Cita Guardada!"})
        except:
            return Response({"Mensaje":"Se produjo un error al separa la cita"}, status= 300)

def autenticar(request):
    mensaje = None

    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
        print request.GET
        print '_username: ' + username
        print '_password: ' + password
        try:
            user = get_object_or_404(User, username=username)
            print 'user_pass: ' + user.password
            print 'user_hash: ' + password

            if user and check_password(password, user.password):
                usuario = get_object_or_404(Usuario, usuario=user)
                usuario = UsuarioSerializer(usuario)
                return JsonResponse({'respuesta': 1, 'usuario': JSONRenderer().render(usuario.data)})
        except Exception, e:
            mensaje = str(e)
    return JsonResponse({'respuesta': 0, 'mensaje': mensaje})

