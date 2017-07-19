# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Diagnostico
from personal.models import Personal
from paciente.models import Paciente

# Create your tests here.

class verificarCreacionDiagnosticoTestCase(TestCase):
    def setUp(self):

        personal = Personal.objects.create(usuario__nombre='christian', usuario__apellido='jaramillo')
        paciente = Paciente.objects.create(usuario__nombre='carola', usuario__apellido='toledo')

        personal_recuperado = Personal.objects.get(id = personal.id)
        paciente_recuperado = Paciente.objects.get(id = paciente.id)

        self.assertEqual(personal_recuperado, personal, 'Error personal no coincide!')
        self.assertEqual(paciente_recuperado, paciente, 'Error paciente no coincide!')

    def crearDiagnostico(self):
        diagnostico = Diagnostico()
        diagnostico.personal = Personal.objects.filter(usuario__nombre='christian', usuario__apellido='jaramillo').first()
        diagnostico.paciente = Paciente.objects.filter(usuario__nombre='carola', usuario__apellido='toledo').first()
        diagnostico.altura = 178
        diagnostico.peso = 200
        diagnostico.imc = 1.2
        diagnostico.musculo = 7
        diagnostico.grasa_visceral = 10
        diagnostico.grasa_porcentaje = 28.5
        diagnostico.cuello = 10
        diagnostico.hombros = 12
        diagnostico.pecho = 1.1
        diagnostico.brazo_derecho = 35.5
        diagnostico.brazo_izquierdo = 35.5
        diagnostico.antebrazo_derecho = 21
        diagnostico.antebrazo_izquierdo = 21.0
        diagnostico.cintura = 60
        diagnostico.cadera = 65.55
        diagnostico.musloderecho = 90
        diagnostico.musloizquierdo = 90.0
        diagnostico.pantorrilla_derecha = 24
        diagnostico.pantorrilla_izquierda = 24
        diagnostico.flexiones = 55
        diagnostico.cadera_arriba = 60
        diagnostico.abdomen = 60
        diagnostico.espinales = 40
        diagnostico.lumbares = 25
        diagnostico.sentadillas = 100
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"
        diagnostico.rutina = "Caminata en piscina por 30 minutos diarios"
        diagnostico.receta = "Paracetamol 1440 diarias cada minuto"
        diagnostico.save()

        diagnostico_recuperado = Diagnostico.objects.filter(id=diagnostico.id).first()

        self.assertEqual(diagnostico_recuperado, diagnostico, 'Error diagnosticos no coinciden!')
        self.assertEqual(diagnostico_recuperado.personal, diagnostico.personal, 'Error personal asignado no coincide!')
        self.assertEqual(diagnostico_recuperado.paciente, diagnostico.paciente, 'Error paciente asignado no coincide!')
        self.assertEqual(diagnostico_recuperado.condiciones_previas, "Ninguna", 'Error mensaje no coincide!')


class verificarEdicionDiagnosticoTestCase(TestCase):
    def setUp(self):
        personal = Personal.objects.create(usuario__nombre='christian', usuario__apellido='jaramillo')
        paciente = Paciente.objects.create(usuario__nombre='carola', usuario__apellido='toledo')

        personal_recuperado = Personal.objects.get(id=personal.id)
        paciente_recuperado = Paciente.objects.get(id=paciente.id)

        self.assertEqual(personal_recuperado, personal, 'Error personal no coincide!')
        self.assertEqual(paciente_recuperado, paciente, 'Error paciente no coincide!')

    def editarDiagnostico(self):
        diagnostico = Diagnostico()
        diagnostico.personal = Personal.objects.filter(usuario__nombre='christian',
                                                       usuario__apellido='jaramillo').first()
        diagnostico.paciente = Paciente.objects.filter(usuario__nombre='carola', usuario__apellido='toledo').first()
        diagnostico.altura = 178
        diagnostico.peso = 200
        diagnostico.imc = 1.2
        diagnostico.musculo = 7
        diagnostico.grasa_visceral = 10
        diagnostico.grasa_porcentaje = 28.5
        diagnostico.cuello = 10
        diagnostico.hombros = 12
        diagnostico.pecho = 1.1
        diagnostico.brazo_derecho = 35.5
        diagnostico.brazo_izquierdo = 35.5
        diagnostico.antebrazo_derecho = 21
        diagnostico.antebrazo_izquierdo = 21.0
        diagnostico.cintura = 60
        diagnostico.cadera = 65.55
        diagnostico.musloderecho = 90
        diagnostico.musloizquierdo = 90.0
        diagnostico.pantorrilla_derecha = 24
        diagnostico.pantorrilla_izquierda = 24
        diagnostico.flexiones = 55
        diagnostico.cadera_arriba = 60
        diagnostico.abdomen = 60
        diagnostico.espinales = 40
        diagnostico.lumbares = 25
        diagnostico.sentadillas = 100
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"
        diagnostico.rutina = "Caminata en piscina por 30 minutos diarios"
        diagnostico.receta = "Paracetamol 1440 diarias cada minuto"
        diagnostico.save()

        diagnostico_recuperado = Diagnostico.objects.get(id=diagnostico.id)
        diagnostico_recuperado.altura = 185
        diagnostico_recuperado.save()

        self.assertEqual(diagnostico_recuperado.id, diagnostico.id, 'Error diagnosticos no coinciden!')
        self.assertNotEqual(diagnostico_recuperado.altura, diagnostico.altura, 'Error variables coinciden!')
        self.assertEqual(diagnostico_recuperado.altura, 185, 'Error paciente asignado no coincide!')


class verificarEliminacionDiagnosticoTestCase(TestCase):
    def setUp(self):
        personal = Personal.objects.create(usuario__nombre='christian', usuario__apellido='jaramillo')
        paciente = Paciente.objects.create(usuario__nombre='carola', usuario__apellido='toledo')

        personal_recuperado = Personal.objects.get(id=personal.id)
        paciente_recuperado = Paciente.objects.get(id=paciente.id)

        self.assertEqual(personal_recuperado, personal, 'Error personal no coincide!')
        self.assertEqual(paciente_recuperado, paciente, 'Error paciente no coincide!')

    def eliminarDiagnostico(self):
        diagnostico = Diagnostico()
        diagnostico.personal = Personal.objects.filter(usuario__nombre='christian',
                                                       usuario__apellido='jaramillo').first()
        diagnostico.paciente = Paciente.objects.filter(usuario__nombre='carola', usuario__apellido='toledo').first()
        diagnostico.altura = 178
        diagnostico.peso = 200
        diagnostico.imc = 1.2
        diagnostico.musculo = 7
        diagnostico.grasa_visceral = 10
        diagnostico.grasa_porcentaje = 28.5
        diagnostico.cuello = 10
        diagnostico.hombros = 12
        diagnostico.pecho = 1.1
        diagnostico.brazo_derecho = 35.5
        diagnostico.brazo_izquierdo = 35.5
        diagnostico.antebrazo_derecho = 21
        diagnostico.antebrazo_izquierdo = 21.0
        diagnostico.cintura = 60
        diagnostico.cadera = 65.55
        diagnostico.musloderecho = 90
        diagnostico.musloizquierdo = 90.0
        diagnostico.pantorrilla_derecha = 24
        diagnostico.pantorrilla_izquierda = 24
        diagnostico.flexiones = 55
        diagnostico.cadera_arriba = 60
        diagnostico.abdomen = 60
        diagnostico.espinales = 40
        diagnostico.lumbares = 25
        diagnostico.sentadillas = 100
        diagnostico.condiciones_previas = "Ninguna"
        diagnostico.area_afectada = "Rodilla derecha"
        diagnostico.rutina = "Caminata en piscina por 30 minutos diarios"
        diagnostico.receta = "Paracetamol 1440 diarias cada minuto"
        diagnostico.save()

        diagnostico_recuperado = Diagnostico.objects.get(id=diagnostico.id)
        diagnostico_recuperado.delete()
        diagnostico_recuperado_f = Diagnostico.objects.get(id=diagnostico_recuperado.id)

        self.assertIsNone(diagnostico_recuperado_f, 'Error diagnostico existe!')
