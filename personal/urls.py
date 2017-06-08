'''
Created on Jun 7, 2017

@author: Edgar Carvajal
'''
from django.conf.urls import url
from personal.views import apiPersonal
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^api/$', apiPersonal, name="personal"),
    ##url(r'^crear/$', views.nuevoPersonal, name="nuevoPersonal"),
    #url(r'^modificar/(?P<paciente_id>\d+)/$', views.modificarPersonal, name="modificarPersonal"),
    ##url(r'(?P<personal_id>[0-9]+)/eliminar/$', views.eliminarPersonal, name="eliminarPersonal"),
]
