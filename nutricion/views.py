# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect

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

@transaction.atomic
def eliminar_cita(request, horario_id):
    cita = HorarioNut.objects.get(pk=horario_id)
    cita.delete()
    return HttpResponseRedirect("/nutricion/horario/ver/")
