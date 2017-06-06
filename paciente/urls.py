'''
Created on Jun 4, 2017

@author: carlos
'''
from django.conf.urls import url
from paciente.views import pacientes, nuevoPaciente, modificarPaciente, eliminarPaciente
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^$', pacientes, name="pacientes"),
    url(r'^crear/$', nuevoPaciente, name="crear"),
    url(r'^modificar/(?P<paciente_id>\d+)/$', modificarPaciente, name="mod"),
    url(r'^eliminar/(?P<paciente_id>\d+)/', eliminarPaciente, name="eliminarPaciente"),

]
