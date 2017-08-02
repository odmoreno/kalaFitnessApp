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
from kala.views import enviar_password_email, generar_password
from personal.forms import UsuarioForm, UsuarioEditForm

from django.http import JsonResponse

#import json
#from django.http import JsonResponse
from io import BytesIO


'''
MODULO Pacientes

VERSION 2.0.0

ACTUALIZADO EN 20/06/2017

'''
@login_required
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
@login_required
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
@login_required
@transaction.atomic
def PacienteNuevo(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        '''
        Si no hay errores en el formulario, sigue el siguiente flujo:
        1.-Crea un nuevo usuario
        2.-Guarda los valores del formulario en ese usuario
        3.-Crea un nuevo User
        4.-Lo inicializa con los valores del form
        5.-Guarda el User
        6.-Obtiene el rol de paciente en un objeto
        7.-Enlaza el nuevo user con el Usuario antes creado, y Con el Rol
        8.-Crea un nuevo Paciente
        9.-Lo enlaza con el nuevo usuario
        10.-Guarda el paciente
        
        '''
        usuario = form.save(commit=False)
        user = User()
        paciente = Paciente()
        user.username = form.cleaned_data['cedula']
        password = generar_password()
        user.set_password(password)
        user.email = form.cleaned_data['email']
        user.save()

        rol = Rol.objects.filter(tipo='paciente').first()

        usuario.usuario = user
        usuario.rol = rol
        usuario.save()

        paciente.usuario = usuario
        paciente.save()

        enviar_password_email(user.email, user.username, password)

        pacientes = Paciente.objects.all()
        return render(request, 'paciente/index.html', {'pacientes': pacientes})

    context = {
        "form": form,
    }
    return render(request, 'paciente/form_paciente.html', context)
'''
Funcion: editarPaciente
Entradas: requerimiento e Identificador del paciente a ser editado
Salidas:Template para renderizacion y lista de pacientes 
*Funcion que recibe el id de un paciente que debe ser editado, y Muestra un formulario llenado con la info 
anterior del paciente para que esta sea editada.*

'''
@login_required
@transaction.atomic
def editarPaciente(request, paciente_id):
    pacientes = get_object_or_404(Paciente, pk=paciente_id)
    paciente=pacientes.usuario
    form = UsuarioEditForm(request.POST or None, instance=paciente)
    #form.email=personal.usuario.email
    if form.is_valid():
        user=paciente.usuario
        user.email = form.cleaned_data['email']
        user.save()
        paciente = form.save()
        all_pacientes = Paciente.objects.all()
        return render(request, 'paciente/index.html', {'pacientes': all_pacientes})

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
@login_required
@transaction.atomic
def PacienteEliminar(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    paciente.usuario.estado="I"
    paciente.usuario.save()
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/index.html', {'pacientes': pacientes})

'''
Funcion: detallePaciente
Entradas: requerimiento e Identificador del paciente a ser visualizado 
Salidas:Template para renderizacion 
*Funcion que recibe el id de un paciente que debe ser visualizado, y muestra su informacion.*
'''
@login_required
def detallePaciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    usuario=paciente.usuario
    return render(request, 'paciente/detalles.html', {'paciente': usuario})


'''
Funcion: reportePaciente
Entradas: requerimiento 
Salidas: JSON con todos los pacientes
*Funcion que retorna la informacion de los pacientes registrados en la base de datos
en forma de un JSON*
'''
@login_required
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

@login_required
def reportePDF(request):
    template = 'paciente/reportePDF.html'
    return render(request, template)

@login_required
def pdf_pacientes(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pacientes.pdf"'

    buffer = BytesIO()

    report = MyPrint(buffer, 'Letter')
    pdf = report.print_users()

    response.write(pdf)
    return response


