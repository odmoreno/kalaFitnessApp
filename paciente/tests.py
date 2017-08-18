# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.test import TestCase, Client, RequestFactory
from paciente.models import Paciente
from kalaapp.models import Usuario, Rol
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your tests here.

class ingresarPacienteTestCase(TestCase):
    def setUp(self):
        s=Rol.objects.create(tipo='paciente')
        s.save()
        p=Rol.objects.create(tipo='fisioterapista')
        p.save()

    def testIngreso(self):
        cedula="0936934468"
        nombre="Carlos"
        apellido="Manosalvas"
        direccion="Calle 3"
        telefono="2365897"
        ocupacion="Student"
        genero="M"
        edad=25
        fecha=27/03/2005
        user=User()
        user.username=cedula
        user.set_password("p.123456")
        user.save()

        usuario=Usuario()
        usuario.usuario=user
        rol=Rol.objects.get(tipo='paciente')
        usuario.rol=rol
        usuario.nombre=nombre
        usuario.apellido=apellido
        usuario.cedula=cedula
        usuario.genero=genero
        usuario.edad=edad
        usuario.telefono=telefono
        usuario.direccion=direccion
        usuario.ocupacion=ocupacion
        usuario.fecha=fecha
        usuario.save()
        paciente=Paciente()
        paciente.usuario=usuario
        paciente.save()

        self.assertEquals(Paciente.objects.get(usuario=usuario).usuario, usuario)
        self.assertEquals(Usuario.objects.get(cedula=cedula).cedula, cedula)


class EliminarPacienteTestCase(TestCase):
    def setUp(self):
        s=Rol.objects.create(tipo='paciente')
        s.save()
        p=Rol.objects.create(tipo='fisioterapista')
        p.save()

    def testIngreso(self):
        cedula="0936934468"
        nombre="Carlos"
        apellido="Manosalvas"
        direccion="Calle 3"
        telefono="2365897"
        ocupacion="Student"
        genero="M"
        edad=25
        fecha=27/03/2005
        user=User()
        user.username=cedula
        user.set_password("p.123456")
        user.save()

        usuario=Usuario()
        usuario.usuario=user
        rol=Rol.objects.get(tipo='paciente')
        usuario.rol=rol
        usuario.nombre=nombre
        usuario.apellido=apellido
        usuario.cedula=cedula
        usuario.genero=genero
        usuario.edad=edad
        usuario.telefono=telefono
        usuario.direccion=direccion
        usuario.ocupacion=ocupacion
        usuario.fecha=fecha
        usuario.save()
        paciente=Paciente()
        paciente.usuario=usuario
        paciente.save()

        user1=User.objects.get(username=cedula)
        user1.delete()

        try:
            x=User.objects.get(username=cedula)

        except User.DoesNotExist:
            x=None

        try:
            y=Usuario.objects.get(cedula=cedula)
        except Usuario.DoesNotExist:
            y=None

        self.assertEquals(x, None)
        self.assertEquals(y, None)

class PacienteViewsTestCase(TestCase):
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
        rol = Rol.objects.get(tipo='paciente')
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

        paciente = Paciente()
        paciente.usuario = usuario
        paciente.save()

    def testGenerarIndexView(self):
        paciente = Paciente.objects.all()
        paciente=paciente[0]
        id=paciente.id
        c = Client()
        c.login(username='carlos', password='carlos123')
        response1 = c.get(reverse("paciente:index"))
        self.assertEquals(response1.status_code, 200)


    def testGenerarCrearView(self):
        self.client.login(username='carlos', password='carlos123')
        paciente = Paciente.objects.all()
        paciente = paciente[0]
        id = paciente.id
        c = Client()
        c.login(username='carlos', password='carlos123')
        response2 = c.get(reverse("paciente:paciente"))
        self.assertEquals(response2.status_code, 200)


    def testGenerarDetallesView(self):
        self.client.login(username='carlos', password='carlos123')
        paciente = Paciente.objects.all()
        paciente = paciente[0]
        id = paciente.id
        c = Client()
        c.login(username='carlos', password='carlos123')
        response3 = c.get('/paciente/%s/' % id)
        self.assertEquals(response3.status_code, 200)


    def testGenerarEditarView(self):
        self.client.login(username='carlos', password='carlos123')
        paciente = Paciente.objects.all()
        paciente = paciente[0]
        id = paciente.id
        c = Client()
        c.login(username='carlos', password='carlos123')
        response4 = c.get('/paciente/editar/%s/' % id)

        self.assertEquals(response4.status_code, 200)


    def testGenerarEliminarView(self):
        self.client.login(username='carlos', password='carlos123')
        paciente = Paciente.objects.all()
        paciente = paciente[0]
        id = paciente.id
        c = Client()
        c.login(username='carlos', password='carlos123')
        response4 = c.get('/paciente/eliminar/%s/' % id)
        self.assertEquals(response4.status_code, 302)
