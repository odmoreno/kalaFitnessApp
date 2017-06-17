# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from kalaapp.models import Usuario, Rol
from .forms import  UsuarioForm
from personal.models import Personal
from paciente.views import Paciente
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

'''
def apiPersonal(request):
    template = "personal/personal.html"
    obj = Personal.objects.all()
    data = {"personal": obj}
    return render(request, template, data)
'''
#@login_required
def index(request):
    all_personal = Usuario.objects.all()
    return render(request, 'personal/index.html', {'all_personal': all_personal})

@transaction.atomic
def nPersonal(request):
    rol = Rol.objects.get(tipo='fisioterapista')
    #rol.tipo = 'fisioterapista'
    #rol.save()
    if request.method == 'POST':
        user = User()
        user.username = request.POST['cedula']
       # print ("Cedula:"+request.POST['cedula'])
      #  print ("cedula11:"+user.username)
        user.username = request.POST.get('cedula', False)
        #print ("Cedula:"+request.POST['cedula'])
        #print ("cedula11:"+user.username)
        user.set_password("p.123456")
        user.save()

        rol.tipo = request.POST['ocupacion']
        rol.save()

        usuario = Usuario()
        usuario.usuario = user
        usuario.rol = rol
        usuario.nombre = request.POST['nombre']
       # print("nombre:" + usuario.nombre)
        usuario.apellido = request.POST['apellido']
        usuario.cedula = request.POST.get('cedula', False)
        usuario.direccion = request.POST['direccion']
        usuario.telefono = request.POST['telefono']
        usuario.ocupacion = request.POST['ocupacion']
        usuario.genero = request.POST['genero']
        usuario.edad = request.POST['edad']
        #usuario.fecha_nacimiento = request.POST['fecha']
        usuario.save()

        #return HttpResponseRedirect(reverse('index.html'))
        all_personal = Usuario.objects.all()
        #return render(request, 'personal/index.html', {'all_personal': all_personal})
    #return  render(request, 'personal/create_personal.html')
    #fields = ['nombre', 'apellido', 'cedula', 'direccion', 'telefono', 'ocupacion', 'genero', 'edad', 'fecha_nacimento']
    return HttpResponse({"message": "Nuevo personal creado"}, content_type="application/json")

def eliminarPersonal(request, personal_id):
    personal = Usuario.objects.get(pk=personal_id)
    personal.delete()
    all_personal = Usuario.objects.all()
    #return HttpResponse({"message": "Se elimino el personal" + personal_id}, content_type="application/json")
    return render(request, 'personal/index.html', {'all_personal': all_personal})

@transaction.atomic
def nuevoPersonal(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        personal = form.save(commit=False)
        user = User()
        user.username = form.cleaned_data['cedula']
        user.set_password('1234')
        user.save()

        rol = Rol.objects.get(tipo='nutricionista')
        rol.save()

        personal.usuario = user
        personal.rol = rol
        personal.save()

        all_personal = Usuario.objects.all()
        return render(request, 'personal/index.html', {'all_personal': all_personal})

    context = {
        "form": form,
    }
    return render(request, 'personal/form_personal.html', context)
