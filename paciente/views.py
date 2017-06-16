# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render
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



def pacientes(request):
    template = 'paciente/pacientes.html'
    p = Paciente.objects.all()
    data = {
            'pacientes':p,

        }
    return render(request, template, data)

def apiPacientes(request):
    template = "paciente/paciente.html"
    p = Paciente.objects.all()
    data = {"pacientes": p}
    return render(request, template, data)

def apiRestPacientes(request):
    p = Paciente.objects.all()
    #data = {"pacientes": p}
    data = serializers.serialize('json', p)
    return HttpResponse(data, content_type="application/json")
    #return JsonResponse(data)
    #return render(request, template, data)

@transaction.atomic
def nuevoPaciente(request):
    rol = Rol.objects.get(tipo='paciente')
    #template = 'paciente/crearPaciente.html'
    if request.method == 'POST':
        try:
            #Crea un USER
            user = User()
            user.username = request.POST.get('cedula', False)
            user.set_password("p.123456")
            user.save()

            usuario = Usuario()
            usuario.usuario = user
            usuario.rol = rol
            usuario.nombre = request.POST['nombre']
            usuario.apellido = request.POST['apellido']
            usuario.cedula = request.POST['cedula']
            usuario.direccion = request.POST['direccion']
            usuario.telefono = request.POST['telefono']
            usuario.ocupacion = request.POST['ocupacion']
            usuario.genero = request.POST['genero']
            usuario.edad = request.POST['edad']
            usuario.fecha_nacimiento = request.POST['fecha']
            #usuario.foto = request.POST['foto']
            usuario.save()

            paciente=Paciente()
            paciente.usuario=usuario
            paciente.save()
            return JsonResponse({"message": "Paciente creado"})
        except Exception:
            return JsonResponse({"message": "Error crear paciente"})
        #return HttpResponseRedirect(reverse('pacientes'))
    #return render(request, template)




@transaction.atomic
def modificarPaciente(request,paciente_id):
    template = 'paciente/datosPacientes.html'
    pacientes = Paciente.objects.all()
    for p in pacientes:
        if p.usuario.cedula==paciente_id:
             usuario=p.usuario
    data = {"paciente": p}
    return render(request, template, data)

@transaction.atomic
def eliminarPaciente(request, paciente_id):
    pacientes = Paciente.objects.all()
    for p in pacientes:
        if p.usuario.cedula==paciente_id:
            print p
            p.delete()
            break
    return JsonResponse({"message": "Paciente eliminado"})
    #return HttpResponse({"message": "Paciente eliminado"}, content_type="application/json")
    #return HttpResponseRedirect(reverse('pacientes'))


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


@transaction.atomic
def PacienteModificar(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    form = UsuarioForm(request.GET or None)
    context = {
        "form": form,
        "paciente": paciente.usuario
    }
    #return render(request, 'paciente/form_paciente.html', context)
