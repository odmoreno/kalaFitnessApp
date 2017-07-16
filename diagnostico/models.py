# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from kalaapp.models import TimeModel
# Create your models here.


class Diagnostico(TimeModel):
    personal = models.ForeignKey('Personal')
    usuario = models.ForeignKey('Pacientes')
    fecha = models.DateField(auto_now_add=True, null=False)
    altura = models.FloatField(default=0, null=False)
    peso = models.FloatField(default=0, null=False)
    imc = models.FloatField(default=0, null=False)
    musculo = models.FloatField(default=0, null=False)
    grasa_visceral = models.FloatField(default=0, null=False)
    grasa_procentaje = models.FloatField(default=0, null=False)
    cuello = models.FloatField(default=0, null=False)
    hombros = models.FloatField(default=0, null=False)
    pecho = models.FloatField(default=0, null=False)
    brazo_derecho = models.FloatField(default=0, null=False)
    brazo_izquierdo = models.FloatField(default=0, null=False)
    antebrazo_derecho = models.FloatField(default=0, null=False)
    antebrazo_izquierdo = models.FloatField(default=0, null=False)
    cintura = models.FloatField(default=0, null=False)
    cadera = models.FloatField(default=0, null=False)
    muslo_derecho = models.FloatField(default=0, null=False)
    muslo_izquierdo = models.FloatField(default=0, null=False)
    pantorrilla_derecha = models.FloatField(default=0, null=False)
    pantorrilla_izquierda = models.FloatField(default=0, null=False)
    flexiones = models.PositiveSmallIntegerField(default=0, null=False)
    cadera_arriba = models.PositiveSmallIntegerField(default=0, null=False)
    abdomen = models.PositiveSmallIntegerField(default=0, null=False)
    espinales = models.PositiveSmallIntegerField(default=0, null=False)
    lumbares = models.PositiveSmallIntegerField(default=0, null=False)
    sentadillas = models.PositiveSmallIntegerField(default=0, null=False)
    condiciones_previas = models.CharField(max_length=200, default='', null=False);
    oarea_afectada = models.CharField(max_length=200, default='', null=False);
    receta = models.CharField(max_length=200, default='', null=False);
    rutina = models.CharField(max_length=200, default='', null=False);
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        #managed = False
        db_table = 'diagnostico'

