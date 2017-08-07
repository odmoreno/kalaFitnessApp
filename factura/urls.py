from django.conf import settings
from .views import *


from django.conf.urls import url
from factura.views import apiFactura
from . import views

app_name = 'factura'

urlpatterns = [
    url(r'^$', listarFacturas, name='ListarFacturas'),
    url(r'^crear$', crearFactura, name='CrearFactura'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarFactura, name='EliminarFactura'),
    url(r'^api/$', views.apiFactura, name="ApiFactura"),
    url(r'^reportes/$', views.reportes, name="reportes"),
        url(r'^reporte/total/$', views.reporteTotal),
]
