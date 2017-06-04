# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView, DeleteView
from django.shortcuts import render
from django.http import request
from .forms import CrearFacturaForm
from factura.models import Facturas

# Create your views here.

class crearFactura(CreateView):
    template_name = 'crear.html'
    success_url = 'espol.edu.ec' #reverse_lazy('courses:list')
    #model = Facturas
    form_class = CrearFacturaForm
    #fields = ('serie', 'paciente', 'fecha_vencimiento', 'subtotal', 'total')

    def form_valid(self, form):
        return HttpResponseRedirect('espol.edu.ec')

    def post(self, request):
        return http.HttpResponse("Post")

    def get_context_data(self, **kwargs):
        context = super(crearFactura, self).get_context_data(**kwargs)

        form = FacturaForm()
        context.update({'form' : form})
        return context

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

class eliminarFactura(DeleteView):
    model = Facturas
    success_url = 'google.ec'
    fields = ['name', 'start_date', 'end_date', 'picture']

