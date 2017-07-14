from django.conf.urls import url

from . import views

app_name = 'fisioterapia'
urlpatterns = [
    url(r'^$', views.index, name="indexF"),
    url(r'^mensajes/$', views.verMensajes, name='mensajesF'),
    url(r'^mensajes/nuevo/$', views.nuevoMensaje, name='nuevoMensajeF'),
    url(r'^mensajes/leer/(?P<mensaje_id>[0-9]+)/$', views.leerMensaje, name='leerMensajeF'),
]