# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from kalaapp.models import Usuario, TimeModel
from personal.models import Personal

# Create your models here.
class Paciente(TimeModel):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, unique=True)
    estado = models.CharField(max_length=1, default='A')


    class Meta:
        #managed = False
        db_table = 'paciente'
        unique_together = (('id', 'usuario'),)


class PacientePersonal(TimeModel):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    #cita = models.ForeignKey(Citas, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        #managed = False
        db_table = 'paciente_personal'
