"""kala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout, password_change, password_change_done, password_reset, \
                                        password_reset_done, password_reset_complete, password_reset_confirm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

urlpatterns = [
    url(r'^', include('kalaapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^paciente/', include('paciente.urls')),
    url(r'^personal/', include('personal.urls')),
    url(r'^factura/', include('factura.urls')),
    url(r'^fisioterapia/', include('fisioterapia.urls')),
    url(r'^nutricion/', include('nutricion.urls')),
    url(r'^diagnostico/', include('diagnostico.urls')),

    url(r'^login/$', login, 
        {'template_name': 'login.html', 'authentication_form': AuthenticationForm, 'redirect_authenticated_user': True}, 
        name='login'),
    url(r'^logout/$', logout, 
        {'next_page': settings.LOGIN_URL}, 
        name="logout"),
    url(r'^password_change/$', password_change,
        {'template_name': 'password_change.html', 'password_change_form': PasswordChangeForm}, 
        name='password_change'),
    url(r'^password_change/done/$', password_change_done, 
        {'template_name': 'password_change_done.html'},
        name='password_change_done'),
    url(r'^password_reset/$', password_reset,
        {'template_name': 'password_reset.html',
         'password_reset_form': PasswordResetForm},
        name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done,
        {'template_name': 'password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, 
        {'template_name': 'password_reset_confirm.html', 'set_password_form': SetPasswordForm},
        name='password_reset_confirm'),
    url(r'reset/done/$', password_reset_complete, 
        {'template_name': 'password_reset_complete.html'},
        name='password_reset_complete'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
