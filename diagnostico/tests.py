# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Diagnostico, Rutina, Subrutina
from personal.models import Personal
from paciente.models import Paciente
from kalaapp.models import Rol, Usuario
from django.contrib.auth.models import User


# Create your tests here.

class verificarCreacionDiagnosticoTestCase(TestCase):

    def setUp(self):
        user = User()
        user.username=''
        user.save()

        usuario = Usuario(usuario=user)
        usuario.nombre = "Christian"
        usuario.apellido = "Jaramillo"

        rol = Rol.objects.create(tipo='personal')
        rol.save()

        usuario.rol = rol
        usuario.cedula = '0999999999'
        usuario.save()

        personal = Personal(usuario=usuario)
        personal.save()

        user2 = User()
        user2.username = 'c'
        user2.save()

        usuario = Usuario(usuario=user2)
        usuario.nombre = "Carola"
        usuario.apellido = "Toledo"
        rol = Rol.objects.create(tipo='paciente')
        rol.save()

        usuario.rol = rol
        usuario.cedula = '0999999998'
        usuario.save()

        paciente = Paciente(usuario=usuario)
        paciente.save()

    def testCrearDiagnostico(self):
        diagnostico = Diagnostico()
        diagnostico.personal = Personal.objects.get(usuario__nombre='Christian', usuario__apellido='Jaramillo')
        diagnostico.paciente = Paciente.objects.get(usuario__nombre='Carola', usuario__apellido='Toledo')
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"
        diagnostico.receta = "Realizar ejercicios para mejorar rodilla por 30 min"

        rutina = Rutina()
        rutina.save()

        diagnostico.rutina = rutina

        subrutina = Subrutina(nombre="Ejercicios isométricos de los músculos cuádriceps",
                              detalle="Con la pierna recta, apriete los músculos del muslo lo más que pueda y manténgalo durante 3-5 segundos. Después relájese y vuelva a repetirlo. Si tiene dificultad puede ponerse una toalla enrollada debajo de la rodilla para aumentar la sensación.",
                              veces=5, repeticiones=4, link = "https://www.youtube.com/watch?v=mlucy2Pz1Fc")
        subrutina.save()
        diagnostico.rutina.subrutina.add(subrutina)

        diagnostico.save()

        diagnostico_recuperado = Diagnostico.objects.filter(id=diagnostico.id).first()

        self.assertEquals(diagnostico_recuperado, diagnostico, 'Error diagnosticos no coinciden!')
        self.assertEquals(diagnostico_recuperado.personal, diagnostico.personal, 'Error personal asignado no coincide!')
        self.assertEquals(diagnostico_recuperado.paciente, diagnostico.paciente, 'Error paciente asignado no coincide!')
        self.assertEquals(diagnostico_recuperado.condiciones_previas, "Ninguna", 'Error mensaje no coincide!')


class verificarEdicionDiagnosticoTestCase(TestCase):

    def setUp(self):
        user = User()
        user.username=''
        user.save()

        usuario = Usuario(usuario=user)
        usuario.nombre = "Christian"
        usuario.apellido = "Jaramillo"

        rol = Rol.objects.create(tipo='personal')
        rol.save()

        usuario.rol = rol
        usuario.cedula = '0999999999'
        usuario.save()

        personal = Personal(usuario=usuario)
        personal.save()

        user2 = User()
        user2.username = 'c'
        user2.save()

        usuario = Usuario(usuario=user2)
        usuario.nombre = "Carola"
        usuario.apellido = "Toledo"
        rol = Rol.objects.create(tipo='paciente')
        rol.save()

        usuario.rol = rol
        usuario.cedula = '0999999998'
        usuario.save()

        paciente = Paciente(usuario=usuario)
        paciente.save()

    def testEditarDiagnostico(self):
        diagnostico = Diagnostico()
        diagnostico.personal = Personal.objects.get(usuario__nombre='Christian', usuario__apellido='Jaramillo')
        diagnostico.paciente = Paciente.objects.get(usuario__nombre='Carola', usuario__apellido='Toledo')
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"

        rutina = Rutina()
        rutina.save()

        diagnostico.rutina = rutina

        subrutina = Subrutina(nombre="Ejercicios isométricos de los músculos cuádriceps",
                              detalle="Con la pierna recta, apriete los músculos del muslo lo más que pueda y manténgalo durante 3-5 segundos. Después relájese y vuelva a repetirlo. Si tiene dificultad puede ponerse una toalla enrollada debajo de la rodilla para aumentar la sensación.",
                              veces=5, repeticiones=4, link="https://www.youtube.com/watch?v=mlucy2Pz1Fc")
        subrutina.save()
        diagnostico.rutina.subrutina.add(subrutina)

        diagnostico.save()

        diagnostico_recuperado = Diagnostico.objects.get(id=diagnostico.id)
        diagnostico_recuperado.area_afectada = "Brazo izquierdo"
        diagnostico_recuperado.save()

        self.assertEquals(diagnostico_recuperado.id, diagnostico.id, 'Error diagnosticos no coinciden!')
        self.assertEquals(diagnostico.area_afectada, 'Rodilla derecha', 'Area afectada no coincide!')
        self.assertEquals(diagnostico_recuperado.area_afectada, 'Brazo izquierdo', 'Area afectada no coincide!')


class verificarEliminacionDiagnosticoTestCase(TestCase):

    def setUp(self):
        user = User()
        user.username=''
        user.save()

        usuario = Usuario(usuario=user)
        usuario.nombre = "Christian"
        usuario.apellido = "Jaramillo"

        rol = Rol.objects.create(tipo='personal')
        rol.save()

        usuario.rol = rol
        usuario.cedula = '0999999999'
        usuario.save()

        personal = Personal(usuario=usuario)
        personal.save()

        user2 = User()
        user2.username = 'c'
        user2.save()

        usuario = Usuario(usuario=user2)
        usuario.nombre = "Carola"
        usuario.apellido = "Toledo"
        rol = Rol.objects.create(tipo='paciente')
        rol.save()

        usuario.rol = rol
        usuario.cedula = '0999999998'
        usuario.save()

        paciente = Paciente(usuario=usuario)
        paciente.save()

    def testEliminarDiagnostico(self):
        diagnostico = Diagnostico()
        diagnostico.personal = Personal.objects.get(usuario__nombre='Christian', usuario__apellido='Jaramillo')
        diagnostico.paciente = Paciente.objects.get(usuario__nombre='Carola', usuario__apellido='Toledo')
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"
        diagnostico.receta = "Paracetamol 1440 diarias cada minuto"
        rutina = Rutina()
        rutina.save()

        diagnostico.rutina = rutina

        subrutina = Subrutina(nombre="Ejercicios isométricos de los músculos cuádriceps",
                              detalle="Con la pierna recta, apriete los músculos del muslo lo más que pueda y manténgalo durante 3-5 segundos. Después relájese y vuelva a repetirlo. Si tiene dificultad puede ponerse una toalla enrollada debajo de la rodilla para aumentar la sensación.",
                              veces=5, repeticiones=4, link="https://www.youtube.com/watch?v=mlucy2Pz1Fc")
        subrutina.save()
        diagnostico.rutina.subrutina.add(subrutina)

        diagnostico.save()

        diagnostico_recuperado = Diagnostico.objects.get(id=diagnostico.id)
        diagnostico_recuperado.delete()

        try:
            diagnostico_recuperado_f = Diagnostico.objects.get(id=diagnostico_recuperado.id)
        except Diagnostico.DoesNotExist:
            diagnostico_recuperado_f = None

        self.assertEquals(diagnostico_recuperado_f, None, 'Error diagnostico existe!')
