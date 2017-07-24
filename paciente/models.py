# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from kalaapp.models import Usuario, TimeModel
from personal.models import Personal

# Create your models here.
class Paciente(TimeModel):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, unique=True)
    n_hijos = models.PositiveSmallIntegerField(default=0, null=False)
    observaciones = models.CharField(max_length=200, default='', null=False);
    motivo_consulta = models.CharField(max_length=200, default='', null=False)
    estado = models.CharField(max_length=1, default='A')


    class Meta:
        #managed = False
        db_table = 'paciente'
        unique_together = (('id', 'usuario'),)

    def __unicode__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.usuario.nombre, self.usuario.apellido,
                                          self.n_hijos, self.observaciones, self.motivo_consulta)



class PacientePersonal(TimeModel):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        #managed = False
        db_table = 'paciente_personal'

    def __unicode__(self):
        return 'PacientePersonalID: {} --> PersonalID: {}, PacienteID: {}'.format(self.id, self.personal_id,
                                                                                 self.paciente_id)