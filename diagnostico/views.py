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
# Create your views here.

def listarDiagnosticos(request):
    template = 'crear.html'
    contexto={}
    # contexto['facturas'] = Facturas.objects.filter(estado='A')\
    #     .values('id', 'empresa__nombre', 'paciente_id', 'paciente__usuario__apellido',\
    #             'paciente__usuario__nombre', 'serie', 'fecha_vencimiento', 'total')
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
            messages.add_message(request, messages.SUCCESS, 'Diagnóstico creado con exito!')
        else:
            messages.add_message(request, messages.ERROR, 'Error inesperado!')
        return redirect('diagnostico:CrearDiagnostico')
    try:
        #pacientes_personal=PacientePersonal.objects.filter(estado='A', personal_id=881).values_list('usuario_id')
        #return HttpResponse(pacientes_personal)
        pacientes = Paciente.objects.filter(estado='A')
            #.values('id', 'usuario__nombre', 'usuario__apellido') \
            #.annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
            #.order_by('id', 'nombre_completo')  #.values_list('id', 'usuario__nombre', 'usuario__apellido') \
        return HttpResponse(pacientes)
    except:
        return HttpResponse('EXCEPTION')

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
        diagnostico.personal = Personal.objects.filter(estado='A')\
            .get(id=1)
        diagnostico.paciente = Paciente.objects.filter(estado='A')\
            .get(id=request.POST.get('paciente', 0))
        diagnostico.altura = request.POST.get('altura')
        diagnostico.peso = request.POST.get('peso')
        diagnostico.imc = request.POST.get('imc')
        diagnostico.imc = request.POST.get('musculo')
        diagnostico.grasa_visceral = request.POST.get('grasavisceral')
        diagnostico.grasa_porcentaje = request.POST.get('grasa')
        diagnostico.cuello = request.POST.get('cuello')
        diagnostico.hombros = request.POST.get('hombros')
        diagnostico.pecho = request.POST.get('pecho')
        diagnostico.brazo_derecho = request.POST.get('brazoderecho')
        diagnostico.brazo_izquierdo = request.POST.get('brazoizquierdo')
        diagnostico.antebrazo_derecho = request.POST.get('antebrazoderecho')
        diagnostico.antebrazo_izquierdo = request.POST.get('antebrazoizquierdo')
        diagnostico.cintura = request.POST.get('cintura')
        diagnostico.cadera = request.POST.get('cadera')
        diagnostico.musloderecho = request.POST.get('musloderecho')
        diagnostico.musloizquierdo = request.POST.get('musloizquierdo')
        diagnostico.pantorrilla_derecha = request.POST.get('pantorrilladerecha')
        diagnostico.pantorrilla_izquierda = request.POST.get('pantorrillaizquierda')
        diagnostico.flexiones = request.POST.get('flexiones')
        diagnostico.cadera_arriba = request.POST.get('caderaarriba')
        diagnostico.abdomen = request.POST.get('abdomen')
        diagnostico.espinales = request.POST.get('espinales')
        diagnostico.lumbares = request.POST.get('lumbares')
        diagnostico.sentadillas = request.POST.get('sentadillas')
        diagnostico.condiciones_previas = request.POST.get('condicionesprevias')
        diagnostico.rutina = request.POST.get('rutina')
        diagnostico.receta = request.POST.get('receta')
        diagnostico.save()
    except :
        return None
    return diagnostico