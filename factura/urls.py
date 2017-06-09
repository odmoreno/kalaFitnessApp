from django.conf import settings
from .views import *


from django.conf.urls import url
from factura.views import apiFactura
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    #url(r'^$', views.index, name="index"),
    url(r'^api/$', views.apiFactura, name="factura"),
	#url(r'^$', facturas, name='facturas'),
    url(r'^crear$', crearFactura),
    url(r'^eliminar/(?P<pk>\d+)$', eliminarFactura),
]

