from django.conf.urls import url
from . import views


app_name = 'personal'

urlpatterns = [
    url(r'^$', views.index , name="index"),
    url(r'^crear/$', views.nuevoPersonal, name="nuevoPersonal"),
    #url(r'^modificar/(?P<paciente_id>\d+)/$', views.modificarPersonal, name="modificarPersonal"),
    url(r'(?P<personal_id>[0-9]+)/eliminar/$', views.eliminarPersonal, name="eliminarPersonal"),
    url(r'^(?P<personal_id>[0-9]+)/$', views.detallePersonal, name='detail'),
    url(r'^editar/(?P<personal_id>[0-9]+)/$', views.editarPersonal, name='editar'),
    url(r'^mensajes/$', views.verMensajes, name='mensajes'),
    url(r'^mensajes/nuevo/$', views.nuevoMensaje, name='nuevoMensaje'),
    url(r'^mensajes/leer/(?P<mensaje_id>[0-9]+)/$', views.leerMensaje, name='leerMensaje'),
    url(r'^reporte/$', views.reportePersonal),
    url(r'^pdf/$', views.reportePDF, name="reportePDF"),
]


