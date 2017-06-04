# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render
from paciente.models import Paciente
from kalaapp.models import Usuario, Rol
from django.contrib.auth.models import User 

# Create your views here.
def pacientes(request):
    template = 'paciente/pacientes.html'
    p=Paciente.objects.all()
    data = {
            'pacientes':p,
            
        }
    return render(request, template, data)

@transaction.atomic
def nuevoPaciente(request):
    pass
@transaction.atomic
def modificarPaciente(request,paciente_id):
    pass
@transaction.atomic
def eliminarPaciente(request, paciente_id):
    pass
