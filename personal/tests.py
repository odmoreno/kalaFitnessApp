# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from personal.models import Personal
from kalaapp.models import Usuario, Rol
from django.contrib.auth.models import User

# Create your tests here.

class ingresarPersonalTest(TestCase):
    def setUp(self):
        n=Rol.objects.create(tipo='nutricionista')
        n.save()
        f=Rol.objects.create(tipo='fisioterapista')
        f.save()

    def test_nuevo_personal(self):
        cedula = "0931245228"
        password = "12345"
        user = User()
        user.username = cedula
        user.set_password(password)
        user.save()
        rol =  Rol.objects.get(tipo='nutricionista')

        usuario = Usuario()
        usuario.usuario= user
        usuario.rol = rol
        usuario.nombre = "Oscar"
        usuario.apellido = "Moreno"
        usuario.cedula = cedula
        usuario.direccion = "albo"
        usuario.telefono = "093912312"
        usuario.genero = "M"
        usuario.edad = 22
        usuario.fecha_nacimiento = 14/06/2017
        usuario.save()

        personal = Personal()
        personal.usuario = usuario
        personal.save()

        self.assertEquals(Personal.objects.get(usuario=usuario).usuario, usuario)
        self.assertEquals(Usuario.objects.get(cedula=cedula).cedula, cedula)

class eliminarPersonalTest():
    def setUp(self):
        n=Rol.objects.create(tipo='nutricionista')
        n.save()
        f=Rol.objects.create(tipo='fisioterapista')
        f.save()

    def test_eliminar_personal(self):
        cedula = "0931245229"
        password = "12345"
        user = User()
        user.username = cedula
        user.set_password(password)
        user.save()
        rol =  Rol.objects.get(tipo='fisioterapista')

        usuario = Usuario()
        usuario.usuario= user
        usuario.rol = rol
        usuario.nombre = "Daniel"
        usuario.apellido = "Moreno"
        usuario.cedula = cedula
        usuario.direccion = "albo"
        usuario.telefono = "093912312"
        usuario.genero = "M"
        usuario.edad = 22
        usuario.fecha_nacimiento = 14/06/2017
        usuario.save()

        personal = Personal()
        personal.usuario = usuario
        personal.save()

        user1 = User.objects.get(username=cedula)
        user1.delete()

        try:
            x = User.objects.get(username=cedula)

        except User.DoesNotExist:
            x = None

        try:
            y = Usuario.objects.get(cedula=cedula)
        except Usuario.DoesNotExist:
            y = None

        self.assertEquals(x, None)
        self.assertEquals(y, None)

