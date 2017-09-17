# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from kalaapp.models import Usuario, Rol
from paciente.models import Paciente
from personal.models import Personal
from fisioterapia.models import Ficha , Horario
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse, HttpResponseServerError, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from directmessages.apps import Inbox
from directmessages.models import Message
from .forms import FichaForm, HorariosForm


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
    #global fichasCache
    #if len(fichasCache) == 0:
    fichas = Ficha.objects.all()
    #    fichasCache = fichas
    #    print "desde la base"
    #else:
    #    fichas = fichasCache
    #    print "desde el cache"

    template = "fisioterapia/lista-fichas.html"
    #fichas = Ficha.objects.all()
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

'''
Funcion: detalleFichas
Entradas: requerimiento e Identificador de la ficha a ser visualizada
Salidas:Template para renderizacion
*Funcion que recibe el id de una ficha que debe ser visualizada, y muestra su informacion.*
'''

def detalleFicha(request, ficha_id):
    contexto = {}
    ficha = None
    template = None
    paciente = None
    template = 'fisioterapia/ficha-detalle.html'
    ficha = get_object_or_404(Ficha, pk=ficha_id)
    form = FichaForm(request.POST or None, instance=ficha)
    contexto['form'] = form
    contexto['ficha'] = ficha
    contexto['paciente'] = ficha.paciente
    return render(request, template_name=template, context=contexto)

@transaction.atomic
def establecer_horario (request):
    template= 'fisioterapia/crear-horario.html'
    form = HorariosForm(request.POST or None)
    sesion = request.session.get('user_sesion', None)
    print form._errors
    if form.is_valid():
#        lel = lel.replace(minute=form.cleaned_data['hora'].minute + duracion)
        horario = form.save(commit=False)
        personal = get_object_or_404(Personal, pk=sesion.get('personal__id', 0))
        horario.personal = personal
        horario.save()
        return HttpResponseRedirect("/fisioterapia/horario/ver/")
    context ={
        "form" : form
    }
    return render(request, template, context)

def ver_horarios(request):
    template = "fisioterapia/listar-horarios.html"
    horarios = Horario.objects.all()
    context = {
        "horarios": horarios,
    }
    return render(request, template, context)

@transaction.atomic
def eliminar_cita(request, horario_id):
    cita = Horario.objects.get(pk=horario_id)
    cita.delete()
    return HttpResponseRedirect("/fisioterapia/horario/ver/")

'''
Funcion: reporteTotal
Entradas: paciente_cedula, la cedula del paciente
Salidas: JSON con una ficha medica del paciente
*Funcion que retorna la informacion de las fichas de un paciente de la base de datos
en forma de un JSON*
'''

#fichasCache = []

@login_required
def reporteFicha(request, paciente_cedula):
    #global fichasCache
    try:
        #if len(fichasCache) == 0:
        fichas = Ficha.objects.all()
        #    fichasCache = fichas
        #    print "desde la base"
        #else:
        #    fichas = fichasCache
        #    print "desde el cache"

        for f in fichas:
            if f.paciente.usuario.cedula==paciente_cedula: #and paciente.usuario.estado=='A':
                cedula = f.paciente.usuario.cedula
                nombre = f.paciente.usuario.nombre
                apellido = f.paciente.usuario.apellido
                genero = f.paciente.usuario.genero
                altura = f.altura
                peso = f.peso
                imc = f.imc
                musculo = f.musculo
                grasa_visceral = f.grasa_visceral
                grasa_porcentaje = f.grasa_porcentaje

                flexiones = f.flexiones
                sentadillas = f.sentadillas
                saltoLargo = f.saltoLargo
                suspension = f.suspension

                abdomen_bajo = f.abdomen_bajo
                abdomen_alto = f.abdomen_alto
                espinales = f.espinales
                lumbares = f.lumbares
                trenSuperior = f.trenSuperior

                record = {
                    "cedula": cedula,
                    "apellido":apellido,
                    "nombre":nombre,
                    "genero":genero,
                    "altura": altura,
                    "peso": peso,
                    "imc": imc,
                    "musculo": musculo,
                    "grasa_visceral": grasa_visceral,
                    "grasa_porcentaje" : grasa_porcentaje,
                    "flexiones" : flexiones,
                    "sentadillas" : sentadillas,
                    "saltoLargo" : saltoLargo,
                    "suspension" : suspension,
                    "abdomen_bajo" :abdomen_bajo,
                    "abdomen_alto" :abdomen_alto,
                    "espinales" :espinales,
                    "lumbares" :lumbares,
                    "trenSuperior" :trenSuperior
                }
                return JsonResponse({"data": record})
        return HttpResponseNotFound("No existen reportes de este paciente")
    except Exception as e:
        print e
        return HttpResponseServerError("Algo salio mal")

'''
Funcion: reporteTotal
Entradas: paciente_cedula, la cedula del paciente
Salidas: JSON con una ficha medica del paciente
*Funcion que retorna la informacion de las fichas de un paciente de la base de datos
en forma de un JSON*
'''
@login_required
def reporte(request):
    #global fichasCache
    pacientes = []

    try:
        #if len(fichasCache) == 0:
        fichas = Ficha.objects.all()
        #    fichasCache = fichas
        #    print "desde la base"
        #else:
        #    fichas = fichasCache
        #    print "desde el cache"


        for fic in fichas:
            cedula = fic.paciente.usuario.cedula
            nombre = fic.paciente.usuario.nombre
            apellido = fic.paciente.usuario.apellido
            genero = fic.paciente.usuario.genero
            ocupacion = fic.paciente.usuario.ocupacion

            paciente = {
                "cedula": cedula,
                "apellido":apellido,
                "nombre":nombre,
                "genero":genero,
                "ocupacion": ocupacion,
                "data": []
            }

            if paciente not in pacientes:
                pacientes.append(paciente)


        for f in fichas:
            altura = f.altura
            peso = f.peso
            imc = f.imc
            musculo = f.musculo
            grasa_visceral = f.grasa_visceral
            grasa_porcentaje = f.grasa_porcentaje
            cuello = f.cuello
            hombros = f.hombros
            pecho = f.pecho
            brazo_derecho = f.brazo_derecho
            brazo_izquierdo = f.brazo_izquierdo
            antebrazo_derecho = f.antebrazo_derecho
            antebrazo_izquierdo = f.antebrazo_izquierdo
            cintura = f.cintura
            cadera = f.cadera
            muslo_derecho = f.muslo_derecho
            muslo_izquierdo = f.muslo_izquierdo
            pantorrilla_derecha = f.pantorrilla_derecha
            pantorrilla_izquierda = f.pantorrilla_izquierda


            flexiones = f.flexiones
            sentadillas = f.sentadillas
            saltoLargo = f.saltoLargo
            suspension = f.suspension
            abdomen_bajo = f.abdomen_bajo
            abdomen_alto = f.abdomen_alto
            espinales = f.espinales
            lumbares = f.lumbares
            trenSuperior = f.trenSuperior
            trenInferior = f.trenInferior

            ficha = {
                "altura" : altura,
                "peso" : peso,
                "imc" : imc,
                "musculo" : musculo,
                "grasa_visceral" : grasa_visceral,
                "grasa_porcentaje" : grasa_porcentaje,
                "cuello" : cuello,
                "hombros" : hombros,
                "pecho" : pecho,
                "brazo_derecho" : brazo_derecho,
                "brazo_izquierdo" : brazo_izquierdo,
                "antebrazo_derecho" : antebrazo_derecho,
                "antebrazo_izquierdo" : antebrazo_izquierdo,
                "cintura" : cintura,
                "cadera" : cadera,
                "muslo_derecho" : muslo_derecho,
                "muslo_izquierdo" : muslo_izquierdo,
                "pantorrilla_derecha" : pantorrilla_derecha,
                "pantorrilla_izquierda" : pantorrilla_izquierda
            }

            estado_fisico = {
                "flexiones" : flexiones,
                "sentadillas" : sentadillas,
                "saltoLargo" : saltoLargo,
                "suspension" : suspension,
                "abdomen_bajo" : abdomen_bajo,
                "abdomen_alto" : abdomen_alto,
                "espinales" : espinales,
                "lumbares" : lumbares,
                "trenSuperior" : trenSuperior,
                "trenInferior" : trenInferior
            }

            for paciente in pacientes:
                if f.paciente.usuario.cedula==paciente["cedula"]:
                    paciente["data"].append({"ficha":ficha, "estado_fisico":estado_fisico})

        return JsonResponse({"pacientes": pacientes})
    except Exception as e:
        print e
        return HttpResponseServerError("Algo salio mal")


'''
Funcion: reportes
Entradas: requerimiento get http
Salidas: Retorna un template de reportes de fichas
'''
@login_required
def reportes(request):
    template = 'fisioterapia_reportes.html'
    response = render(request, template)
    response['Cache-Control'] = "private,max-age=600"
    return response
