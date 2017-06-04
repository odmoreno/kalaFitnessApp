from django.conf import settings
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^crear$', crearFactura.as_view(), name='crear_factura'),
    url(r'^eliminar/(?P<pk>\d+)$', eliminarFactura.as_view(), name='eliminar_factura'),

]