# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from kalaapp.models import Usuario, Rol
from paciente.views import Paciente
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse


def index(request):

    all_personal = Usuario.objects.all()
    return render(request, 'personal/index.html', {'all_personal': all_personal})

def nuevoPersonal(request):

    rol = Rol()
    rol.es_personal=True
    rol.tipo = 'fisioterapista'
    rol.save()
    if request.method == 'POST':
        user = User()
        user.username = request.POST['cedula']
        print ("Cedula:"+request.POST['cedula'])
        print ("cedula11:"+user.username)
        user.set_password("p.123456")
        user.save()

        usuario = Usuario()
        usuario.usuario = user
        usuario.rol = rol
        usuario.nombre = request.POST['nombre']
        print("nombre:" + usuario.nombre)
        usuario.apellido = request.POST['apellido']
        usuario.cedula = request.POST['cedula']
        usuario.direccion = request.POST['direccion']
        usuario.telefono = request.POST['telefono']
        usuario.ocupacion = request.POST['ocupacion']
        usuario.genero = request.POST['genero']
        usuario.edad = request.POST['edad']
        #usuario.fecha_nacimiento = request.POST['fecha']
        usuario.save()

        return HttpResponseRedirect(reverse('index'))
    return  render(request, 'personal/create_personal.html')
    #fields = ['nombre', 'apellido', 'cedula', 'direccion', 'telefono', 'ocupacion', 'genero', 'edad', 'fecha_nacimento']

