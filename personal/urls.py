
from django.conf.urls import url
from . import views

app_name = 'personal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^crear/$', views.nuevoPersonal, name="nuevoPersonal"),
    #url(r'^modificar/(?P<paciente_id>\d+)/$', views.modificarPersonal, name="modificarPersonal"),
    url(r'(?P<personal_id>[0-9]+)/eliminar/$', views.eliminarPersonal, name="eliminarPersonal"),
]