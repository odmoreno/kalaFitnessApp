# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#import MyPrint as MyPrint
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from paciente.models import Paciente
#from paciente.models import paciente
from kalaapp.models import Usuario, Rol
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.http import HttpRequest,HttpResponse
from django.urls.base import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from personal.forms import  UsuarioForm

from django.http import JsonResponse

#import json
#from django.http import JsonResponse
from io import BytesIO


'''
MODULO Pacientes

VERSION 2.0.0

ACTUALIZADO EN 20/06/2017

'''

def pacientes(request):
    template = 'paciente/pacientes.html'
    p = Paciente.objects.all()
    data = {
            'pacientes':p,

        }
    return render(request, template, data)
'''
Funcion: index
Entradas: requerimiento
Salidas:Template para renderizacion junto con JSON con los pacientes de la base de datos
*Funcion que retorna a los pacientes registrados en la base de datos*

'''
def index(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/index.html', {'pacientes': pacientes})
'''
Funcion: PacienteNuevo
Entradas: requerimiento GET y POST
Salidas:Template para renderizacion junto con FORM para el registro de nuevos Pacientes
*Funcion que renderiza un form para el ingreso de nuevos pacientes y, una vez llenado, recibe
por medio de POST los datos para generar el registro del paciente en la base de datos*

'''
#@login_required
@transaction.atomic
def PacienteNuevo(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        usuario = form.save(commit=False)
        user = User()
        paciente = Paciente()

        user.username = form.cleaned_data['cedula']
        user.set_password('1234')
        user.save()

        rol = Rol.objects.get(tipo='paciente')
        rol.save()

        usuario.usuario = user
        usuario.rol = rol
        usuario.save()

        paciente.usuario = usuario
        paciente.save()

        pacientes = Paciente.objects.all()
        return render(request, 'paciente/index.html', {'pacientes': pacientes})

    context = {
        "form": form,
    }
    return render(request, 'paciente/form_paciente.html', context)
'''
Funcion: PacienteEliminar
Entradas: requerimiento e Identificador del paciente a ser eliminado 
Salidas:Template para renderizacion 
*Funcion que recibe el id de un paciente que debe ser eliminado, y elimina su registro de 
la base de datos retornando a la pagina de visualizacion de los pacientes.*

'''
@transaction.atomic
def PacienteEliminar(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    paciente.delete()
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/index.html', {'pacientes': pacientes})

'''
Funcion: detallePaciente
Entradas: requerimiento e Identificador del paciente a ser visualizado 
Salidas:Template para renderizacion 
*Funcion que recibe el id de un paciente que debe ser visualizado, y muestra su informacion.*
'''

def detallePaciente(request, paciente_id):
    paciente = get_object_or_404(Usuario, pk=paciente_id)
    return render(request, 'paciente/detalles.html', {'paciente': paciente})

@transaction.atomic
def PacienteModificar(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    form = UsuarioForm(request.GET or None)
    context = {
        "form": form,
        "paciente": paciente.usuario
    }
    #return render(request, 'paciente/form_paciente.html', context)
'''
Funcion: reportePaciente
Entradas: requerimiento 
Salidas: JSON con todos los pacientes
*Funcion que retorna la informacion de los pacientes registrados en la base de datos
en forma de un JSON*
'''
def reportePacientes(request):
    pacientes = Paciente.objects.all()
    p = []

    for paciente in pacientes:
        cedula = paciente.usuario.cedula
        nombre = paciente.usuario.nombre
        apellido = paciente.usuario.apellido
        telefono = paciente.usuario.telefono
        genero = paciente.usuario.genero
        record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"genero":genero}
        p.append(record)

    return JsonResponse({"pacientes": p})

def reportePDF(request):
    template = 'paciente/reportePDF.html'
    return render(request, template)

def pdf_pacientes(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pacientes.pdf"'

    buffer = BytesIO()

    report = MyPrint(buffer, 'Letter')
    pdf = report.print_users()

    response.write(pdf)
    return response


