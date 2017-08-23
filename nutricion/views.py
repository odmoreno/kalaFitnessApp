# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.http import JsonResponse
from kalaapp.decorators import rol_required
from paciente.models import Paciente, PacientePersonal
from personal.models import Personal
from .models import ficha_nutricion, HorarioNut
from .forms import FichaForm, HorariosForm

def index(request):
    template = "nutricion/index.html"
    return render(request, template, { 'nutricionista': True})

@transaction.atomic
def crear_ficha(request):
    template = "nutricion/crear-ficha.html"
    form = FichaForm(request.POST or None)
    pacientes = Paciente.objects.all()
    sesion = request.session.get('user_sesion', None)
    #p = PacientePersonal.objects.filter(personal=sesion.get('personal__id', 0))
    print  sesion
    print sesion.get('personal__id', 0)
    print form._errors
    if form.is_valid():
        ficha = form.save(commit=False)
        print request.POST.get('paciente')
        paciente_id = request.POST.get('paciente')
        paciente = get_object_or_404(Paciente, pk=paciente_id)
        personal = get_object_or_404(Personal, pk=sesion.get('personal__id', 0))
        print personal
        ficha.paciente = paciente
        ficha.personal = personal
        ficha.save()
        return HttpResponseRedirect("/nutricion/ficha/lista/")
    context = {
        'form': form,
        'nutricionista': True,
        "pacientes": pacientes
    }
    return render(request, template, context)


def listar_fichas(request):
    template = "nutricion/listar-fichas.html"
    pacientes = Paciente.objects.all()
    fichas = ficha_nutricion.objects.all()
    context = {
        'fichas': fichas,
        "pacientes": pacientes
    }
    return render(request, template, context)

@transaction.atomic
def eliminar_ficha(request, ficha_id):
    ficha = ficha_nutricion.objects.get(pk=ficha_id)
    ficha.delete()
    return HttpResponseRedirect("/nutricion/ficha/lista/")

@transaction.atomic
def editar_ficha(request, ficha_id):

    ficha_nutri = get_object_or_404(ficha_nutricion, pk=ficha_id)
    template = "nutricion/crear-ficha.html"
    form = FichaForm(request.POST or None, instance=ficha_nutri)
    pacientes = Paciente.objects.all()
    sesion = request.session.get('user_sesion', None)
    if form.is_valid():
        ficha = form.save(commit=False)
        paciente_id = request.POST.get('paciente')
        paciente = get_object_or_404(Paciente, pk=paciente_id)
        personal = get_object_or_404(Personal, pk=sesion.get('personal__id', 0))
        ficha.paciente = paciente
        ficha.personal = personal
        ficha.save()
        return HttpResponseRedirect("/nutricion/ficha/lista/")
    context = {
        'form': form,
        'ficha': ficha_nutri,
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
    template = 'nutricion/ficha-detalle.html'
    ficha = get_object_or_404(ficha_nutricion, pk=ficha_id)
    form = FichaForm(request.POST or None, instance=ficha)
    contexto['form'] = form
    contexto['ficha'] = ficha
    contexto['paciente'] = ficha.paciente
    return render(request, template_name=template, context=contexto)


@transaction.atomic
def establecer_horario (request):
    template= 'nutricion/crear-horario.html'
    form = HorariosForm(request.POST or None)
    sesion = request.session.get('user_sesion', None)
    print form._errors
    if form.is_valid():
        horario = form.save(commit=False)
        personal = get_object_or_404(Personal, pk=sesion.get('personal__id', 0))
        horario.personal = personal
        horario.save()
        return HttpResponseRedirect("/nutricion/horario/ver/")
    context ={
        "form" : form
    }
    return render(request, template, context)

def ver_horarios(request):
    template = "nutricion/listar-horarios.html"
    horarios = HorarioNut.objects.all()
    context = {
        "horarios": horarios,
    }
    return render(request, template, context)

'''
Funcion: reporteTotal
Entradas: request
Salidas: JSON con los datos de todas las facturas

Funcion que permite obtener todas las facturas creadas
'''
#@login_required
def reporteByCedula(request, cedula):
    fichas = ficha_nutricion.objects.all()
    pacientes = Paciente.objects.all()

    #records = []

    for paciente in pacientes:
        if paciente.usuario.cedula == cedula:
            nombre = paciente.usuario.nombre
            apellido = paciente.usuario.apellido
            paciente_id = paciente.usuario.id

            obj = {"nombre": nombre, "apellido": apellido, "id": paciente_id, "fichas": []}

            for ficha in fichas:
                if ficha.paciente.usuario.id == paciente_id:
                    proteina = ficha.proteina
                    grasas = ficha.grasas
                    carbohidratos =  ficha.carbohidratos
                    dieta = ficha.dieta
                    record = {"proteina": proteina, "grasas": grasas, "carbohidratos": carbohidratos, "dieta": dieta}
                    obj['fichas'].append(record)
            return JsonResponse(obj)
'''
Funcion: reportes
Entradas: requerimiento get http
Salidas: Retorna un template de reportes de ficha medica
'''
#@login_required
def reportes(request):
    template = 'nutricion/reportes.html'
    return render(request, template)

@transaction.atomic
def eliminar_cita(request, horario_id):
    cita = HorarioNut.objects.get(pk=horario_id)
    cita.delete()
    return HttpResponseRedirect("/nutricion/horario/ver/")
