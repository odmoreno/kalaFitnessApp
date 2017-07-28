# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render

from paciente.models import Paciente, PacientePersonal
from personal.models import Personal
from .models import Usuario


# Create your views here.
@login_required
def home(request):
    template = 'landing.html'
    contexto = {}

    #request.session.set_expiry(60*30)
    user_sesion = request.session.get('user_sesion', None)
    print user_sesion
    try:
        if not user_sesion:
            user_sesion = Usuario.objects.filter(cedula=request.user.username).\
                values('id', 'nombre', 'apellido', 'cedula', 'rol__tipo', 'personal__id').first()
            request.session['user_sesion'] = user_sesion
        contexto['user_sesion'] = user_sesion
    except Exception, e:
        print "error --> " + str(e)

    return render(request, template, context=contexto)

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


'''
Funcion: paginar
Entradas: request, lista de objectos
Salidas: - lista de objetos paginados

Funcion que permite listar los diagnosticos existentes
'''
def paginar(request, objetos):
    if objetos is not None and objetos.count() > 0:
        objetos_por_pagina = 10
        objetos_paginator = None

        pag = request.GET.get('pag', 1)
        paginator = Paginator(objetos, objetos_por_pagina)

        try:
            objetos_paginator = paginator.page(pag)
        except PageNotAnInteger:
            objetos_paginator = paginator.page(1)
        except EmptyPage:
            objetos_paginator = paginator.page(paginator.num_pages)

        return objetos_paginator