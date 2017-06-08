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
#import json
#from django.http import JsonResponse

# Create your views here.
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
    rol = Rol()
    rol.save()
    #template = 'paciente/crearPaciente.html'
    if request.method == 'POST':
        #Crea un USER
        user = User()
        user.username = request.POST['cedula']
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
        #return HttpResponseRedirect(reverse('pacientes'))
    #return render(request, template)
    return HttpResponse({"message": "Nuevo paciente creado"}, content_type="application/json")



@transaction.atomic
def modificarPaciente(request,paciente_id):
#     pacientes = Paciente.objects.all()
#     for p in pacientes:
#         if p.usuario.cedula==paciente_id:
#             usuario=p.usuario
    
    pass
@transaction.atomic
def eliminarPaciente(request, paciente_id):
    pacientes = Paciente.objects.all()
    for p in pacientes:
        if p.usuario.cedula==paciente_id:
            p.delete()
            break
    return HttpResponse({"message": "Paciente eliminado"}, content_type="application/json")
    #return HttpResponseRedirect(reverse('pacientes'))
