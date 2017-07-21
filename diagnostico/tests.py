# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Diagnostico,Rutina,Subrutina
from personal.models import Personal
from paciente.models import Paciente


# Create your tests here.

class verificarCreacionDiagnosticoTestCase(TestCase):
    personal_recuperado = None
    paciente_recuperado = None

    def setUp(self):
        personal = Personal.objects.create(usuario__nombre='christian', usuario__apellido='jaramillo')
        paciente = Paciente.objects.create(usuario__nombre='carola', usuario__apellido='toledo')

        personal_recuperado = Personal.objects.get(id=personal.id)
        paciente_recuperado = Paciente.objects.get(id=paciente.id)


    def crearDiagnostico(self):
        diagnostico = Diagnostico()
        rutina = Rutina()
        subRutina = Subrutina()
        # diagnostico.personal = Personal.objects.filter(usuario__nombre='christian', usuario__apellido='jaramillo').first()
        # diagnostico.paciente = Paciente.objects.filter(usuario__nombre='carola', usuario__apellido='toledo').first()
        diagnostico.personal = personal_recuperado
        diagnostico.paciente = paciente_recuperado
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"
        diagnostico.rutina = "Realizar ejercicios para mejorar rodilla por 30 min"
        subRutina.nombre = "Ejercicios isométricos de los músculos cuádriceps"
        subRutina.detalle = "Con la pierna recta, apriete los músculos del muslo lo más que pueda y manténgalo durante 3-5 segundos. Después relájese y vuelva a repetirlo. Si tiene dificultad puede ponerse una toalla enrollada debajo de la rodilla para aumentar la sensación."
        subRutina.veces = 5
        subRutina.repeticiones = 4
        subRutina.link = "https://www.youtube.com/watch?v=mlucy2Pz1Fc"
        diagnostico.receta = None
        diagnostico.save()

        diagnostico_recuperado = Diagnostico.objects.filter(id=diagnostico.id).first()

        self.assertEquals(diagnostico_recuperado, diagnostico, 'Error diagnosticos no coinciden!')
        self.assertEquals(diagnostico_recuperado.personal, diagnostico.personal, 'Error personal asignado no coincide!')
        self.assertEquals(diagnostico_recuperado.paciente, diagnostico.paciente, 'Error paciente asignado no coincide!')
        self.assertEquals(diagnostico_recuperado.condiciones_previas, "Ninguna", 'Error mensaje no coincide!')


class verificarEdicionDiagnosticoTestCase(TestCase):
    personal_recuperado = None
    paciente_recuperado = None

    def setUp(self):
        personal = Personal.objects.create(usuario__nombre='christian', usuario__apellido='jaramillo')
        paciente = Paciente.objects.create(usuario__nombre='carola', usuario__apellido='toledo')

        personal_recuperado = Personal.objects.get(id=personal.id)
        paciente_recuperado = Paciente.objects.get(id=paciente.id)

    def editarDiagnostico(self):
        diagnostico = Diagnostico()
        diagnostico.personal = Personal.objects.filter(usuario__nombre='christian',
                                                       usuario__apellido='jaramillo').first()
        diagnostico.paciente = Paciente.objects.filter(usuario__nombre='carola', usuario__apellido='toledo').first()
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"
        diagnostico.rutina = None
        diagnostico.receta = "Paracetamol 1440 diarias cada minuto"
        diagnostico.save()

        diagnostico_recuperado = Diagnostico.objects.get(id=diagnostico.id)
        diagnostico_recuperado.save()

        self.assertEquals(diagnostico_recuperado.id, diagnostico.id, 'Error diagnosticos no coinciden!')
        self.assertEquals(diagnostico_recuperado.condiciones_previas, 'Ninguna', 'Error paciente asignado no coincide!')


class verificarEliminacionDiagnosticoTestCase(TestCase):
    personal_recuperado = None
    paciente_recuperado = None

    def setUp(self):
        personal = Personal.objects.create(usuario__nombre='christian', usuario__apellido='jaramillo')
        paciente = Paciente.objects.create(usuario__nombre='carola', usuario__apellido='toledo')

        personal_recuperado = Personal.objects.get(id=personal.id)
        paciente_recuperado = Paciente.objects.get(id=paciente.id)

    def eliminarDiagnostico(self):
        diagnostico = Diagnostico()
        subRutina = Subrutina()
        diagnostico.personal = Personal.objects.filter(usuario__nombre='christian',
                                                       usuario__apellido='jaramillo').first()
        diagnostico.paciente = Paciente.objects.filter(usuario__nombre='carola', usuario__apellido='toledo').first()
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"
        diagnostico.rutina = "Realizar ejercicios para mejorar rodilla por 30 min"
        subRutina.nombre = "Ejercicios isométricos de los músculos cuádriceps"
        subRutina.detalle = "Con la pierna recta, apriete los músculos del muslo lo más que pueda y manténgalo durante 3-5 segundos. Después relájese y vuelva a repetirlo. Si tiene dificultad puede ponerse una toalla enrollada debajo de la rodilla para aumentar la sensación."
        subRutina.veces = 5
        subRutina.repeticiones = 4
        subRutina.link = "https://www.youtube.com/watch?v=mlucy2Pz1Fc"
        diagnostico.receta = "Paracetamol 1440 diarias cada minuto"
        diagnostico.save()

        diagnostico_recuperado = Diagnostico.objects.get(id=diagnostico.id)
        diagnostico_recuperado.delete()
        diagnostico_recuperado_f = None

        try:
            diagnostico_recuperado_f = Diagnostico.objects.get(id=diagnostico_recuperado.id)
        except Diagnostico.DoesNotExist:
            pass

        self.assertEquals(diagnostico_recuperado, None, 'Error diagnostico existe!')
