from django.conf import settings
from .views import *


from django.conf.urls import url
from factura.views import apiFactura
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^api/$', apiFactura, name="factura"),
	url(r'^$', facturas, name='facturas'),
    url(r'^crear$', crearFactura, name='crear_factura'),
    url(r'^eliminar/(?P<pk>\d+)$', eliminarFactura, name='eliminar_factura'),
]

