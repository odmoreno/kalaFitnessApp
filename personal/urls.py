'''
Created on Jun 7, 2017

@author: Edgar Carvajal
'''
from django.conf.urls import url
from personal.views import apiPersonal, nuevoPersonal, eliminarPersonal
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^api/$', apiPersonal, name="personal"),
    url(r'^crear/$', views.nuevoPersonal),
    #url(r'^modificar/(?P<paciente_id>\d+)/$', views.modificarPersonal),
    url(r'^eliminar/(?P<personal_id>\d+)/', eliminarPersonal),
    #url(r'(?P<personal_id>[0-9]+)/eliminar/$', eliminarPersonal),
]
