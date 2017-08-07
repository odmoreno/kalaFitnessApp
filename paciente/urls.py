
from django.conf.urls import url
#from paciente.views import reportePDF, reportePacientes
from . import views

app_name = 'paciente'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^crear/$', views.PacienteNuevo, name="paciente"),
    url(r'^(?P<paciente_id>[0-9]+)/$', views.detallePaciente, name='detail'),
    url(r'^editar/(?P<paciente_id>[0-9]+)/$', views.editarPaciente, name='editar'),
    #url(r'^modificar/(?P<paciente_id>\d+)/$', views.PacienteModificar, name="modificar"),
    url(r'^eliminar/(?P<paciente_id>\d+)/', views.PacienteEliminar, name="eliminar"),
    url(r'^reporte/hombres/$', views.reporteHombres),
    url(r'^reporte/mujeres/$', views.reporteMujeres),
    url(r'^reporte/totales/$', views.reporteTotales),
    url(r'^reportes/$', views.reportes, name="reportes"),
]
