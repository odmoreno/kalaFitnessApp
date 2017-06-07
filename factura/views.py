# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import *
from .forms import CrearFacturaForm
from factura.models import Facturas
from kalaapp.models import Empresa, Usuario
from paciente.models import Paciente

# Create your views here.

def crearFactura(request):
    template = 'crear.html'
    empresaNombre = None
    pacienteNombre = None

    if request.method == 'POST':
        # empresaNombre = request.POST['empresa']
        # pacienteNombre = request.POST['paciente']
        # request.POST = request.POST.copy()
        # request.POST['empresa'] = Empresa.objects.get(pk=request.POST['empresa']);
        # request.POST['paciente'] = Paciente.objects.get(pk=request.POST['paciente']);
        form = CrearFacturaForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = CrearFacturaForm()

    # form.fields['empresa'].queryset = Empresa.objects.filter(pk=empresaIds)\
    #                                     .values_list('nombre', flat=True)\
    #                                     .order_by('nombre')


    # form.fields['empresa'].queryset = Empresa.objects.filter(estado='A')\
    #                                   .order_by('nombre')\
    #                                   .values_list('nombre', flat=True)
    # form.fields['paciente'].queryset = Paciente.objects.filter(estado='A') \
    #                                     .order_by('usuario__nombre') \
    #                                     .values_list('usuario__nombre', flat=True)
    #
    # form.initial = {'empresa':empresaNombre, 'paciente':pacienteNombre}
    contexto = {'form': form}
    return render(request, template_name=template, context=contexto)

def eliminarFactura(request, facturaId=0):
    template='eliminar.html'
    contexto = {'mensake':'ok'}

    if request.method == 'POST':
        facturaEliminada = Facturas.objects.get(id=facturaId)

        if facturaEliminada and facturaEliminada.estado == 'A':
            facturaEliminada.estado = 'I'
            facturaEliminada.save()
        else:
            contexto['mensaje'] = 'Factura no encontrada'

    facturas = Facturas.objects.filter(estado='A')
    contexto['facturas'] = facturas
    return render(request, template_name=template, context=contexto)












# class crearFactura(CreateView):
#     template_name = 'crear.html'
#     success_url = 'espol.edu.ec' #reverse_lazy('Facturas:list')
#
#     form_class = CrearFacturaForm
#     #fields = ('serie', 'paciente', 'fecha_vencimiento', 'subtotal', 'total')
#
#     # def form_valid(self, form):
#     #     print 'saving'
#     #     return super(crearFactura, self).form_valid(form)
#     #     #return render_to_response(template_name, {'form': form})
#
#     def post(self, request):
#         print request.POST
#         super(crearFactura, self).post(request)
#         form = CrearFacturaForm(request.POST)
#         form.save()
#         if form.is_valid():
#             return HttpResponse('/ok/')
#         else:
#             return render(request, self.template_name, {'form': form})
#
#     def get_context_data(self, **kwargs):
#         print 'get_context_data'
#         context = super(crearFactura, self).get_context_data(**kwargs)
#         form = CrearFacturaForm()
#         form.fields['empresa'].queryset = Empresa.objects.all().order_by('nombre').values_list('nombre', flat=True)
#         context.update({'form' : form})
#         return context

# def validarFactura(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = FacturaForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('espol.edu.ec')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = FacturaForm()
#
#     return render(request, 'crear.html', {'form': form})

# class eliminarFactura(DeleteView):
#     model = Facturas
#     success_url = 'google.ec'
#     fields = ['name', 'start_date', 'end_date', 'picture']
#
