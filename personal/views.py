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
    template="personal/nuevoMensaje.html"
    personal= Personal.objects.all()
    usuarios=[]
    for p in personal:
        usuarios.append(p.usuario)
    data={
        'personal':personal,
        'usuarios':usuarios,
    }
    if request.POST:
        pass
    return(request, template, data)

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
