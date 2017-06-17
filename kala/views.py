# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.
def index(request):
    return render(request, 'kalaapp/landing.html')