'''
Created on Jun 7, 2017

@author: Edgar Carvajal
'''
from django.conf.urls import url
from paciente.views import apiRestPacientes, apiPacientes
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #url(r'^$', pacientes, name="pacientes"),
    url(r'^api/$', apiPacientes, name="paciente"),
    url(r'^apirest/$', apiRestPacientes),
    url(r'^crear/$', nuevoPaciente),
    url(r'^modificar/(?P<paciente_id>\d+)/$', modificarPaciente),
    url(r'^eliminar/(?P<paciente_id>\d+)/', eliminarPaciente),
]
