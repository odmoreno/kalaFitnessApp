# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from kalaapp.models import Usuario, Rol
from personal.models import Personal
from paciente.views import Paciente
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from directmessages.apps import Inbox
from directmessages.models import Message


from django.shortcuts import render
from forms import ComentarioForm

# Create your views here.
def index(request):
    template="fisioterapia/index.html"
    '''
    
    Aqui van los datos que se quieran mostrar en el index de fisioterapia
    
    '''
    return render(request, 'fisioterapia/index.html')


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
    if request.method == 'POST':
        return render(request, "fisioterapia/mensajes.html")

    return render(request, "fisioterapia/nuevoMensaje.html", data)
