from django.conf import settings
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^crear$', crearFactura, name='crear_factura'),
    url(r'^eliminar/(?P<pk>\d+)$', eliminarFactura, name='eliminar_factura'),

]