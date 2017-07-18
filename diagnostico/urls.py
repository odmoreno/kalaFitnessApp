from django.conf import settings
from .views import *


from django.conf.urls import url
from factura.views import apiFactura
from . import views

app_name = 'diagnostico'

urlpatterns = [
    url(r'^$', listarDiagnosticos, name='ListarDiagnosticos'),
    url(r'^crear$', crearDiagnostico, name='CrearDiagnostico'),
    #url(r'^eliminar/(?P<id>\d+)$', eliminarDiagnostico, name='EliminarDiagnostico'),
    #url(r'^api/$', views.apiDiagnostico, name="ApiDiagnostico"),
]

