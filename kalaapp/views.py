# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render
from django.http import Http404, HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from paciente.models import Paciente, PacientePersonal
from personal.models import Personal
from .models import Usuario
from django.contrib.auth.models import User
from .decorators import rol_required

# Create your views here.


@login_required
def home(request):
    template = 'landing.html'
    contexto = {}
    
    request.session.set_expiry(10800)
    user_sesion = request.session.get('user_sesion', None)

    if not user_sesion:
        try:
            user = User.objects.get(username=request.user.username)

            if user is not None:
                if user.is_superuser:

                    request.session['user_sesion'] = {'id': user.id,
                                                      'nombre': user.first_name if user.first_name != '' else 'N.',
                                                      'apellido': user.last_name if user.last_name != '' else 'N.',
                                                      'cedula': user.username,
                                                      'rol__tipo': 'administrador',
                                                      'personal__id': 0}
                else:
                    request.session['user_sesion'] = Usuario.objects.filter(cedula=request.user.username)\
                                    .values('id', 'nombre', 'apellido', 'cedula', 'rol__tipo', 'personal__id', 'paciente__id')\
                                    .first()
        except User.DoesNotExist, e:
            return HttpResponse(str(e))
        except Exception, e2:
            return HttpResponse(str(e2))
    if request.session['user_sesion']:
        return render(request=request, template_name=template, context=contexto)
    else:
        return Http404("Error inesperado!")


@login_required
def index2(request):
    template = 'landing.html'
    data = {}
    return render(request, template, data)


'''
Funcion: asignarPersonalaPaciente
Entradas: request
Salidas: - HttpResponse con template asignar.ntml y la lista de todas personal y pacientes

Funcion que crear las asignaciones y/o eliminarlas
'''


@login_required
@rol_required(roles=['administrador'])
@transaction.atomic
def asignarPersonalaPaciente(request):
    template = 'kalaapp_asignar.html'
    contexto = {}
    pacientes = None
    personal = None
    personal_id_actual = 0

    if request.method == 'POST':
        try:
            personal = Personal.objects.get(id=request.POST.get('personal_id', 0))
            pacientes_id = request.POST.getlist('paciente_seleccionado' or None)

            # Si la asignación con otro personal existe o esta siendo desasignada entonces eliminarla
            try:
                asigDiferentePersonal = PacientePersonal.objects.filter(estado='A', paciente__in=pacientes_id) \
                    .exclude(personal=personal)
                eliminarAsignaciones(asigDiferentePersonal)

                asigMismoPersonal = PacientePersonal.objects.filter(estado='A', personal=personal) \
                    .exclude(paciente__in=pacientes_id)
                eliminarAsignaciones(asigMismoPersonal)

            except PacientePersonal.DoesNotExist:
                messages.add_message(request, messages.WARNING, 'No existen asignaciones a eliminar!, ' + str(e))

            # Si la asignación no existe entonces crearla
            veces = 0
            for pid in pacientes_id:

                try:
                    paciente = Paciente.objects.get(id=pid)
                    pp = PacientePersonal.objects.get(estado='A', personal=personal, paciente=paciente)
                    print '5 ' + pp
                except PacientePersonal.DoesNotExist, e:
                    pp = PacientePersonal.objects.create(personal=personal, paciente=paciente)
                    print '6 ' + pp
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
        personal = Personal.objects.filter(estado='A', usuario__estado='A') \
            .values('id', 'usuario__nombre', 'usuario__apellido', 'usuario__cedula', 'usuario__rol__tipo') \
            .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
            .order_by('id', 'nombre_completo')

        pacientes = Paciente.objects.filter(estado='A', usuario__estado='A') \
            .values('id', 'pacientepersonal__personal_id', 'usuario__nombre', 'usuario__apellido', 'usuario__cedula',
                    'usuario__telefono', 'usuario__ocupacion', 'usuario__edad', 'usuario__genero', 'usuario__foto') \
            .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
            .order_by('id', 'nombre_completo')

    except Exception, e:
        messages.add_message(request, messages.WARNING, 'Error inesperado al consultar informacion!, ' + str(e))

    contexto['pacientes'] = pacientes
    contexto['personal'] = personal
    contexto['personal_id_actual'] = int(personal_id_actual)
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

Funcion que permite paginar objetos existentes
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
