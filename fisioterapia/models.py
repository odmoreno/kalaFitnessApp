# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from time import timezone

from django.db import models
from kalaapp.models import TimeModel
from personal.models import Personal
from paciente.models import Paciente
#from django.utils.timezone import  now
from django.utils import timezone
# Create your models here.

TIPO =(('alta', 'alta'),
        ('media', 'media'),
        ('baja', 'baja'))

class EstadoFisico(TimeModel):
    personal = models.ForeignKey(Personal, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    flexiones = models.PositiveSmallIntegerField(default=1, null=False)
    sentadillas = models.PositiveSmallIntegerField(default=1, null=False)
    saltoLargo = models.PositiveSmallIntegerField(default=1, null=False)
    suspension = models.CharField(max_length=200, choices= TIPO, default='baja', null=False)
    abdomen_bajo = models.PositiveSmallIntegerField(default=1, null=False)
    abdomen_alto = models.PositiveSmallIntegerField(default=1, null=False)
    espinales = models.PositiveSmallIntegerField(default=1, null=False)
    lumbares = models.PositiveSmallIntegerField(default=1, null=False)
    trenSuperior = models.TimeField(auto_now_add=True, blank=True)
    trenInferior = models.TimeField(auto_now_add=True, blank=True)
    #duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        #managed = False
        db_table = 'estadofisico'
        unique_together = (('id', 'personal'),)

class Ficha(TimeModel):
    personal = models.ForeignKey(Personal, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    fecha = models.DateField(default=timezone.now, blank=False, null=False)
    altura = models.FloatField(default=1.0, null=False)
    peso = models.FloatField(default=1.0, null=False)
    imc = models.FloatField(default=1.0, null=False)
    musculo = models.FloatField(default=1.0, null=False)
    grasa_visceral = models.FloatField(default=1.0, null=False)
    grasa_porcentaje = models.FloatField(default=1.0, null=False)
    cuello = models.FloatField(default=1.0, null=False)
    hombros = models.FloatField(default=1.0, null=False)
    pecho = models.FloatField(default=1.0, null=False)
    brazo_derecho = models.FloatField(default=1.0, null=False)
    brazo_izquierdo = models.FloatField(default=1.0, null=False)
    antebrazo_derecho = models.FloatField(default=1.0, null=False)
    antebrazo_izquierdo = models.FloatField(default=1.0, null=False)
    cintura = models.FloatField(default=1.0, null=False)
    cadera = models.FloatField(default=1.0, null=False)
    muslo_derecho = models.FloatField(default=1.0, null=False)
    muslo_izquierdo = models.FloatField(default=1.0, null=False)
    pantorrilla_derecha = models.FloatField(default=1.0, null=False)
    pantorrilla_izquierda = models.FloatField(default=1.0, null=False)

    class Meta:
        #managed = False
        db_table = 'ficha'
        unique_together = (('id', 'personal'),)