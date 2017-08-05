# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from kalaapp.models import TimeModel, models
from django.core.urlresolvers import  reverse
from kalaapp.models import Usuario, TimeModel


class Personal(TimeModel):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, unique=True)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        #managed = False
        db_table = 'personal'
        unique_together = (('id', 'usuario'),)

    def __unicode__(self):
        return str(self.id)
