# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from kalaapp.models import Usuario
from paciente.models import Paciente, PacientePersonal
from personal.models import Personal
from diagnostico.models import DiagnosticoNutricion, DiagnosticoFisioterapia, Subrutina, PlanNutDiario, Rutina, Dieta
from fisioterapia.models import Ficha

from nutricion.models import ficha_nutricion
from .serializers import PacienteSerializer,FichaFisSerializer, FichaNutSerializer, PersonalSerializer, UsuarioSerializer, DiagnosticoNutSerializer, DiagnosticoFisSerializer, RutinaSerializer, SubrutinaSerializer, DietaSerializer, PlanNutDiarioSerializer
# Vistas que definiran la funcionalidad del API REST de cliente
# Seguir Las Historias de Usuario de Cliente
# Mi progreso, Mis Mensajes, Enviar Mensajes, Recibir Mensajes, Ver Citas, Separar Citas.

from rest_framework.authentication import BasicAuthentication


class QuietBasicAuthentication(BasicAuthentication):
    # disclaimer: once the user is logged in, this should NOT be used as a
    def authenticate_header(self, request):
        return 'xBasic realm="%s"' % self.www_authenticate_realm


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
    def get(self, request):
        pass
    #Para enviar un mensaje
    def post(self, request):
        pass





class HorariosList(APIView):
    def get(self, request):
        pass
    def post(self, request, pacienteID, citaID):
        pass



# def verMensajes(requets):
#     pass
#
# def nuevoMensaje(requets):
#     pass
#
# def miProgreso(request):
#     pass
#
# def citasDisponibles(request):
#     pass
#
# def separarCita(request):
#     pass
#
