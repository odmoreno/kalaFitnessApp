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
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from directmessages.apps import Inbox
from directmessages.models import Message

@login_required
def index(request):
    all_personal = Usuario.objects.filter(estado="A")
    return render(request, 'personal/index.html', {'all_personal': all_personal})
'''
Funcion: eliminarPersonal
Entradas: requerimiento e Identificador del Personal a ser eliminado
Salidas:Template para renderizacion
*Funcion que recibe el id de un personal que debe ser eliminado, y elimina su registro de
la base de datos retornando a la pagina de visualizacion de los pacientes.*

'''

@login_required
def eliminarPersonal(request, personal_id):
    personal = Usuario.objects.get(pk=personal_id)
    # user=personal.usuario
    # user.delete()
    personal.estado="I"
    personal.save()
    #all_personal = Usuario.objects.filter(estado="A")
    #return HttpResponse({"message": "Se elimino el personal" + personal_id}, content_type="application/json")
    #return render(request, 'personal/index.html', {'all_personal': all_personal})
    return redirect('personal:index')

'''
Funcion: nuevoPersonal
Entradas: requerimiento GET y POST
Salidas:Template para renderizacion junto con FORM para el registro de nuevos Personal
*Funcion que renderiza un form para el ingreso de nuevos Personales y, una vez llenado, recibe
por medio de POST los datos para generar el registro del paciente en la base de datos*

'''
@login_required
@transaction.atomic
def nuevoPersonal(request):
    form = PersonalForm(request.POST, request.FILES)
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
        usuario.foto = form.cleaned_data['foto']
        usuario.save()
        personal=Personal()
        personal.usuario=usuario
        personal.save()
        #all_personal = Usuario.objects.filter(estado="A")
        #return render(request, 'personal/index.html', {'all_personal': all_personal})
        return redirect('personal:index')

    context = {
        "form": form,
    }
    return render(request, 'personal/form_personal.html', context)

'''
Funcion: editarPersonal
Entradas: requerimiento e Identificador del Personal a ser editado
Salidas:Template para renderizacion y lista de Personal
*Funcion que recibe el id de un Personal que debe ser editado, y Muestra un formulario llenado con la info
anterior del Personal para que esta sea editada.*

'''
@login_required
@transaction.atomic
def editarPersonal(request, personal_id):
    personal = get_object_or_404(Usuario, pk=personal_id)

    form = PersonalEditForm(request.POST or None, instance=personal)

    if form.is_valid():
        user=personal.usuario
        user.email = form.cleaned_data['email']
        user.save()
        if form.cleaned_data["ocupacion"] == "1":
            rol = Rol.objects.get(tipo='fisioterapista')
        else:
            rol = Rol.objects.get(tipo='nutricionista')


        personal.rol = rol
        personal.save()
        personal = form.save()
        #all_personal = Usuario.objects.filter(estado="A")
        #return render(request, 'personal/index.html', {'all_personal': all_personal})
        return redirect('personal:index')

    context = {
        "form": form,
    }
    return render(request, 'personal/form_personal.html', context)
'''
Funcion: detallePersonal
Entradas: requerimiento e Identificador del paciente a ser visualizado
Salidas:Template para renderizacion
*Funcion que recibe el id de un Personal que debe ser visualizado, y muestra su informacion.*
'''
@login_required
def detallePersonal(request, personal_id):
    personal = get_object_or_404(Usuario, pk=personal_id)
    return render(request, 'personal/detalles.html', {'personal': personal})

'''
Funcion: verMensaje
Entradas: requerimiento
Salidas:Template para renderizacion
*Funcion que retorna una pagina con todos los mensajes cuyo destinatario es el usuario que ha iniciado sesion.*
'''
@login_required
def verMensajes(request):
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
'''
Funcion: leerMensaje
Entradas: requerimiento, id del mensaje a ser leido
Salidas:Template para renderizacion
*Funcion que permite retornar a informacion de un mensaje a ser visto por el usuario*
'''
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
'''
Funcion: nuevoMensajePaciente
Entradas: requerimiento
Salidas:Template para renderizacion con formulario de creacion de mensaje
*Funcion que permite enviar un mensaje a un paciente*
'''

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

'''
Funcion: nuevoMensajePersonal
Entradas: requerimiento
Salidas:Template para renderizacion con formulario de creacion de mensaje
*Funcion que permite enviar un mensaje a un Personal*
'''
def nuevoMensajePersonal(request):
    personal = Usuario.objects.all()
    form = ComentarioPersonalForm(request.POST or None)
    data = {
        'personal': personal,
        'form': form,
    }
    if form.is_valid():
        para = form.cleaned_data["Destino"]


        to = Usuario.objects.get(pk=para)
        #to_user=to.usuario
        to_user=User.object.get(username=to.usuario)
        print to_user

        Inbox.send_message(request.user, to_user, form.cleaned_data["mensaje"])
        return render(request, "personal/mensajes.html")
    else:
        form=ComentarioPersonalForm()

    return render(request, "personal/nuevoMensajePersonal.html", data)

@login_required
def reporteTotal(request):
    personal = Personal.objects.all()
    per = []

    for p in personal:
        cedula = str(p.usuario.cedula)
        nombre = p.usuario.nombre
        apellido = p.usuario.apellido
        telefono = p.usuario.telefono
        ##genero = p.usuario.genero
        rol = p.usuario.rol.tipo
        record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"rol":rol}
        per.append(record)

    return JsonResponse({"data": per})

@login_required
def reporteRol(request):
    personal = Personal.objects.all()
    per = []

    for p in personal:
        if p.usuario.rol.tipo=='fisioterapista':
            cedula = str(p.usuario.cedula)
            nombre = p.usuario.nombre
            apellido = p.usuario.apellido
            telefono = p.usuario.telefono
            ##genero = p.usuario.genero
            rol = p.usuario.rol.tipo
            record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"rol":rol}
            per.append(record)

    return JsonResponse({"data": per})

@login_required
def reporteMujeres(request):
    personal = Personal.objects.all()
    per = []

    for p in personal:
        if p.usuario.genero=='F':
            cedula = str(p.usuario.cedula)
            nombre = p.usuario.nombre
            apellido = p.usuario.apellido
            telefono = p.usuario.telefono
            ##genero = p.usuario.genero
            rol = p.usuario.rol.tipo
            record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"rol":rol}
            per.append(record)

    return JsonResponse({"data": per})

@login_required
def reporteHombres(request):
    personal = Personal.objects.all()
    per = []

    for p in personal:
        if p.usuario.genero=='M':
            cedula = str(p.usuario.cedula)
            nombre = p.usuario.nombre
            apellido = p.usuario.apellido
            telefono = p.usuario.telefono
            ##genero = p.usuario.genero
            rol = p.usuario.rol.tipo
            record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"rol":rol}
            per.append(record)

    return JsonResponse({"data": per})

@login_required
def reportes(request):
    template = 'personal/reportes.html'
    return render(request, template)
