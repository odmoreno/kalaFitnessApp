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
#from factura.urls import urlpatterns as urlfactura
from factura.views import crearFactura, eliminarFactura



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', crearFactura.as_view(), name='crear_factura'),
    #url(r'^factura/', include('factura.urls')),
    #url(r'^paciente/', include(factura.urls)),
    #url(r'^personal/', include(factura.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
