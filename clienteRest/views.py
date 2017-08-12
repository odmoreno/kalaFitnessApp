# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from kalaapp.models import Usuario
from paciente.models import Paciente
from personal.models import Personal
from diagnostico.models import DiagnosticoNutricion, DiagnosticoFisioterapia, Subrutina, PlanNutDiario, Rutina, Dieta
from fisioterapia.models import Ficha
from nutricion.models import ficha_nutricion
from .serializers import PacienteSerializer, PersonalSerializer, UsuarioSerializer, DiagnosticoNutSerializer, DiagnosticoFisSerializer, RutinaSerializer, SubrutinaSerializer, DietaSerializer, PlanNutDiarioSerializer
# Vistas que definiran la funcionalidad del API REST de cliente
# Seguir Las Historias de Usuario de Cliente
# Mi progreso, Mis Mensajes, Enviar Mensajes, Recibir Mensajes, Ver Citas, Separar Citas.
class PersonalList(APIView):

    def get(self, request):
        personal=Personal.objects.all()
        usuarios=[]
        for x in personal:
            usuarios.append(x.usuario)
        response=UsuarioSerializer(usuarios, many=True)
        return Response(response.data)

    def post(self, request):
        pass

class DiagnosticoNutList(APIView):
    def get(self, request, pacienteid=None):
        paciente = get_object_or_404(Paciente, usuario=request.user)
        diagnosticos = DiagnosticoNutricion.objects.filter(paciente=paciente)
        response = DiagnosticoNutSerializer(diagnosticos, many=True)
        return Response(response.data or None)


class DiagnosticoFisList(APIView):
    def get(self, request, pacienteid=None):
        paciente =get_object_or_404(Paciente, usuario=request.user)
        diagnosticos=DiagnosticoFisioterapia.objects.filter(paciente=paciente)
        response=DiagnosticoFisSerializer(diagnosticos, many=True)
        return Response(response.data or None)


class RutinasList(APIView):
    def get(self, request):
        paciente = get_object_or_404(Paciente, usuario=request.user)
        diagnosticos = DiagnosticoFisioterapia.objects.filter(paciente=paciente)
        rutinas=[]
        for x in diagnosticos:
            rut=x.rutina
            for y in rut.subrutina:
                rutinas.append(y)
        response=SubrutinaSerializer(rutinas, many=True)
        return Response(response.data or None)

class DietasList(APIView):
    def get(self, request):
        paciente = get_object_or_404(Paciente, usuario=request.user)
        diagnosticos = DiagnosticoNutricion.objects.filter(paciente=paciente)
        dietas=[]
        for x in diagnosticos:
            dieta=x
            plan=PlanNutDiario.objects.filter(dieta=dieta)
            for y in plan:
                dietas.append(y)
        response=PlanNutDiarioSerializer(dietas, many=True)
        return Response(response.data or None)


class MensajesList(APIView):

    def get(self, request):
        pass



def verMensajes(requets):
    pass

def nuevoMensaje(requets):
    pass

def miProgreso(request):
    pass

def citasDisponibles(request):
    pass

def separarCita(request):
    pass

