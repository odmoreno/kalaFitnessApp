from django.conf import settings
from .views import *


from django.conf.urls import url
from factura.views import apiFactura
from . import views

app_name = 'diagnostico'

urlpatterns = [
    url(r'^$', listarDiagnosticos, name='ListarDiagnosticos'),
    url(r'^crear$', crearDiagnostico, name='CrearDiagnostico'),
    url(r'^(?P<diagnostico_id>[0-9]+)/$', views.detalleDiagnostico, name='detail'),
    url(r'^editar/(?P<id>\d+)$', editarDiagnostico, name='EditarDiagnostico'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarDiagnostico, name='EliminarDiagnostico'),
    url(r'^guardar$', guardarDiagnostico, name='GuardarDiagnostico'),
    url(r'^reportes/$', views.reportes, name="reportes"),
        url(r'^reporte/(?P<paciente_cedula>[0-9]+)/$', views.reporteTotal),
    #url(r'^api/$', views.apiDiagnostico, name="ApiDiagnostico"),
]
