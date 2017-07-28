'''
MODULO DIAGNOSTICO FISIOTERAPISTA Y NUTRICIONISTA

VERSION 2.0.0

ACTUALIZADO EN 15/07/2017

'''

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.db import transaction
from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from diagnostico.models import DiagnosticoFisioterapia, DiagnosticoNutricion, Dieta, PlanNutDiario
from kalaapp.views import paginar
from paciente.models import Paciente
from personal.models import Personal
from .models import Rutina, Subrutina, DIAS

# Create your views here.


'''
Funcion: listarDiagnosticos
Entradas: request
Salidas: - HttpResponse con template diagnostico_listar.ntml y la lista de todos los diagnosticos

Funcion que permite listar los diagnosticos existentes
'''


@login_required
def listarDiagnosticos(request):
    template = 'diagnostico_listar.html'
    contexto = {}
    diagnosticos = None

    sesion = request.session.get('user_sesion', None)

    if sesion['rol__tipo'] == 'fisioterapista':
        diagnosticos = DiagnosticoFisioterapia.objects.filter(estado='A').order_by('-creado') \
            .annotate(paciente_nombre_completo=Concat('paciente__usuario__apellido', \
                                                      Value(' '), 'paciente__usuario__nombre')) \
            .annotate(paciente_id=Concat('paciente_id', Value('')))
    elif sesion['rol__tipo'] == 'nutricionista':
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
@transaction.atomic
def crearDiagnostico(request):
    template = None
    contexto = {}
    pacientes = None

    sesion = request.session.get('user_sesion', None)
    print sesion
    rol = sesion.get('rol__tipo', None)

    if request.method == 'POST':
        diagnostico = getDiagnostico(request, rol)

        if diagnostico is not None:
            messages.add_message(request, messages.SUCCESS, 'Diagnostico creado con exito!')
        else:
            messages.add_message(request, messages.WARNING, 'Error inesperado creando diagnostico!')
        return redirect('diagnostico:ListarDiagnosticos')

    try:
        pacientes = Paciente.objects.filter(estado='A', pacientepersonal__personal_id=sesion['personal__id'])\
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
        contexto['dias'] = {'One': 'Lunes', 'Two': 'Martes', 'Three': 'Miercoles',
                            'Four': 'Jueves', 'Five': 'Viernes', 'Six': 'Sabado'}
    else:
        template = '404.html'
    return render(request, template_name=template, context=contexto)

'''
Funcion: getDiagnostico
Entradas: - request
Salidas:  - nueva diagnostico

Funcion que retorna un nuevo diagnostico con los datos ingresados en formulario
'''


@transaction.atomic
def getDiagnostico(request, rol):
    diagnostico = None
    if rol:
        try:
            if rol == 'fisioterapista':
                diagnostico = DiagnosticoFisioterapia()
                diagnostico.area_afectada = request.POST.get('areaafectada', '')
                diagnostico.receta = request.POST.get('receta', '')
                s = Subrutina.objects.create(nombre="caminata", detalle="caminata x 60 minutos", veces=2, repeticiones=1, descanso=45, link='http://google.ec')
                diagnostico.rutina = Rutina.objects.create()
                diagnostico.rutina.subrutina.add(s)
            elif rol == 'nutricionista':
                print request.POST
                diagnostico = DiagnosticoNutricion()
                dieta = Dieta()
                for key, dia in DIAS:
                    plan_diario = PlanNutDiario(dia=dia, desayuno=dia+'_Desayuno', colacion1=dia+'_Colacion1',
                                                almuerzo=dia+'_Almuerzo', colacion2=dia+'_Colacion2',
                                                cena=dia+'_Cena')
                    plan_diario.save()
                    dieta.plan_nut_diario = plan_diario


            diagnostico.personal = Personal.objects.get(estado='A', id=sesion['personal__id'])
            diagnostico.paciente = Paciente.objects.get(estado='A', id=request.POST.get('paciente', 0))
            diagnostico.condiciones_previas = request.POST.get('condicionesprevias', '')
            diagnostico.save()
        except:
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
@transaction.atomic
def eliminarDiagnostico(request, id=0):
    contexto = {}

    if request.method == 'POST':
        try:
            diagnosticoEliminado = DiagnosticoFisioterapia.objects.get(id=id)

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
def editarDiagnostico(request, id=0):
    template = 'diagnostico_editar.html'
    contexto = {}
    diagnostico = None
    pacientes = None

    if request.method == 'POST':
        print id, request.POST
        try:
            diagnostico = DiagnosticoFisioterapia.objects.get(estado='A', id=id)
        except:
            messages.add_message(request, messages.WARNING, 'Error inesperado consultando diagnostico!')

        try:
            pacientes = Paciente.objects.filter(estado='A', pacientepersonal__personal_id=1) \
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

    if request.method == 'POST':
        try:
            diagnostico = DiagnosticoFisioterapia.objects.filter(estado='A', id=request.POST.get('diagnostico_id', 0)).first()
            diagnostico.condiciones_previas = request.POST.get('condicionesprevias', '')
            diagnostico.area_afectada = request.POST.get('areaafectada', '')
            diagnostico.receta = request.POST.get('receta', '')
            diagnostico.save()
            messages.add_message(request, messages.SUCCESS, 'Diagnostico actualizado satisfactoriamente!')
        except:
            messages.add_message(request, messages.WARNING, 'Error inesperado al actualizar diagnostico!')

    return redirect('diagnostico:ListarDiagnosticos')


'''
'''
