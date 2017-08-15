# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

    def testGenerarViews(self):
        self.client.login(username='carlos', password='carlos123')
        paciente = Paciente.objects.all()
        paciente=paciente[0]
        id=paciente.id
        print id
        c = Client()
        response1 = c.get(reverse("paciente:index"))
        response2 = c.get(reverse("paciente:paciente"))
        response3 = c.get('/paciente/%s/' % id)
        response4 = c.get('/paciente/editar/%s/' % id)
        self.assertEquals(response1.status_code, 302)
        print "listar"
        self.assertEquals(response2.status_code, 302)
        print "crear"
        self.assertEquals(response3.status_code, 302)
        print "detalles"
        self.assertEquals(response4.status_code, 302)
        print "eliminar"

    def testCrearView(self):
        c = Client()
        response1 = c.post(reverse("paciente:paciente"), {'nombre':'Carlos','cedula':'1234567896', 'apellido':'Manosalvas', 'email':'carlos@gmail.com', 'estado_civil':'Soltero', 'direccion':'Por ahi', 'telefono':'2341472', 'ocupacion':'Estudiante','genero':'M', 'edad':'23', 'observaciones':'Algo', 'motivo_consulta':'Otra'})
        usuario=Usuario.objects.get(cedula='1234567896')
        print usuario
        self.assertEquals(response1.status_code, 302)
       # self.assertEquals(usuario, Usuario.objects.get(cedula='1234567896'))
        print "creacion"

