from django.conf.urls import url

from . import views

app_name = 'nutricion'
urlpatterns = [
    url(r'^$', views.index, name="indexF"),
    url(r'^ficha/$', views.crear_ficha, name="crear_ficha"),
    url(r'^ficha/lista/$', views.listar_fichas, name="listar_fichas"),
    url(r'^(?P<ficha_id>[0-9]+)/$', views.detalleFicha, name='detail'),
    url(r'(?P<ficha_id>[0-9]+)/eliminar/$', views.eliminar_ficha, name="eliminar_ficha"),
    url(r'^editar/(?P<ficha_id>[0-9]+)/$', views.editar_ficha, name='editar_ficha'),
    url(r'^reporte/(?P<cedula>[0-9]+)/$', views.reporteByCedula),
    url(r'^reportes/$', views.reportes, name="reportes"),
    url(r'^horario/$', views.establecer_horario, name="crear_horario"),
    url(r'^horario/ver/$', views.ver_horarios, name="ver_horarios"),
    url(r'(?P<horario_id>[0-9]+)/cita/eliminar/$', views.eliminar_cita, name="eliminar_cita"),
]
