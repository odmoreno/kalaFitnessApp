# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from kalaapp.models import Usuario, Rol
from paciente.models import Paciente
from personal.models import Personal
from fisioterapia.models import Ficha
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from directmessages.apps import Inbox
from directmessages.models import Message
from .forms import FichaForm


from django.shortcuts import render
from forms import ComentarioForm

def index(request):
    template = "fisioterapia/lista-fichas.html"
    fichas = Ficha.objects.all()
    context = {
        "fichas": fichas,
        'fisioterapia': True
    }
    return render(request, template, context)

@transaction.atomic
def crear_ficha(request):
    template = "fisioterapia/ficha-temp.html"
    form = FichaForm(request.POST or None)
    pacientes = Paciente.objects.all()
    sesion = request.session.get('user_sesion', None)

    print form._errors
    if form.is_valid():
        ficha = form.save(commit=False)
        print request.POST.get('paciente')
        paciente_id = request.POST.get('paciente')
        paciente = get_object_or_404(Paciente, pk=paciente_id)
        ficha.paciente = paciente
        personal = get_object_or_404(Personal, pk=sesion.get('personal__id', 0))
        ficha.personal = personal
        ficha.save()
        return HttpResponseRedirect("/fisioterapia/ficha/lista/")
    context = {
        "form": form, "pacientes": pacientes,
        'fisioterapia': True
    }
    return render(request, template, context)

def listar_fichas(request):

    template = "fisioterapia/lista-fichas.html"
    fichas = Ficha.objects.all()
    print fichas
    for ficha in fichas:
        print ficha
        print ficha.paciente.usuario.nombre
        print ficha.paciente_id
        print ficha.paciente

    context = {
        "fichas": fichas,
        'fisioterapia': True
    }
    return render(request, template, context)


@transaction.atomic
def eliminar_ficha(request, ficha_id):
    ficha = Ficha.objects.get(pk=ficha_id)
    ficha.delete()
    return HttpResponseRedirect("/fisioterapia/ficha/lista/")

@transaction.atomic
def editar_ficha(request, ficha_id):

    ficha_fisio = get_object_or_404(Ficha, pk=ficha_id)
    template = "fisioterapia/ficha-temp.html"
    form = FichaForm(request.POST or None, instance=ficha_fisio)
    pacientes = Paciente.objects.all()
    sesion = request.session.get('user_sesion', None)
    if form.is_valid():
        ficha = form.save(commit=False)
        paciente_id = request.POST.get('paciente')
        paciente = get_object_or_404(Paciente, pk=paciente_id)
        print "ABC", paciente, sesion.get('personal__id', 0)
        #
        #
        #

        personal = get_object_or_404(Personal, pk=sesion.get('personal__id', 0))
        ficha.paciente = paciente
        ficha.personal = personal
        ficha.save()
        return HttpResponseRedirect("/fisioterapia/ficha/lista/")
    context = {
        'form': form,
        'ficha': ficha_fisio,
        'flag': True,
        "pacientes": pacientes
    }
    return render(request, template, context)


def verMensajes(request, personal_id=None):
    template= 'fisioterapia/mensajes.html'

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

    data={}
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
    return render(request, "fisioterapia/leerMensaje.html", data)


###CORREGIR###
def nuevoMensaje(request):
    personal= Usuario.objects.all()
    print personal
    form=ComentarioForm(request.POST or None)
    data={
        'personal':personal,
        'form':form,
    }
    if form.is_valid():
        para=form.cleaned_data["Destino"]
        to_user=para[0].usuario.usuario

        Inbox.send_message(request.user, to_user, form.cleaned_data["comentario"])
        return render(request, "fisioterapia/mensajes.html")

    return render(request, "fisioterapia/nuevoMensaje.html", data)

