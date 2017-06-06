# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.
def index(request):
    template = 'templates/index.html'

    data = {
            'pacientes':"hola mundo",

        }
    return render(request, template, data)
