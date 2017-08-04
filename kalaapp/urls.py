'''
Created on Jun 4, 2017

@author: carlos
'''
from django.conf.urls import url

from . import views

app_name = 'kalaapp'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^asignar$', views.asignarPersonalaPaciente, name="AsignarPersonalaPaciente"),
]
