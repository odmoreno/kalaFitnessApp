# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import json
# from django.http import JsonResponse
from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# import MyPrint as MyPrint
from django.db import transaction
from django.db.models import Value
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from kala.views import enviar_password_email, generar_password
# from paciente.models import paciente
from kalaapp.models import Rol, Usuario
from paciente.models import Paciente
from personal.forms import UsuarioForm, UsuarioEditForm

'''
MODULO Pacientes

VERSION 3.0.0

ACTUALIZADO EN 01/08/2017

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
    pacientes = Paciente.objects.all().annotate(foto=Concat('usuario__foto', Value('')))
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
    form = UsuarioForm(request.POST, request.FILES)
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
        usuario.foto = form.cleaned_data['foto']
        usuario.save()

        paciente.usuario = usuario
        paciente.n_hijos=form.cleaned_data['n_hijos']
        paciente.motivo_consulta=form.cleaned_data['motivo_consulta']
        paciente.observaciones=form.cleaned_data['observaciones']

        paciente.save()

        enviar_password_email(user.email, user.username, password)

        # pacientes = Paciente.objects.all()
        # return render(request, 'paciente/index.html', {'pacientes': pacientes})
        return redirect('paciente:index')

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
    user=paciente.usuario
    form.fields["email"].initial = user.email
    #form.email=personal.usuario.email
    if form.is_valid():
        user=paciente.usuario
        user.email = form.cleaned_data['email']
        user.save()
        paciente = form.save()
        return redirect('paciente:index')

    context = {
        "form": form,
        "editar":True
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
    paciente.usuario.estado = "I"
    paciente.estado = "I"
    paciente.usuario.save()
    #pacientes = Paciente.objects.all()
    #return render(request, 'paciente/index.html', {'pacientes': pacientes})
    return redirect('paciente:index')

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
Funcion: reporteTotales
Entradas: requerimiento
Salidas: JSON con todos los pacientes
*Funcion que retorna la informacion de los pacientes registrados en la base de datos
en forma de un JSON*
'''
@login_required
def reporteTotales(request):
    pacientes = Paciente.objects.all()
    p = []

    for paciente in pacientes:
        if paciente.usuario.genero == 'M' or paciente.usuario.genero == 'F':
            cedula = paciente.usuario.cedula
            nombre = paciente.usuario.nombre
            apellido = paciente.usuario.apellido
            telefono = paciente.usuario.telefono
            genero = paciente.usuario.genero
            record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"genero":genero}
            p.append(record)

    return JsonResponse({"pacientes": p})

'''
Funcion: reporteMujeres
Entradas: requerimiento
Salidas: JSON con todos los pacientes del genero femenino
*Funcion que retorna la informacion de los pacientes registrados en la base de datos
en forma de un JSON*
'''
@login_required
def reporteMujeres(request):
    pacientes = Paciente.objects.all()
    p = []

    for paciente in pacientes:
        if paciente.usuario.genero=='F':
            cedula = paciente.usuario.cedula
            nombre = paciente.usuario.nombre
            apellido = paciente.usuario.apellido
            telefono = paciente.usuario.telefono
            genero = paciente.usuario.genero
            record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"genero":genero}
            p.append(record)

    return JsonResponse({"pacientes": p})


'''
Funcion: reporteHombres
Entradas: requerimiento
Salidas: JSON con todos los pacientes del genero femenino
*Funcion que retorna la informacion de los pacientes registrados en la base de datos
en forma de un JSON*
'''
@login_required
def reporteHombres(request):
    pacientes = Paciente.objects.all()
    p = []

    for paciente in pacientes:
        if paciente.usuario.genero=='M':
            cedula = (paciente.usuario.cedula)
            nombre = paciente.usuario.nombre
            apellido = paciente.usuario.apellido
            telefono = paciente.usuario.telefono
            genero = paciente.usuario.genero
            record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"genero":genero}
            p.append(record)

    return JsonResponse({"pacientes": p})
'''
Funcion: reportes
Entradas: requerimiento get http
Salidas: Retorna un template de reportes de pacientes
'''
@login_required
def reportes(request):
    template = 'paciente/reportes.html'
    return render(request, template)
