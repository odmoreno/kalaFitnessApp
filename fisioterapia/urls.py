from django.conf.urls import url

from . import views

app_name = 'fisioterapia'
urlpatterns = [
    url(r'^$', views.index, name="indexF"),
    url(r'^ficha/$', views.crear_ficha, name="crear_ficha"),
    url(r'^ficha/lista/$', views.listar_fichas, name="lista_fichas"),
    url(r'^(?P<ficha_id>[0-9]+)/$', views.detalleFicha, name='detail'),
    #url(r'^mensajes/$', views.verMensajes, name='mensajesF'),
    #url(r'^mensajes/nuevo/$', views.nuevoMensaje, name='nuevoMensajeF'),
    #url(r'^mensajes/leer/(?P<mensaje_id>[0-9]+)/$', views.leerMensaje, name='leerMensajeF'),
    url(r'(?P<ficha_id>[0-9]+)/eliminar/$', views.eliminar_ficha, name="eliminar_ficha"),
    url(r'^editar/(?P<ficha_id>[0-9]+)/$', views.editar_ficha, name='editar_ficha'),
    url(r'^horario/$', views.establecer_horario, name="crear_horario"),
    url(r'^horario/ver/$', views.ver_horarios, name="ver_horarios"),
    url(r'(?P<horario_id>[0-9]+)/cita/eliminar/$', views.eliminar_cita, name="eliminar_cita"),
    url(r'^reportes/$', views.reportes, name="reportes"),
    url(r'^reporte/ficha/(?P<paciente_cedula>[0-9]+)/$', views.reporteFicha),
]
