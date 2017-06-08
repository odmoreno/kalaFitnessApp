# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.db import transaction
from factura.models import Facturas
##from kalaapp.models import Usuario, Rol
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse


# Create your views here.
def apiFactura(request):
    template = "factura/factura.html"
    obj = Facturas.objects.all()
    data = {"facturas": obj}
    return render(request, template, data)
