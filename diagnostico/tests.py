# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Diagnostico
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
        # diagnostico.personal = Personal.objects.filter(usuario__nombre='christian', usuario__apellido='jaramillo').first()
        # diagnostico.paciente = Paciente.objects.filter(usuario__nombre='carola', usuario__apellido='toledo').first()
        diagnostico.personal = personal_recuperado
        diagnostico.paciente = paciente_recuperado
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"
        diagnostico.rutina = "Caminata en piscina por 30 minutos diarios"
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
        diagnostico.personal = Personal.objects.filter(usuario__nombre='christian',
                                                       usuario__apellido='jaramillo').first()
        diagnostico.paciente = Paciente.objects.filter(usuario__nombre='carola', usuario__apellido='toledo').first()
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"
        diagnostico.rutina = "Caminata en piscina por 30 minutos diarios"
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
