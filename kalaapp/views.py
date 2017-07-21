# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.db.models.functions import Concat
from django.db.models import Value
from django.db import transaction
from django.urls.base import reverse
from paciente.models import Paciente
from personal.models import Personal


# Create your views here.
@login_required
def index2(request):
    template = 'kalaapp/landing.html'
    data = {}
    return render(request, template, data)

def asignarPersonalaPaciente(request):
    template = 'kalaapp_asignar.html'
    contexto = {}
    pacientes = None
    personal = None

    if request.method == 'POST':
        pass

    try:
        pacientes = Paciente.objects.filter(estado='A') \
            .values('id', 'usuario__nombre', 'usuario__apellido', 'usuario__cedula', 'usuario__telefono',
                    'usuario__ocupacion', 'usuario__edad', 'usuario__genero', 'usuario__foto') \
            .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
            .order_by('id', 'nombre_completo')
        personal = Paciente.objects.filter(estado='A') \
            .values('id', 'usuario__nombre', 'usuario__apellido', 'usuario__cedula') \
            .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
            .order_by('id', 'nombre_completo')
        print pacientes.count(), personal.count()
    except Exception, e:
        print str(e)

    contexto['pacientes'] = pacientes
    contexto['personal'] = personal

    return render(request, template_name=template, context=contexto)