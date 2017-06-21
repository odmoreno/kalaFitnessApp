# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from paciente.models import Paciente
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

def pacientes(request):
    template = 'paciente/pacientes.html'
    p = Paciente.objects.all()
    data = {
            'pacientes':p,

        }
    return render(request, template, data)

def index(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/index.html', {'pacientes': pacientes})

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

@transaction.atomic
def PacienteEliminar(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    paciente.delete()
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/index.html', {'pacientes': pacientes})


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
