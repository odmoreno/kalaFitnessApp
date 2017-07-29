from django.conf.urls import url

from . import views

app_name = 'nutricion'
urlpatterns = [
    url(r'^$', views.index, name="indexF"),
    url(r'^ficha/$', views.crear_ficha, name="crear_ficha")
]