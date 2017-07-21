# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from kalaapp.models import Empresa
from paciente.models import Paciente
from kalaapp.models import TimeModel
from django.utils import timezone

# Create your models here.

class Facturas(TimeModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    serie = models.CharField(max_length=25, unique=True, default='', null=False)
    fecha_vencimiento = models.DateField(default=timezone.now, null=False)
    total = models.FloatField(default=0, null=False)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        #managed = False
        db_table = 'facturas'
