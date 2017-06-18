# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse


# Create your views here.
def index(request):
    template = 'kalaapp/landing.html'
    data = {}
    return render(request, template, data)
