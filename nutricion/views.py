# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect

from kalaapp.decorators import rol_required
from paciente.models import Paciente
from personal.models import Personal
from .models import ficha_nutricion
from .forms import FichaForm

def index(request):
    template = "nutricion/index.html"
    return render(request, template, { 'nutricionista': True})

@transaction.atomic
def crear_ficha(request):
    template = "nutricion/crear-ficha.html"
    form = FichaForm(request.POST or None)
    pacientes = Paciente.objects.all()
    sesion = request.session.get('user_sesion', None)
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

def ver_horarios(request):
    return

