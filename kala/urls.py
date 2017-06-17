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
from kala.views import index
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    url(r'^kalaapp/', include("kalaapp.urls")),
    url(r'^admin/', admin.site.urls),
    url(r'^paciente/', include('paciente.urls')),
    url(r'^personal/', include('personal.urls')),
    url(r'^factura/', include('factura.urls')),
    url(r'^accounts/login/', LoginView.as_view(template_name="kalaapp/login.html"), name="login"),
    url(r'^accounts/logout/', LogoutView.as_view(next_page="/home"), name="logout"),
    #url(r'^$', index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
