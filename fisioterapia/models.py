# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from time import timezone

from django.db import models
from kalaapp.models import TimeModel
from personal.models import Personal
from paciente.models import Paciente
#from django.utils.timezone import  now
from django.utils import timezone
import datetime
# Create your models here.

TIPO =(('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'))

ESTADO = (('1', 'No tomada'),
          ('2', 'Finalizada'))

class Ficha(TimeModel):
    personal = models.ForeignKey(Personal, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)

    #estado = models.OneToOneField('EstadoFisico', on_delete=models.CASCADE, unique=True)
    #fecha = models.DateField(default=timezone.now, blank=False, null=False)
    altura = models.FloatField(null=True)
    peso = models.FloatField(null=True)
    imc = models.FloatField(null=True)
    musculo = models.FloatField(null=True)
    grasa_visceral = models.FloatField(null=True)
    grasa_porcentaje = models.FloatField(null=True)
    cuello = models.FloatField(null=True)
    hombros = models.FloatField(null=True)
    pecho = models.FloatField(null=True)
    brazo_derecho = models.FloatField(null=True)
    brazo_izquierdo = models.FloatField(null=True)
    antebrazo_derecho = models.FloatField(null=True)
    antebrazo_izquierdo = models.FloatField(null=True)
    cintura = models.FloatField(null=True)
    cadera = models.FloatField(null=True)
    muslo_derecho = models.FloatField(null=True)
    muslo_izquierdo = models.FloatField(null=True)
    pantorrilla_derecha = models.FloatField(null=True)
    pantorrilla_izquierda = models.FloatField(null=True)

    # duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    flexiones = models.PositiveSmallIntegerField(default=1, null=False)
    sentadillas = models.PositiveSmallIntegerField(default=1, null=False)
    saltoLargo = models.PositiveSmallIntegerField(default=1, null=False)
    suspension = models.CharField(max_length=200, choices=TIPO, default='baja', null=False)
    abdomen_bajo = models.PositiveSmallIntegerField(default=1, null=False)
    abdomen_alto = models.PositiveSmallIntegerField(default=1, null=False)
    espinales = models.PositiveSmallIntegerField(default=1, null=False)
    lumbares = models.PositiveSmallIntegerField(default=1, null=False)
    trenSuperior = models.TimeField(blank=True, default=datetime.time(00, 00))
    trenInferior = models.TimeField( blank=True, default=datetime.time(00,00))

    class Meta:
        #managed = False
        db_table = 'ficha'

class Horario(TimeModel):
    personal = models.ForeignKey(Personal, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING, null=True, blank=True)

    fecha = models.DateField(auto_now=False)
    hora = models.TimeField(auto_now=False, default= datetime.datetime.utcnow)
    detalle = models.CharField(max_length=200, null=False)
    estado = models.CharField(max_length=200, choices=ESTADO, default='1', null=False)

    class Meta:
        db_table = 'horario_fis'