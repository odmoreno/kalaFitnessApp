# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from kalaapp.models import Usuario, TimeModel


class Personal(models.Model):
    usuario = models.OneToOneField(Usuario, unique=True)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        #managed = False
        db_table = 'personal'
        unique_together = (('id', 'usuario'),)


# class PersonalPlanificaciones(models.Model):
#     planificacion = models.ForeignKey('Planificaciones', models.DO_NOTHING)
#     personal = models.ForeignKey(Personal, models.DO_NOTHING)
#     detalle = models.CharField(max_length=200)
#     oficina = models.CharField(max_length=200)
#     estado = models.CharField(max_length=1)
#     creado = models.DateTimeField()
#     actualizado = models.DateTimeField()
#
#     class Meta:
#         #managed = False
#         db_table = 'personal_planificaciones'
