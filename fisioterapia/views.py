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
from django.http import JsonResponse
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

@transaction.atomic
def establecer_horario (request):
    template= 'fisioterapia/crear-horario.html'
    form = HorariosForm(request.POST or None)
    sesion = request.session.get('user_sesion', None)
    print form._errors
    if form.is_valid():
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