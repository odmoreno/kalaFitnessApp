# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from kala.views import enviar_password_email, generar_password
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
from django.contrib import messages as me
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
        #user.set_password('1234')
        password = generar_password()
        user.set_password(password)
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
        enviar_password_email(user.email, user.username, password)
        #all_personal = Usuario.objects.filter(estado="A")
        #return render(request, 'personal/index.html', {'all_personal': all_personal})
        me.add_message(request, m.SUCCESS, 'Personal creado con exito!')
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
    user=personal.usuario
    form.fields["email"].initial = user.email

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
        me.add_message(request, me.SUCCESS, 'Personal editado con exito!')
        #all_personal = Usuario.objects.filter(estado="A")
        #return render(request, 'personal/index.html', {'all_personal': all_personal})
        return redirect('personal:index')

    context = {
        "form": form,
        "editar": True,
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
    mensajes=Message.objects.filter(recipient=request.user)
    print mensajes
    if mensajes is not None:
        nombresL = []
        nombresN = []
        usuariosL = []
        usuariosN = []
        mensajesL = []
        mensajesN = []
        for m in mensajes:
            if m.read_at == None:
                try:
                    print "entro"
                    usuario=Usuario.objects.get(usuario=m.sender)
                    nombre = usuario.nombre + " " + usuario.apellido
                    nombresN.append(nombre)
                    usuariosN.append(usuario)
                    mensajesN.append(m)
                except:
                    print "entro2"
                    usuario= Usuario()
                    usuario.estado="I"
                    usuario.usuario=m.sender
                    usuario.nombre="Administrador"
                    usuario.apellido="Kala"
                    usuario.cedula="0922658845"
                    rol = Rol.objects.filter(tipo='administrador').first()
                    usuario.rol=rol
                    usuario.save()
                    nombre = usuario.nombre + " " + usuario.apellido
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
    Inbox.read_message(mensaje_id)
    user=User.objects.get(id=message.sender.id)
    usuarioN=Usuario.objects.get(usuario=user)
    if usuarioN.rol.tipo == "administrador" or usuarioN.rol.tipo == "nutricionista" or usuarioN.rol.tipo == "fisioterapista":
        espersonal=True
    else:
        espersonal=False
    nombre=usuarioN.nombre + " " + usuarioN.apellido
    data={
        'sender':nombre,
        'mensaje':message.content,
        'personal':espersonal

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

        try:
            Inbox.send_message(request.user, to_user, form.cleaned_data["mensaje"])
            me.add_message(request, me.SUCCESS, 'Mensaje Enviado con exito!')
        except:
            me.add_message(request, me.WARNING, 'Mensaje No pudo ser enviado!')
        mensajes = Message.objects.filter(recipient=request.user)
        print mensajes
        if mensajes is not None:
            nombresL = []
            nombresN = []
            usuariosL = []
            usuariosN = []
            mensajesL = []
            mensajesN = []
            for m in mensajes:
                if m.read_at == None:
                    try:
                        usuario = Usuario.objects.get(usuario=m.sender)
                        nombre = usuario.nombre + " " + usuario.apellido
                        nombresN.append(nombre)
                        usuariosN.append(usuario)
                        mensajesN.append(m)
                    except:
                        usuario = Usuario()
                        usuario.estado = "I"
                        usuario.usuario = m.sender
                        usuario.nombre = "Administrador"
                        usuario.apellido = "Kala"
                        usuario.cedula = "0922658845"
                        rol = Rol.objects.filter(tipo='administrador').first()
                        usuario.rol = rol
                        usuario.save()
                        nombre = usuario.nombre + " " + usuario.apellido
                        nombresN.append(nombre)
                        usuariosN.append(usuario)
                        mensajesN.append(m)

                else:
                    usuario = Usuario.objects.get(usuario=m.sender)
                    nombre = usuario.nombre + " " + usuario.apellido
                    nombresL.append(nombre)
                    usuariosL.append(usuario)
                    mensajesL.append(m)

            data = {
                'mensajesL': mensajesL,
                'nombresL': nombresL,
                'usuariosL': usuariosL,
                'mensajesN': mensajesN,
                'nombresN': nombresN,
                'usuariosN': usuariosN
            }
        return render(request, "personal/mensajes.html", data)

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
        to_user=to.usuario
        print to_user
        try:
            Inbox.send_message(request.user, to_user, form.cleaned_data["mensaje"])
            me.add_message(request, me.SUCCESS, 'Mensaje Enviado con exito!')
        except:
            me.add_message(request, me.WARNING, 'Mensaje No pudo ser enviado!')

        mensajes = Message.objects.filter(recipient=request.user)
        print mensajes
        if mensajes is not None:
            nombresL = []
            nombresN = []
            usuariosL = []
            usuariosN = []
            mensajesL = []
            mensajesN = []
            for m in mensajes:
                if m.read_at == None:
                    try:
                        print "entro"
                        usuario = Usuario.objects.get(usuario=m.sender)
                        nombre = usuario.nombre + " " + usuario.apellido
                        nombresN.append(nombre)
                        usuariosN.append(usuario)
                        mensajesN.append(m)
                    except:
                        print "entro2"
                        usuario = Usuario()
                        usuario.estado = "I"
                        usuario.usuario = m.sender
                        usuario.nombre = "Administrador"
                        usuario.apellido = "Kala"
                        usuario.cedula = "0922658845"
                        rol = Rol.objects.filter(tipo='administrador').first()
                        usuario.rol = rol
                        usuario.save()
                        nombre = usuario.nombre + " " + usuario.apellido
                        nombresN.append(nombre)
                        usuariosN.append(usuario)
                        mensajesN.append(m)

                else:
                    usuario = Usuario.objects.get(usuario=m.sender)
                    nombre = usuario.nombre + " " + usuario.apellido
                    nombresL.append(nombre)
                    usuariosL.append(usuario)
                    mensajesL.append(m)

            data = {
                'mensajesL': mensajesL,
                'nombresL': nombresL,
                'usuariosL': usuariosL,
                'mensajesN': mensajesN,
                'nombresN': nombresN,
                'usuariosN': usuariosN
            }

        return render(request, "personal/mensajes.html", data)
    else:
        form=ComentarioPersonalForm()

    return render(request, "personal/nuevoMensajePersonal.html", data)


'''
Funcion: reporteTotal
Entradas: requerimiento get http
Salidas: JSON con todo el personal
*Funcion que retorna la informacion del personal registrados en la base de datos
en forma de un JSON*
'''

#personalCache = []

@login_required
def reporteTotal(request):
    #global personalCache
    #if len(personalCache) == 0:
    personal = Personal.objects.all()
    #    personalCache = personal
    #    print "desde la base"
    #else:
    #    personal = personalCache
    #    print "desde el cache"


    #personal = Personal.objects.all()
    per = []

    for p in personal:
        if p.usuario.estado=='A':
            cedula = str(p.usuario.cedula)
            nombre = p.usuario.nombre
            apellido = p.usuario.apellido
            telefono = p.usuario.telefono
            rol = p.usuario.rol.tipo
            genero = p.usuario.genero
            record = {
                "cedula":cedula,
                "nombre":nombre,
                "apellido":apellido,
                "telefono":telefono,
                "rol":rol,
                "genero":genero
            }
            per.append(record)

    return JsonResponse({"data": per})


'''
Funcion: reporteRol
Entradas: requerimiento get http
Salidas: JSON con todo el personal filtrado por rol
*Funcion que retorna la informacion del personal registrados en la base de datos
en forma de un JSON*
'''
@login_required
def reporteRol(request):
    personal = Personal.objects.all()
    per = []

    for p in personal:
        if p.usuario.rol.tipo=='fisioterapista' and p.usuario.estado=='A':
            cedula = str(p.usuario.cedula)
            nombre = p.usuario.nombre
            apellido = p.usuario.apellido
            telefono = p.usuario.telefono
            ##genero = p.usuario.genero
            rol = p.usuario.rol.tipo
            record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"rol":rol}
            per.append(record)

    return JsonResponse({"data": per})


'''
Funcion: reporteMujeres
Entradas: requerimiento get http
Salidas: JSON con todo el personal filtrado por genero femenino
*Funcion que retorna la informacion del personal registrados en la base de datos
en forma de un JSON*
'''
@login_required
def reporteMujeres(request):
    personal = Personal.objects.all()
    per = []

    for p in personal:
        if p.usuario.genero=='F' and p.usuario.estado=='A':
            cedula = str(p.usuario.cedula)
            nombre = p.usuario.nombre
            apellido = p.usuario.apellido
            telefono = p.usuario.telefono
            ##genero = p.usuario.genero
            rol = p.usuario.rol.tipo
            record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"rol":rol}
            per.append(record)

    return JsonResponse({"data": per})

'''
Funcion: reporteHombres
Entradas: requerimiento get http
Salidas: JSON con todo el personal filtrado por genero hombres
*Funcion que retorna la informacion del personal registrados en la base de datos
en forma de un JSON*
'''
@login_required
def reporteHombres(request):
    personal = Personal.objects.all()
    per = []

    for p in personal:
        if p.usuario.genero=='M' and p.usuario.estado=='A':
            cedula = str(p.usuario.cedula)
            nombre = p.usuario.nombre
            apellido = p.usuario.apellido
            telefono = p.usuario.telefono
            ##genero = p.usuario.genero
            rol = p.usuario.rol.tipo
            record = {"cedula":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"rol":rol}
            per.append(record)

    return JsonResponse({"data": per})


'''
Funcion: reportes
Entradas: requerimiento get http
Salidas: template de reportes de personal
'''
@login_required
def reportes(request):
    template = 'personal/reportes.html'
    response = render(request, template)
    response['Cache-Control'] = "private,max-age=600"
    return response
