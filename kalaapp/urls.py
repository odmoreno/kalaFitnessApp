'''
Created on Jun 4, 2017

@author: carlos
'''
from django.conf.urls import url
from kalaapp.views import index
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'kalaapp'

urlpatterns = [
    #url(r'^$', index, name="index"),
    url(r'^$', views.index , name="index"),
]
