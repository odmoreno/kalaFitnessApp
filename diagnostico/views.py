'''
MODULO DIAGNOSTICO

VERSION 1.0.0

ACTUALIZADO EN 15/07/2017

'''

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from diagnostico.models import Diagnostico
from django.http import HttpResponseRedirect, HttpRequest,HttpResponse
from personal.models import Personal
from paciente.models import Paciente, PacientePersonal
from django.db.models.functions import Concat
from django.db.models import Value
from django.db import transaction
from django.urls.base import reverse
from django.contrib import messages
from django.contrib.messages import get_messages
from django.db import transaction
from django.contrib.auth.models import User
from django.urls.base import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def listarDiagnosticos(request):
    template = 'diagnostico.html'
    contexto={}
    diagnosticos_por_pagina = 10
    diagnosticos_paginator = None

    diagnosticos = Diagnostico.objects.filter(estado='A').order_by('-creado') \
        .annotate(paciente_nombre_completo=Concat('paciente__usuario__apellido',\
                                            Value(' '), 'paciente__usuario__nombre'))\
        .annotate(paciente_id=Concat('paciente_id', Value('')))

    pag = request.GET.get('pag', 1)

    paginator = Paginator(diagnosticos, diagnosticos_por_pagina)

    try:
        diagnosticos_paginator = paginator.page(pag)
    except PageNotAnInteger:
        diagnosticos_paginator = paginator.page(1)
    except EmptyPage:
        diagnosticos_paginator = paginator.page(paginator.num_pages)

    contexto['diagnosticos_paginator'] = diagnosticos_paginator
    contexto['diagnosticos'] = diagnosticos

    return render(request, template_name=template, context=contexto)

'''
Funcion: crearDiagnostico
Entradas: request
Salidas: - HttpResponse con template crear.ntml y la lista de todas los pacientes

Funcion que permite crear un nuevo diagnostico
'''
@transaction.atomic
def crearDiagnostico(request):
    template = 'crear.html'
    contexto={}

    if request.method == 'POST':
        diagnostico = getDiagnostico(request)

        if diagnostico is not None:
            messages.add_message(request, messages.SUCCESS, 'Diagnostico creado con exito!')
        else:
            messages.add_message(request, messages.WARNING, 'Error inesperado creando diagnostico!')
        return redirect('diagnostico:ListarDiagnosticos')

    try:
        pacientes = Paciente.objects.filter(estado='A', pacientepersonal__personal_id=1)\
            .values('id', 'usuario__nombre', 'usuario__apellido') \
            .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
            .order_by('nombre_completo')  #.values_list('id', 'usuario__nombre', 'usuario__apellido') \
    except:
        messages.add_message(request, messages.WARNING, 'Error inesperado consultando pacientes!')

    contexto['pacientes'] = pacientes
    return render(request, template_name=template, context=contexto)

'''
Funcion: getDiagnostico
Entradas: - request
Salidas:  - nueva diagnostico

Funcion que retorna un nuevo diagnostico con los datos ingresados en formulario
'''
def getDiagnostico(request):
    try:
        diagnostico = Diagnostico()
        diagnostico.personal = Personal.objects.filter(estado='A', id=1).first()
        diagnostico.paciente = Paciente.objects.filter(estado='A', id=request.POST.get('paciente', 0)).first()
        diagnostico.altura = request.POST.get('altura', 1.0)
        diagnostico.peso = request.POST.get('peso', 1.0)
        diagnostico.imc = request.POST.get('imc', 1.0)
        diagnostico.musculo = request.POST.get('musculo', 1.0)
        diagnostico.grasa_visceral = request.POST.get('grasavisceral', 1.0)
        diagnostico.grasa_porcentaje = request.POST.get('grasa', 1.0)
        diagnostico.cuello = request.POST.get('cuello', 1.0)
        diagnostico.hombros = request.POST.get('hombros', 1.0)
        diagnostico.pecho = request.POST.get('pecho', 1.0)
        diagnostico.brazo_derecho = request.POST.get('brazoderecho', 1.0)
        diagnostico.brazo_izquierdo = request.POST.get('brazoizquierdo', 1.0)
        diagnostico.antebrazo_derecho = request.POST.get('antebrazoderecho', 1.0)
        diagnostico.antebrazo_izquierdo = request.POST.get('antebrazoizquierdo', 1.0)
        diagnostico.cintura = request.POST.get('cintura', 1.0)
        diagnostico.cadera = request.POST.get('cadera', 1.0)
        diagnostico.musloderecho = request.POST.get('musloderecho', 1.0)
        diagnostico.musloizquierdo = request.POST.get('musloizquierdo', 1.0)
        diagnostico.pantorrilla_derecha = request.POST.get('pantorrilladerecha', 1.0)
        diagnostico.pantorrilla_izquierda = request.POST.get('pantorrillaizquierda', 1.0)
        diagnostico.flexiones = request.POST.get('flexiones', 1)
        diagnostico.cadera_arriba = request.POST.get('caderaarriba', 1)
        diagnostico.abdomen = request.POST.get('abdomen', 1)
        diagnostico.espinales = request.POST.get('espinales', 1)
        diagnostico.lumbares = request.POST.get('lumbares', 1)
        diagnostico.sentadillas = request.POST.get('sentadillas', 1)
        diagnostico.condiciones_previas = request.POST.get('condicionesprevias', '')
        diagnostico.area_afectada = request.POST.get('areaafectada', '')
        diagnostico.rutina = request.POST.get('rutina', '')
        diagnostico.receta = request.POST.get('receta', '')
        diagnostico.save()
    except :
        return None
    return diagnostico

'''
Funcion: crearDiagnostico
Entradas: - request
          - id: id del diagnostico a eliminar
Salidas: ninguna

Funcion que permite eliminar un diagnostico existente
'''
@transaction.atomic
def eliminarDiagnostico(request, id=0):
    contexto = {}

    if request.method == 'POST':
        try:
            diagnosticoEliminado = Diagnostico.objects.get(id=id)

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
@transaction.atomic
def editarDiagnostico(request, id=0):
    template = 'editar.html'
    contexto = {}

    if request.method == 'POST':
        try:
            diagnostico = Diagnostico.objects.filter(estado='A', id=id).first()
        except:
            messages.add_message(request, messages.WARNING, 'Error inesperado consultando diagnostico!')

        try:
            pacientes = Paciente.objects.filter(estado='A', pacientepersonal__personal_id=1) \
                .values('id', 'usuario__nombre', 'usuario__apellido') \
                .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
                .order_by('nombre_completo')  # .values_list('id', 'usuario__nombre', 'usuario__apellido') \
        except:
            messages.add_message(request, messages.WARNING, 'Error inesperado consultando pacientes!')

        contexto['diagnostico'] = diagnostico
        contexto['pacientes'] = pacientes

        return render(request, template_name=template, context=contexto)

'''
Funcion: guardarDiagnostico
Entradas: - request
Salidas: ninguna

Funcion que persiste un diagnostico en base
'''
@transaction.atomic
def guardarDiagnostico(request):

    if request.method == 'POST':
        try:
            diagnostico = Diagnostico.objects.filter(estado='A', id=request.POST.get('diagnostico_id', 0)).first()
            #diagnostico.paciente = ?
            diagnostico.altura = request.POST.get('altura', 1.0)
            diagnostico.peso = request.POST.get('peso', 1.0)
            diagnostico.imc = request.POST.get('imc', 1.0)
            diagnostico.musculo = request.POST.get('musculo', 1.0)
            diagnostico.grasa_visceral = request.POST.get('grasavisceral', 1.0)
            diagnostico.grasa_porcentaje = request.POST.get('grasa', 1.0)
            diagnostico.cuello = request.POST.get('cuello', 1.0)
            diagnostico.hombros = request.POST.get('hombros', 1.0)
            diagnostico.pecho = request.POST.get('pecho', 1.0)
            diagnostico.brazo_derecho = request.POST.get('brazoderecho', 1.0)
            diagnostico.brazo_izquierdo = request.POST.get('brazoizquierdo', 1.0)
            diagnostico.antebrazo_derecho = request.POST.get('antebrazoderecho', 1.0)
            diagnostico.antebrazo_izquierdo = request.POST.get('antebrazoizquierdo', 1.0)
            diagnostico.cintura = request.POST.get('cintura', 1.0)
            diagnostico.cadera = request.POST.get('cadera', 1.0)
            diagnostico.musloderecho = request.POST.get('musloderecho', 1.0)
            diagnostico.musloizquierdo = request.POST.get('musloizquierdo', 1.0)
            diagnostico.pantorrilla_derecha = request.POST.get('pantorrilladerecha', 1.0)
            diagnostico.pantorrilla_izquierda = request.POST.get('pantorrillaizquierda', 1.0)
            diagnostico.flexiones = request.POST.get('flexiones', 1)
            diagnostico.cadera_arriba = request.POST.get('caderaarriba', 1)
            diagnostico.abdomen = request.POST.get('abdomen', 1)
            diagnostico.espinales = request.POST.get('espinales', 1)
            diagnostico.lumbares = request.POST.get('lumbares', 1)
            diagnostico.sentadillas = request.POST.get('sentadillas', 1)
            diagnostico.condiciones_previas = request.POST.get('condicionesprevias', '')
            diagnostico.area_afectada = request.POST.get('areaafectada', '')
            diagnostico.rutina = request.POST.get('rutina', '')
            diagnostico.receta = request.POST.get('receta', '')
            diagnostico.save()
        except:
            messages.add_message(request, messages.WARNING, 'Error inesperado al actualizar diagnostico!')

    return redirect('diagnostico:ListarDiagnosticos')
