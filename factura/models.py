# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from kalaapp.models import Empresa
from paciente.models import Paciente

# Create your models here.

class Facturas(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    #factura_estado = models.ForeignKey('FacturasEstados', models.DO_NOTHING)
    serie = models.CharField(max_length=200)
    fecha_vencimiento = models.DateField()
    subtotal = models.FloatField()
    total = models.FloatField()
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        #managed = False
        db_table = 'facturas'
