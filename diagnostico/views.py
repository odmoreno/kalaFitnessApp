'''
MODULO DIAGNOSTICO FISIOTERAPISTA Y NUTRICIONISTA

VERSION 2.0.0

ACTUALIZADO EN 15/07/2017

'''

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseForbidden
from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from diagnostico.models import DiagnosticoFisioterapia, DiagnosticoNutricion, Dieta, PlanNutDiario
from kalaapp.views import paginar
from paciente.models import Paciente
from personal.models import Personal
from .models import Rutina, Subrutina, DIAS
from kalaapp.decorators import rol_required

# Create your views here.


'''
Funcion: listarDiagnosticos
Entradas: request
Salidas: - HttpResponse con template diagnostico_listar.ntml y la lista de todos los diagnosticos

Funcion que permite listar los diagnosticos existentes
'''


@login_required
@rol_required(roles=['fisioterapista', 'nutricionista'])
def listarDiagnosticos(request):
    template = 'diagnostico_listar.html'
    contexto = {}
    diagnosticos = None
    pacientes = None
    rol = None

    sesion = request.session.get('user_sesion', None)

    if sesion:
        rol = sesion.get('rol__tipo', None)

    if rol == 'fisioterapista':
        diagnosticos = DiagnosticoFisioterapia.objects.filter(estado='A').order_by('-creado') \
            .annotate(paciente_nombre_completo=Concat('paciente__usuario__apellido', \
                                                      Value(' '), 'paciente__usuario__nombre')) \
            .annotate(paciente_id=Concat('paciente_id', Value('')))
    elif rol == 'nutricionista':
        diagnosticos = DiagnosticoNutricion.objects.filter(estado='A').order_by('-creado') \
            .annotate(paciente_nombre_completo=Concat('paciente__usuario__apellido', \
                                                      Value(' '), 'paciente__usuario__nombre')) \
            .annotate(paciente_id=Concat('paciente_id', Value('')))

    contexto['diagnosticos_paginator'] = paginar(request, diagnosticos)
    contexto['user_sesion'] = sesion

    return render(request, template_name=template, context=contexto)


'''
Funcion: crearDiagnostico
Entradas: request
Salidas: - HttpResponse con template crear.ntml y la lista de todas los pacientes

Funcion que permite crear un nuevo diagnostico
'''


@login_required
@rol_required(roles=['fisioterapista', 'nutricionista', 'administrador'])
@transaction.atomic
def crearDiagnostico(request):
    template = None
    contexto = {}
    pacientes = None
    rol = None

    sesion = request.session.get('user_sesion', None)

    if sesion:
        rol = sesion.get('rol__tipo', '')

    if request.method == 'POST':
        diagnostico = getDiagnostico(request)

        if diagnostico is not None:
            messages.add_message(request, messages.SUCCESS, 'Diagnostico creado con exito!')
        else:
            messages.add_message(request, messages.WARNING, 'Error inesperado creando diagnostico!')
        return redirect('diagnostico:ListarDiagnosticos')

    try:
        pacientes = Paciente.objects.filter(estado='A', pacientepersonal__personal_id=sesion.get('personal__id', 0))\
            .values('id', 'usuario__nombre', 'usuario__apellido') \
            .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
            .order_by('nombre_completo')
        if pacientes is not None and pacientes.count() == 0:
            raise Exception
    except Exception, e:
        messages.add_message(request, messages.WARNING, 'No tiene pacientes asignados, consulte con su administrador! ')

    contexto['pacientes'] = pacientes

    if rol == 'fisioterapista':
        template = 'diagnostico_crear.html'
    elif rol == 'nutricionista':
        template = 'diagnostico_nut_crear.html'
        contexto['dias'] = DIAS
    else:
        return redirect(to='/')

    return render(request, template_name=template, context=contexto)

'''
Funcion: getDiagnostico
Entradas: - request
Salidas:  - nueva diagnostico

Funcion que retorna un nuevo diagnostico con los datos ingresados en formulario
'''


@transaction.atomic
def getDiagnostico(request):
    diagnostico = None
    sesion = request.session.get('user_sesion', None)
    rol = None

    if sesion:
        rol = sesion.get('rol__tipo', None)

    if rol is not None:
        try:
            if rol == 'fisioterapista':
                diagnostico = DiagnosticoFisioterapia()
                diagnostico.area_afectada = request.POST.get('areaafectada', '')
                diagnostico.receta = request.POST.get('receta', '')
                #falta obtener rutinas
                s = Subrutina.objects.create(nombre="caminata", detalle="caminata x 60 minutos", veces=2, repeticiones=1, descanso=45, link='http://google.ec')
                diagnostico.rutina = Rutina.objects.create()
                diagnostico.rutina.subrutina.add(s)
            elif rol == 'nutricionista':
                diagnostico = DiagnosticoNutricion()

                dieta = Dieta()
                dieta.descripcion = request.POST.get('dietadescripcion', '')
                dieta.save()
                diagnostico.dieta = dieta

                for key, dia in DIAS:
                    plan_diario = PlanNutDiario(dia=dia,
                                                desayuno=request.POST.get(dia+'_Desayuno', ''),
                                                colacion1=request.POST.get(dia+'_Colacion1', ''),
                                                almuerzo=request.POST.get(dia+'_Almuerzo', ''),
                                                colacion2=request.POST.get(dia+'_Colacion2', ''),
                                                cena=request.POST.get(dia+'_Cena', ''),
                                                dieta=dieta)
                    plan_diario.save()

            diagnostico.personal = Personal.objects.get(estado='A', id=sesion.get('personal__id', 0))
            diagnostico.paciente = Paciente.objects.get(estado='A', id=request.POST.get('paciente', 0))
            diagnostico.condiciones_previas = request.POST.get('condicionesprevias', '')
            diagnostico.save()
        except Exception, e:
            return None
    return diagnostico

'''
Funcion: crearDiagnostico
Entradas: - request
          - id: id del diagnostico a eliminar
Salidas: ninguna

Funcion que permite eliminar un diagnostico existente
'''


@login_required
@rol_required(roles=['fisioterapista', 'nutricionista'])
@transaction.atomic
def eliminarDiagnostico(request, id=0):
    contexto = {}
    diagnosticoEliminado = None
    sesion = request.session.get('user_sesion', None)

    if sesion:
        rol = sesion.get('rol__tipo', None)

    if request.method == 'POST':
        try:
            if rol == 'fisioterapista':
                diagnosticoEliminado = DiagnosticoFisioterapia.objects.get(estado='A', id=id)
                #Falta inactivar rutinas
            elif rol == 'nutricionista':
                diagnosticoEliminado = DiagnosticoNutricion.objects.get(estado='A', id=id)
                diagnosticoEliminado.dieta.estado = 'I'
                diagnosticoEliminado.dieta.save()

                for plan_diario in PlanNutDiario.objects.filter(estado='A', dieta=diagnosticoEliminado.dieta):
                    plan_diario.estado = 'I'
                    plan_diario.save()

            if diagnosticoEliminado and diagnosticoEliminado.estado == 'A':
                diagnosticoEliminado.estado = 'I'
                diagnosticoEliminado.save()
                messages.add_message(request, messages.SUCCESS, 'Diagnostico eliminado con exito!')
            else:
                messages.add_message(request, messages.WARNING, 'Diagnostico no encontrado o ya eliminado')
        except:
            messages.add_message(request, messages.WARNING, 'Error inesperado!')

    return redirect('diagnostico:ListarDiagnosticos')

'''
Funcion: editarDiagnostico
Entradas: - request
          - id: id del diagnostico a editar
Salidas: ninguna

Funcion que permite editar un diagnostico existente
'''


@login_required
@rol_required(roles=['fisioterapista', 'nutricionista'])
def editarDiagnostico(request, id=0):
    contexto = {}
    template = None
    diagnostico = None
    pacientes = None
    sesion = request.session.get('user_sesion', None)
    rol = None

    if sesion:
        rol = sesion.get('rol__tipo', None)

    if request.method == 'POST':
        try:
            if rol == 'fisioterapista':
                diagnostico = DiagnosticoFisioterapia.objects.get(estado='A', id=id)
                template = 'diagnostico_editar.html'
            elif rol == 'nutricionista':
                diagnostico = DiagnosticoNutricion.objects.get(estado='A', id=id)
                template = 'diagnostico_nut_editar.html'
                dias = {'One': 'Lunes', 'Two': 'Martes', 'Three': 'Miercoles',
                        'Four': 'Jueves', 'Five': 'Viernes', 'Six': 'Sabado'}
                planes_diarios = PlanNutDiario.objects.filter(estado='A', dieta=diagnostico.dieta).order_by('id')
                contexto['planes_diarios'] = planes_diarios
        except:
            messages.add_message(request, messages.WARNING, 'Error inesperado consultando diagnostico!')

        try:
            pacientes = Paciente.objects.filter(estado='A', pacientepersonal__personal_id=sesion.get('personal__id', 0)) \
                .values('id', 'usuario__nombre', 'usuario__apellido') \
                .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
                .order_by('nombre_completo')
        except Exception, e:
            messages.add_message(request, messages.WARNING, 'Error inesperado consultando pacientes! ' + str(e))

        contexto['diagnostico'] = diagnostico
        contexto['pacientes'] = pacientes

    return render(request, template_name=template, context=contexto)

'''
Funcion: guardarDiagnostico
Entradas: - request
Salidas: ninguna

Funcion que persiste un Diagnostico en base
'''


@transaction.atomic
def guardarDiagnostico(request):
    diagnostico = None
    sesion = request.session.get('user_sesion', None)
    rol = None

    if sesion:
        rol = sesion.get('rol__tipo', None)

    if rol and request.method == 'POST':
        try:
            if rol == 'fisioterapia':
                diagnostico = DiagnosticoFisioterapia.objects.get(estado='A', id=request.POST.get('diagnostico_id', 0))
                diagnostico.condiciones_previas = request.POST.get('condicionesprevias', '')
                diagnostico.area_afectada = request.POST.get('areaafectada', '')
                diagnostico.receta = request.POST.get('receta', '')
                #Falta guardar rutina editada

            elif rol == 'nutricionista':
                diagnostico = DiagnosticoNutricion.objects.get(estado='A',
                                                               id=request.POST.get('diagnostico_id', 0))
                diagnostico.condiciones_previas = request.POST.get('condicionesprevias', '')
                diagnostico.dieta.descripcion = request.POST.get('dietadescripcion', '')
                diagnostico.dieta.save()

                for key, dia in DIAS:
                    plan_diario = PlanNutDiario.objects.get(estado='A', dia=dia, dieta=diagnostico.dieta)
                    plan_diario.desayuno = request.POST.get(dia + '_Desayuno', '')
                    plan_diario.colacion1 = request.POST.get(dia + '_Colacion1', '')
                    plan_diario.almuerzo = request.POST.get(dia + '_Almuerzo', '')
                    plan_diario.colacion2 = request.POST.get(dia + '_Colacion2', '')
                    plan_diario.cena = request.POST.get(dia + '_Cena', '')
                    plan_diario.save()

            if diagnostico:
                diagnostico.save()
                messages.add_message(request, messages.SUCCESS, 'Diagnostico actualizado satisfactoriamente!')
            else:
                raise Exception
        except Exception, e:
            messages.add_message(request, messages.WARNING, 'Error inesperado al actualizar diagnostico!')

    return redirect('diagnostico:ListarDiagnosticos')

