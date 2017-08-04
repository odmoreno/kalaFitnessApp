# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from paciente.models import Paciente

def index(request):
    template = "nutricion/index.html"
    return render(request, template, { 'nutricionista': True})

def crear_ficha(request):
    template = "nutricion/crear-ficha.html"
    pacientes = Paciente.objects.all()
    context = {
        'nutricionista': True,
        "pacientes": pacientes
    }
    return render(request, template, context)

def listar_fichas(request):
    template = "nutricion/listar-fichas.html"
    pacientes = Paciente.objects.all()
    context = {
        'nutricionista': True,
        "pacientes": pacientes
    }
    return render(request, template, context)

def ver_horarios(request):
    return

