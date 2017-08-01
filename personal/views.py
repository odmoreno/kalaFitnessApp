# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from kalaapp.models import Usuario, Rol
from .forms import  UsuarioForm, PersonalForm, ComentarioForm, PersonalEditForm
from personal.models import Personal
#from paciente.views import paciente
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from directmessages.apps import Inbox
from directmessages.models import Message

#@login_required
def index(request):
    all_personal = Usuario.objects.filter(estado="A")
    return render(request, 'personal/index.html', {'all_personal': all_personal})

def eliminarPersonal(request, personal_id):
    personal = Usuario.objects.get(pk=personal_id)
    # user=personal.usuario
    # user.delete()
    personal.estado="I"
    all_personal = Usuario.objects.filter(estado="A")
    #return HttpResponse({"message": "Se elimino el personal" + personal_id}, content_type="application/json")
    return render(request, 'personal/index.html', {'all_personal': all_personal})

@transaction.atomic
def nuevoPersonal(request):
    form = PersonalForm(request.POST or None)
    if form.is_valid():
        personal = form.save(commit=False)
        user = User()
        user.username = form.cleaned_data['cedula']
        user.set_password('1234')
        user.email = form.cleaned_data['email']
        user.save()
        if form.cleaned_data["ocupacion"]== "1":
            rol = Rol.objects.get(tipo='fisioterapista')

        else:
            rol = Rol.objects.get(tipo='nutricionista')

        personal.usuario = user
        personal.rol = rol
        personal.save()

        all_personal = Usuario.objects.filter(estado="A")
        return render(request, 'personal/index.html', {'all_personal': all_personal})

    context = {
        "form": form,
    }
    return render(request, 'personal/form_personal.html', context)

@transaction.atomic
def editarPersonal(request, personal_id):
    personal = get_object_or_404(Usuario, pk=personal_id)
    print personal.rol.tipo
    form = PersonalEditForm(request.POST or None, instance=personal)
    #form.email=personal.usuario.email
    if form.is_valid():
        user=personal.usuario
        user.email = form.cleaned_data['email']
        user.save()
        if form.cleaned_data["ocupacion"] == "1":
            rol = Rol.objects.get(tipo='fisioterapista')
        else:
            rol = Rol.objects.get(tipo='nutricionista')

        print rol.tipo
        personal.rol = rol
        print personal.rol.tipo
        personal.save()
        personal = form.save()
        all_personal = Usuario.objects.filter(estado="A")
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
#separar mensajes
    mensajes=Message.objects.all().filter(recipient=request.user)
    if mensajes:
        nombresL = []
        nombresN = []
        usuariosL = []
        usuariosN = []
        mensajesL = []
        mensajesN = []
        for m in mensajes:
            if m.read_at == None:
                usuario=Usuario.objects.get(usuario=m.sender)
                nombre=usuario.nombre +" "+ usuario.apellido
                nombresN.append(nombre)
                usuariosN.append(usuario)
                mensajesN.append(m)
            else:
                usuario = Usuario.objects.get(usuario=m.sender)
                nombre = usuario.nombre + " " + usuario.apellido
                nombresL.append(nombre)
                usuariosL.append(usuario)
                mensajesL.append(m)


        data={
            'mensajesL': mensajesL,
            'nombresL':nombresL,
            'usuariosL':usuariosL,
            'mensajesN': mensajesN,
            'nombresN': nombresN,
            'usuariosN': usuariosN
        }
    else:
        data={
            'mensajes':None,
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
    personal = Usuario.objects.all()
    print personal
    form = ComentarioForm(request.POST or None)
    data = {
        'personal': personal,
        'form': form,
    }
    if form.is_valid():
        para = form.cleaned_data["Destino"]
        print "######"
        print para
        to_user=para.usuario

        Inbox.send_message(request.user, to_user, form.cleaned_data["mensaje"])
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
