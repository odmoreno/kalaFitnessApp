# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from kalaapp.models import TimeModel
from personal.models import Personal
from paciente.models import Paciente
#from django.utils.timezone import  now
from django.utils import timezone
import datetime

FRECUENCIA = (
    ('diario', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('semanal', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('rara_vez', 'raraVez'),
    ('nunca', 'nunca'),
)

TIPO =(('diario', 'Diario'),
        ('semanal', 'Semanal'),
        ('raravez', 'Rara vez'),
       ('nunca', 'Nunca'))

VECES= (('1', '4-5 veces'),
        ('2', '2-3 veces'),
        ('3', '1 vez'),
        ('4', 'Rara vez'),
        ('5', 'Nunca'))

ESTADO = (('1', 'No tomada'),
          ('2', 'Finalizada'))

class ficha_nutricion(TimeModel):
    personal = models.ForeignKey(Personal, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)

    #Frecuencia de consumo
    lacteos = models.CharField(max_length=200, choices=TIPO, default='diario', null=False)
    vegetales = models.CharField(max_length=200, choices=TIPO, default='semanal', null=False)
    frutas = models.CharField(max_length=200, choices=TIPO, default='diario', null=False)
    cho = models.CharField(max_length=200, choices=TIPO, default='diario', null=False)
    carnes = models.CharField(max_length=200, choices=TIPO, default='diario', null=False)
    comidas_rapidas = models.CharField(max_length=200, choices=TIPO, default='diario', null=False)
    frituras = models.CharField(max_length=200, choices=TIPO, default='diario', null=False)
    enlatados = models.CharField(max_length=200, choices=TIPO, default='diario', null=False)
    gaseosas = models.CharField(max_length=200, choices=TIPO, default='diario', null=False)
    energizantes = models.CharField(max_length=200, choices=TIPO, default='diario', null=False)
    infusiones = models.CharField(max_length=200, choices=TIPO, default='diario', null=False)

    lacteos_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)
    vegetales_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)
    frutas_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)
    cho_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)
    carnes_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)
    comidas_rapidas_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)
    frituras_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)
    enlatados_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)
    gaseosas_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)
    energizantes_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)
    infusiones_input = models.CharField(max_length=20,choices=VECES, default='3', null=False)

    #Anamnesis alimentaria
    pregunta1= models.CharField(max_length=100, null=False)
    pregunta2 = models.CharField(max_length=100, null=False)
    pregunta3 = models.CharField(max_length=100, null=False)
    pregunta4 = models.CharField(max_length=100, null=False)
    pregunta5 = models.CharField(max_length=100, null=False)
    pregunta6 = models.CharField(max_length=100, null=False)

    #Requerimientos
    proteina = models.PositiveSmallIntegerField(null=False)
    grasas = models.PositiveSmallIntegerField(null=False)
    carbohidratos = models.PositiveSmallIntegerField(null=False)
    dieta = models.CharField(max_length=100, null=False)


    class Meta:
        #managed = False
        db_table = 'ficha_nutricion'

class HorarioNut(TimeModel):
    personal = models.ForeignKey(Personal, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING, null=True, blank=True)

    fecha = models.DateField(auto_now=False)
    hora = models.TimeField(auto_now=False)
    detalle = models.CharField(max_length=200, null=False)
    estado = models.CharField(max_length=200, choices=ESTADO, default='1', null=False)

    class Meta:
        db_table = 'horario_nut'