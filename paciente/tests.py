# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from paciente.models import Paciente
from kalaapp.models import Usuario, Rol
from django.contrib.auth.models import User
# Create your tests here.
class ingresarPacienteTestCase(TestCase):
    def setUp(self):
        Rol.objects.create(tipo='paciente')
        Rol.objects.create(tipo='fisioterapista')

    def testIngreso(self,cedula,nombre,apellido,direccion,telefono,ocupacion,genero,edad,fecha):
        user=User()
        user.username=cedula
        user.set_password("p.123456")
        user.save()

        usuario=Usuario()
        usuario.usuario=user
        usuario.rol= Rol.objects.name(tipo='paciente')
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

        self.assertEquals(Paciente.objects.get(usuario=usuario), usuario)
        self.assertEquals(Usuario.objects.get(cedula=cedula).cedula, cedula)
