'''
Created on Jun 4, 2017

@author: carlos
'''
from django.conf.urls import url
from kalaapp.views import index
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^$', index, name="index"),
]
