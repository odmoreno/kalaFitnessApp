# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.db.models.functions import Concat
from django.db.models import Value
from django.db import transaction
from django.urls.base import reverse
from paciente.models import Paciente, PacientePersonal
from personal.models import Personal
from django.contrib import messages


# Create your views here.
@login_required
def index2(request):
    template = 'kalaapp/landing.html'
    data = {}
    return render(request, template, data)

'''
Funcion: asignarPersonalaPaciente
Entradas: request
Salidas: - HttpResponse con template asignar.ntml y la lista de todas personal y pacientes

Funcion que crear las asignaciones y/o eliminarlas
'''

@transaction.atomic
def asignarPersonalaPaciente(request):
    template = 'kalaapp_asignar.html'
    contexto = {}
    pacientes = None
    personal = None

    if request.method == 'POST':
        try:
            personal = Personal.objects.get(id = request.POST.get('personal_id', 0))
            pacientes_id = request.POST.getlist('paciente_seleccionado' or None)

            # Si la asignación con otro personal existe o esta siendo desasignada entonces eliminarla
            try:
                asigDiferentePersonal = PacientePersonal.objects.filter(estado='A', paciente__in = pacientes_id)\
                                                                        .exclude(personal = personal)
                eliminarAsignaciones(asigDiferentePersonal)

                asigMismoPersonal = PacientePersonal.objects.filter(estado='A', personal = personal)\
                                                                    .exclude(paciente__in = pacientes_id)
                eliminarAsignaciones(asigMismoPersonal)

            except PacientePersonal.DoesNotExist:
                messages.add_message(request, messages.WARNING, 'No existen asignaciones a eliminar!, ' + str(e))

            # Si la asignación no existe entonces crearla
            veces = 0
            for pid in pacientes_id:

                try:
                    paciente = Paciente.objects.get(id = pid)
                    pp = PacientePersonal.objects.get(estado = 'A', personal = personal, paciente = paciente)
                except PacientePersonal.DoesNotExist, e:
                    pp = PacientePersonal.objects.create(personal = personal, paciente = paciente)
                    veces = veces + 1

            if veces > 0:
                if veces == 1:
                    msg = '1 asignacion creada con exito!'
                else:
                    msg = str(veces) + ' asignaciones creadas con exito!'
                messages.add_message(request, messages.WARNING, msg)

        except Exception, e:
            messages.add_message(request, messages.WARNING, 'Error inesperado al crear asignacion!, ' + str(e))

    try:
        personal = Personal.objects.filter(estado='A') \
            .values('id', 'usuario__nombre', 'usuario__apellido', 'usuario__cedula') \
            .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
            .order_by('id', 'nombre_completo')

        pacientes = Paciente.objects.filter(estado='A') \
            .values('id', 'pacientepersonal__personal_id', 'usuario__nombre', 'usuario__apellido', 'usuario__cedula', 'usuario__telefono',
                   'usuario__ocupacion', 'usuario__edad', 'usuario__genero', 'usuario__foto') \
            .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
            .order_by('id', 'nombre_completo')

    except Exception, e:
        messages.add_message(request, messages.WARNING, 'Error inesperado al consultar informacion!, ' + str(e))

    contexto['pacientes'] = pacientes
    contexto['personal'] = personal

    return render(request, template_name=template, context=contexto)

'''
Funcion: eliminarAsignaciones
Entradas: lista de asignaciones a eliminar
Salidas: Ninguna

Funcion que permite eliminar las asignaciones enviadas como parametro
'''
def eliminarAsignaciones(asignaciones):
    if asignaciones is not None and asignaciones.count() > 0:
        for pp in asignaciones:
            try:
                pp.delete()
            except Exception, e:
                messages.add_message(request, messages.WARNING, 'Error inesperado al eliminar asignaciones!, ' + str(e))