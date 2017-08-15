# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django import forms
from django.test import TestCase, Client, RequestFactory
from paciente.models import Paciente
from personal.models import Personal
from kalaapp.models import Usuario, Rol
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your tests here.
class PersonalViewsTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username= 'carlos', password = 'carlos123')
        #self.client.login(username='carlos', password='carlos123')
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

    def testGenerarIndexView(self):
        personal = Personal.objects.all()
        personal=personal[0]
        id=personal.id
        print id
        c = Client()
        c.login(username='carlos', password='carlos123')
        response1 = c.get(reverse("personal:index"))
        self.assertEquals(response1.status_code, 200)
        print "listar"


    def testGenerarCrearView(self):
        self.client.login(username='carlos', password='carlos123')
        personal = Personal.objects.all()
        personal = personal[0]
        id = personal.id
        print id
        c = Client()
        c.login(username='carlos', password='carlos123')
        response2 = c.get(reverse("personal:nuevoPersonal"))
        self.assertEquals(response2.status_code, 200)
        print "crear"


    def testGenerarDetallesView(self):
        self.client.login(username='carlos', password='carlos123')
        personal = Personal.objects.all()
        personal = personal[0]
        id = personal.id
        c = Client()
        c.login(username='carlos', password='carlos123')
        response3 = c.get('/personal/%s/' % id)
        self.assertEquals(response3.status_code, 200)
        print "detalles"


    def testGenerarEditarView(self):
        self.client.login(username='carlos', password='carlos123')
        personal = Personal.objects.all()
        personal = personal[0]
        id = personal.id
        c = Client()
        c.login(username='carlos', password='carlos123')
        response4 = c.get('/personal/editar/%s/' % id)

        self.assertEquals(response4.status_code, 200)
        print "editar"
        print response4.status_code

    def testGenerarEliminarView(self):
        self.client.login(username='carlos', password='carlos123')
        personal = Personal.objects.all()
        personal = personal[0]
        id = personal.id
        c = Client()
        c.login(username='carlos', password='carlos123')
        response4 = c.get('/personal/%s/eliminar' % id)
        print response4
        self.assertEquals(response4.status_code, 200)
        print "editar"
        print response4.status_code

