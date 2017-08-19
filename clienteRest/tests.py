# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from kalaapp.models import Usuario, Rol
from personal.models import Personal
from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
# Create your tests here.


class ObtenerPersonalTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(username='carlos', password='carlos123')
        # self.client.login(username='carlos', password='carlos123')
        s = Rol.objects.create(tipo='paciente')
        s.save()
        p = Rol.objects.create(tipo='fisioterapista')
        p.save()

        cedula = "0936934468"
        nombre = "Carlos"
        apellido = "Manosalvas"
        direccion = "Calle 3"
        telefono = "2365897"
        ocupacion = "Student"
        genero = "M"
        edad = 25
        fecha = 27 / 03 / 2005
        user = User()
        user.username = cedula
        user.set_password("p.123456")
        user.save()

        usuario = Usuario()
        usuario.usuario = user
        rol = Rol.objects.get(tipo='fisioterapista')
        usuario.rol = rol
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.cedula = cedula
        usuario.genero = genero
        usuario.edad = edad
        usuario.telefono = telefono
        usuario.direccion = direccion
        usuario.ocupacion = ocupacion
        usuario.fecha = fecha
        usuario.save()

        personal = Personal()
        personal.usuario = usuario
        personal.save()

    def testObtenerPersonal(self):
        client = APIClient()
        client.login(username='carlos', password='carlos123')
        response = self.client.get('/api/personal/')
        personal=Personal.objects.get(usuario__cedula = "0936934468")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response2=response.data[0]
        self.assertEqual(response2["cedula"],"0936934468")
