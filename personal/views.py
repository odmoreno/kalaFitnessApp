# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from kalaapp.models import Usuario, Rol
from paciente.models import Paciente
from .forms import  UsuarioForm, PersonalForm, ComentarioForm, PersonalEditForm, ComentarioPersonalForm
from personal.models import Personal
#from paciente.views import paciente
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from directmessages.apps import Inbox
from directmessages.models import Message

@login_required
def index(request):
    all_personal = Usuario.objects.filter(estado="A")
    return render(request, 'personal/index.html', {'all_personal': all_personal})

@login_required
def eliminarPersonal(request, personal_id):
    personal = Usuario.objects.get(pk=personal_id)
    # user=personal.usuario
    # user.delete()
    personal.estado="I"
    personal.save()
    all_personal = Usuario.objects.filter(estado="A")
    #return HttpResponse({"message": "Se elimino el personal" + personal_id}, content_type="application/json")
    return render(request, 'personal/index.html', {'all_personal': all_personal})

@login_required
@transaction.atomic
def nuevoPersonal(request):
    form = PersonalForm(request.POST or None)
    if form.is_valid():
        usuario= form.save(commit=False)
        user = User()
        user.username = form.cleaned_data['cedula']
        user.set_password('1234')
        user.email = form.cleaned_data['email']
        user.save()
        if form.cleaned_data["ocupacion"]== "1":
            rol = Rol.objects.get(tipo='fisioterapista')

        else:
            rol = Rol.objects.get(tipo='nutricionista')

        usuario.usuario = user
        usuario.rol = rol
        usuario.save()
        personal=Personal()
        personal.usuario=usuario
        personal.save()
        all_personal = Usuario.objects.filter(estado="A")
        return render(request, 'personal/index.html', {'all_personal': all_personal})

    context = {
        "form": form,
    }
    return render(request, 'personal/form_personal.html', context)

@login_required
@transaction.atomic
def editarPersonal(request, personal_id):
    personal = get_object_or_404(Usuario, pk=personal_id)

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

@login_required
def detallePersonal(request, personal_id):
    personal = get_object_or_404(Usuario, pk=personal_id)
    return render(request, 'personal/detalles.html', {'personal': personal})

@login_required
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

@login_required
def leerMensaje(request, mensaje_id):
    message=Message.objects.get(id=mensaje_id)
    Inbox.read_message(message)
    user=User.objects.get(id=message.sender.id)
    usuarioN=Usuario.objects.get(usuario=user)
    nombre=usuarioN.nombre + " " + usuarioN.apellido
    data={
        'sender':nombre,
        'mensaje':message.content,

    }
    return render(request, "personal/leerMensaje.html", data)

@login_required
def nuevoMensajePaciente(request):
    Paciente = Usuario.objects.all()

    form = ComentarioForm(request.POST or None)
    data = {
        'personal': Paciente,
        'form': form,
    }
    if form.is_valid():
        para = form.cleaned_data["Destino"]
        print para
        print form
        to = Usuario.objects.get(pk=para)
        print to
        to_user=to.usuario

        Inbox.send_message(request.user, to_user, form.cleaned_data["mensaje"])
        return render(request, "personal/mensajes.html")

    return render(request, "personal/nuevoMensaje.html", data)

def nuevoMensajePersonal(request):
    personal = Usuario.objects.all()
    form = ComentarioPersonalForm(request.POST or None)
    data = {
        'personal': personal,
        'form': form,
    }
    if form.is_valid():
        para = form.cleaned_data["Destino"]
        print para
        print form
        to = Usuario.objects.get(pk=para)
        print to
        to_user=to.usuario

        Inbox.send_message(request.user, to_user, form.cleaned_data["mensaje"])
        return render(request, "personal/mensajes.html")

    return render(request, "personal/nuevoMensaje.html", data)

@login_required
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

@login_required
def reportePDF(request):
    template = 'personal/reportePDF.html'
    return render(request, template)
