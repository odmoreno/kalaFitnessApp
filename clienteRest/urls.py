from django.conf.urls import url, include
from rest_framework.authtoken import views

from rest_framework.urlpatterns import format_suffix_patterns
from clienteRest import views as api


urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^personal/', api.PersonalList.as_view()),
    url(r'^personal/(?P<paciente_us>[0-9]+)/$', api.PersonalAsignadoList.as_view()),
    url(r'^diagnosticoN/(?P<paciente_us>[0-9]+)/$', api.DiagnosticoNutList.as_view()),
    url(r'^diagnosticoF/(?P<paciente_us>[0-9]+)/$', api.DiagnosticoFisList.as_view()),
    url(r'^plandieta/(?P<paciente_us>[0-9]+)/$', api.DietasList.as_view()),
    url(r'^rutinas/(?P<paciente_us>[0-9]+)/$', api.RutinasList.as_view()),
    url(r'^fichas/fisioterapia/(?P<paciente_us>[0-9]+)/$', api.FichaFisList.as_view()),
    url(r'^fichas/nutricion/(?P<paciente_us>[0-9]+)/$', api.FichaNutList.as_view()),
    url(r'^mensajes/(?P<paciente_us>[0-9]+)/$', api.MensajesList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

]
#urlpatterns= format_suffix_patterns(urlpatterns)
