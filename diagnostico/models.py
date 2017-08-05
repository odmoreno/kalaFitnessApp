# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from kalaapp.models import TimeModel, Usuario
from personal.models import Personal
from paciente.models import Paciente
# Create your models here.


class DiagnosticoFisioterapia(TimeModel):
    personal = models.ForeignKey(Personal, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    condiciones_previas = models.CharField(max_length=1000, default='', null=False)
    area_afectada = models.CharField(max_length=1000, default='', null=False)
    receta = models.CharField(max_length=1000, default='', null=False)
    rutina = models.OneToOneField('Rutina', on_delete=models.CASCADE, unique=True)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        db_table = 'diagnostico_fis'

    def __unicode__(self):
        return str(self.id)


class DiagnosticoNutricion(TimeModel):
    personal = models.ForeignKey(Personal, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    condiciones_previas = models.CharField(max_length=1000, default='', null=False)
    dieta = models.OneToOneField('Dieta', on_delete=models.CASCADE, unique=True)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        db_table = 'diagnostico_nut'


class Rutina(TimeModel):
    subrutina = models.ManyToManyField('Subrutina')
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        db_table = 'rutina'


class Subrutina(TimeModel):
    nombre = models.CharField(max_length=1000, default='', null=False)
    detalle = models.CharField(max_length=1000, default='', null=False)
    veces = models.PositiveSmallIntegerField(default=0, null=False)           #50 veces
    repeticiones = models.PositiveSmallIntegerField(default=0, null=False)    #por 3 repeticiones
    descanso = models.PositiveSmallIntegerField(default=0, null=False)        #3 minutos entre cada repeticion
    link = models.URLField(max_length=500, default='', null=False)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        #managed = False
        db_table = 'subrutina'


class Dieta(TimeModel):
    descripcion = models.CharField(max_length=1000, default='', null=False)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        db_table = 'dieta'

DIAS = ((1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'),
        (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'))


class PlanNutDiario(TimeModel):
    dieta = models.ForeignKey('Dieta', on_delete=models.CASCADE, default='')
    dia = models.CharField(max_length=30, choices=DIAS, default='Lunes', null=False)
    desayuno = models.CharField(max_length=1000, default='', null=False)
    colacion1 = models.CharField(max_length=1000, default='', null=False)
    almuerzo = models.CharField(max_length=1000, default='', null=False)
    colacion2 = models.CharField(max_length=1000, default='', null=False)
    cena = models.CharField(max_length=1000, default='', null=False)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        db_table = 'plan_nut_diario'