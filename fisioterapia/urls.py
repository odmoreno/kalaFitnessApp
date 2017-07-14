from django.conf.urls import url

from . import views

app_name = 'paciente'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^mensajes/$', views.verMensajes, name='mensajes'),
    url(r'^mensajes/nuevo/$', views.nuevoMensaje, name='nuevoMensaje'),
    url(r'^mensajes/leer/(?P<mensaje_id>[0-9]+)/$', views.leerMensaje, name='leerMensaje'),
]