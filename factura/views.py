'''
MODULO Factura

VERSION 1.0.0

ACTUALIZADO EN 20/06/2017

'''

from __future__ import unicode_literals

from datetime import date

from django.contrib import messages
from django.db import transaction
from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render, redirect

from factura.models import Facturas
from kalaapp.models import Empresa
from kalaapp.views import paginar
from paciente.models import Paciente

'''
Funcion: listarFacturas
Entradas: request
Salidas: HttpResponse con template factura.ntml y la lista de todas las facturas creadas

Funcion que retorna todas las facturas leidas desde la base de datos
'''
def listarFacturas(request):
    template = 'factura_listar.html'
    contexto={}

    facturas = Facturas.objects.filter(estado='A')\
                .values('id', 'empresa__nombre', 'paciente_id', 'paciente__usuario__apellido',\
                'paciente__usuario__nombre', 'serie', 'fecha_vencimiento', 'total')\
                .order_by('id')

    contexto['facturas'] =  paginar(request, facturas)
    return render(request, template_name=template, context=contexto)


'''
Funcion: crearFactura
Entradas: request
Salidas: - HttpResponse con template crear.ntml y la lista de todas las empresas y pacientes

Funcion que permite crear una factura
'''
@transaction.atomic
def crearFactura(request):
    template = 'factura_crear.html'
    contexto={}

    if request.method == 'POST':
        factura = getFactura(request)

        if factura is not None:
            messages.add_message(request, messages.SUCCESS, 'Factura creada con exito!')
        return redirect('factura:ListarFacturas')

    empresas = Empresa.objects.filter(estado='A') \
        .values('id', 'nombre') \
        .order_by('nombre')
    pacientes = Paciente.objects.filter(estado='A') \
        .values('id', 'usuario__nombre', 'usuario__apellido') \
        .annotate(nombre_completo=Concat('usuario__apellido', Value(' '), 'usuario__nombre')) \
        .order_by('id', 'nombre_completo')

    contexto['empresas'] = empresas
    contexto['pacientes'] = pacientes
    contexto['hoy'] = date.today()
    return render(request, template_name=template, context=contexto)

'''
Funcion: getFactura
Entradas: - request
Salidas:  - nueva factura

Funcion que retorna una nueva factura con los datos ingresados en formulario
'''
def getFactura(request):
    try:
        factura = Facturas()
        factura.empresa = Empresa.objects.get(id=request.POST.get('empresa', 0))
        factura.paciente = Paciente.objects.get(id=request.POST.get('paciente', 0))
        factura.serie = request.POST.get('serie')
        factura.fecha_vencimiento = request.POST.get('fecha_vencimiento')
        factura.total = request.POST.get('total')
        factura.save()
    except Exception, e:
        messages.add_message(request, messages.WARNING, 'Error inesperado! ' + str(e))
        return None
    return factura

'''
Funcion: crearFactura
Entradas: - request
          - id: id de la factura a eliminar
Salidas: ninguna

Funcion que permite eliminar una factura existente
'''
@transaction.atomic
def eliminarFactura(request, id=0):
    template='factura_listar.html'
    contexto = {}

    if request.method == 'POST':
        try:
            facturaEliminada = Facturas.objects.get(id=id)

            if facturaEliminada and facturaEliminada.estado == 'A':
                facturaEliminada.estado = 'I'
                facturaEliminada.save()
                messages.add_message(request, messages.SUCCESS, 'Factura eliminada con exito!')
            else:
                messages.add_message(request, messages.WARNING, 'Factura no encontrada o ya eliminada')
        except:
            messages.add_message(request, messages.WARNING, 'Factura no encontrada o ya eliminada')

        return redirect('factura:ListarFacturas')

'''
Funcion: crearFactura
Entradas: request
Salidas: HttpResponse con template factura.ntml y la lista de todas las empresas y pacientes

Funcion que permite obtener todas las facturas creadas
'''
def apiFactura(request):
    template = "factura_listar.html"
    facturas = Facturas.objects.all()
    contexto = {"facturas": facturas}
    return render(request, template_name=template, context=contexto)

