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
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from directmessages.apps import Inbox
from directmessages.models import Message

#@login_required
def index(request):
    all_personal = Usuario.objects.all()
    return render(request, 'personal/index.html', {'all_personal': all_personal})

def eliminarPersonal(request, personal_id):
    personal = Usuario.objects.get(pk=personal_id)
    # user=personal.usuario
    # user.delete()
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
        #rol.save()

        personal.usuario = user
        personal.rol = rol
        personal.save()

        all_personal = Usuario.objects.all()
        return render(request, 'personal/index.html', {'all_personal': all_personal})

    context = {
        "form": form,
    }
    return render(request, 'personal/form_personal.html', context)

def detallePersonal(request, personal_id):
    personal = get_object_or_404(Usuario, pk=personal_id)
    return render(request, 'personal/detalles.html', {'personal': personal})

def verMensajes(request, personal_id=None):
    template= 'personal/mensajes.html'

    mensajes=Message.objects.all().filter(recipient=request.user)
    if mensajes:
        nombres=[]
        usuarios=[]
        for m in mensajes:
            usuario=Usuario.objects.get(usuario=m.sender)
            nombre=usuario.nombre +" "+ usuario.apellido
            nombres.append(nombre)
            usuarios.append(usuario)

        data={
            'mensajes': mensajes,
            'nombres':nombres,
            'usuarios':usuarios
        }
    return render(request,template,data)

def leerMensaje(request, mensaje_id):
    message=Message.objects.get(id=mensaje_id)
    user=User.objects.get(id=message.sender.id)
    usuarioN=Usuario.objects.get(usuario=user)
    nombre=usuarioN.nombre + " " + usuarioN.apellido
    data={
        'sender':nombre,
        'mensaje':message.content,

    }
    return render(request, "personal/leerMensaje.html", data)

def nuevoMensaje(request):
    personal= Usuario.objects.all()
    print personal
    data={
        'personal':personal,
    }
    if request.method == 'POST':
        return render(request, "personal/mensajes.html")

    return render(request, "personal/nuevoMensaje.html", data)

def reportePersonal(request):
    personal = Personal.objects.all()
    per = []

    for p in personal:
        cedula = p.usuario.cedula
        nombre = p.usuario.nombre
        apellido = p.usuario.apellido
        telefono = p.usuario.telefono
        genero = p.usuario.genero
        record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"genero":genero}
        per.append(record)

    return JsonResponse({"data": per})

def reportePDF(request):
    template = 'personal/reportePDF.html'
    return render(request, template)
