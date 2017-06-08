'''
Created on Jun 7, 2017

@author: Edgar Carvajal
'''
from django.conf.urls import url
from factura.views import apiFactura
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #url(r'^$', pacientes, name="pacientes"),
    url(r'^api/$', apiFactura, name="factura"),
    #url(r'^crear/$', nuevoPaciente, name="crear"),
    #url(r'^modificar/(?P<paciente_id>\d+)/$', modificarPaciente, name="mod"),
    #url(r'^eliminar/(?P<paciente_id>\d+)/', eliminarPaciente, name="eliminarPaciente"),
]
