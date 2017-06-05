# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView, DeleteView
from django.shortcuts import render
from django.http import *
from .forms import CrearFacturaForm
from factura.models import Facturas
from kalaapp.models import Empresa, Usuario
from paciente.models import Paciente
from django.db.models.functions import Concat

# Create your views here.

def crearFactura(request):
    template_name = 'crear.html'
    empresa_nombre = None
    paciente_nombre = None

    if request.method == 'POST':
        empresa_nombre = request.POST['empresa']
        paciente_nombre = request.POST['paciente']
        request.POST = request.POST.copy()
        request.POST['empresa'] = int(Empresa.objects.get(nombre=request.POST['empresa']).pk);
        request.POST['paciente'] = int(Usuario.objects.get(nombre=request.POST['paciente']).pk);
        form = CrearFacturaForm(request.POST)

        if form.is_valid():
            #form.save()
            return HttpResponse(request.POST)
    else:
        form = CrearFacturaForm()

    form.fields['empresa'].queryset = Empresa.objects.filter(estado='A')\
                                        .order_by('nombre')\
                                        .values_list('nombre', flat=True)
    form.fields['paciente'].queryset = Usuario.objects.filter(estado='A', rol__tipo='paciente', paciente__estado='A') \
                                        .values_list('nombre', flat=True)
                                        #.annotate(search_name=Concat('nombre', ' ', 'apellido'))

    form.initial = {'empresa':empresa_nombre, 'paciente':paciente_nombre}
    context = {'form': form}
    return render(request, template_name, context=context)

def eliminarFactura(request, facturaId):
    pass












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
