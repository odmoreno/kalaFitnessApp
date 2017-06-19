
from django.conf.urls import url
from paciente.views import apiRestPacientes, apiPacientes, nuevoPaciente, modificarPaciente, eliminarPaciente, reportePacientes
from . import views

app_name = 'paciente'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^api/$', apiPacientes, name="pacientes"),
    url(r'^apirest/$', apiRestPacientes),
    url(r'^crear/$', views.PacienteNuevo, name="paciente"),
    #url(r'^modificar/(?P<paciente_id>\d+)/$', views.PacienteModificar, name="modificar"),
    url(r'^eliminar/(?P<paciente_id>\d+)/', views.PacienteEliminar, name="eliminar"),
    url(r'^reporte/$', reportePacientes),
]
