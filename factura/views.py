# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from factura.models import Facturas
from kalaapp.models import Empresa, Usuario
from paciente.models import Paciente
from django.db.models.functions import Concat
from django.db.models import Value
from django.db import transaction
from django.urls.base import reverse

# Create your views here.
def facturas(request):
    template = 'factura/crear.html'
    contexto={}
    contexto['facturas'] = Facturas.objects.filter(estado='A')

    return render(request, template_name=template, context=contexto)


@transaction.atomic
def crearFactura(request):
    template = 'factura/crear.html'
    contexto={}

    if request.method == 'POST':

        factura = Facturas()
        factura.empresa = Empresa.objects.get(pk=request.POST['empresa'])
        factura.paciente = Paciente.objects.get(pk=request.POST['paciente'])
        factura.serie = request.POST['serie']
        factura.fecha_vencimiento = request.POST['fecha_vencimiento']
        factura.subtotal = request.POST['subtotal']
        factura.total = request.POST['total']
        factura.save()

        if factura.id is not None:
            contexto['mensaje'] = 'Factura creada con exito!'
            return HttpResponseRedirect(redirect_to=reverse('facturas'), content=contexto)
        else:
            factura = None
            contexto['mensaje'] = 'Error al grabar!'

    empresas = Empresa.objects.filter(estado='A') \
        .values_list('pk', 'nombre') \
        .order_by('nombre')
    pacientes = Paciente.objects.filter(estado='A') \
        .values_list('pk', 'usuario__nombre', 'usuario__apellido') \
        .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
        .values_list('pk', 'nombre_completo') \
        .order_by('nombre_completo')

    contexto['empresas'] = empresas
    contexto['pacientes'] = pacientes
    return render(request, template_name=template, context=contexto)

@transaction.atomic
def eliminarFactura(request, facturaId=0):
    template='factura/eliminar.html'
    contexto = {}

    if request.method == 'POST':
        facturaEliminada = Facturas.objects.get(id=facturaId)

        if facturaEliminada and facturaEliminada.estado == 'A':
            facturaEliminada.estado = 'I'
            facturaEliminada.save()
            contexto['mensaje'] = 'Factura elminada con exito!'
        else:
            contexto['mensaje'] = 'Factura no encontrada'

    facturas = Facturas.objects.filter(estado='A')
    contexto['facturas'] = facturas
    return render(request, template_name=template, context=contexto)
