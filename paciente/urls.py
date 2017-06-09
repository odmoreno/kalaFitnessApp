
from django.conf.urls import url
from paciente.views import apiRestPacientes, apiPacientes
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #url(r'^$', pacientes, name="pacientes"),
    url(r'^api/$', apiPacientes, name="paciente"),
    url(r'^apirest/$', apiRestPacientes),
    #url(r'^crear/$', nuevoPaciente, name="crear"),
    #url(r'^modificar/(?P<paciente_id>\d+)/$', modificarPaciente, name="mod"),
    #url(r'^eliminar/(?P<paciente_id>\d+)/', eliminarPaciente, name="eliminarPaciente"),
]
