# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from kalaapp.models import Usuario, Rol, Empresa
from django.contrib.auth.models import User
from paciente.models import Paciente
from factura.models import Facturas

# Create your tests here.


class verificarCreacionFacturaTestCase(TestCase):

    def setUp(self):
        rol = Rol.objects.create(tipo='paciente')
        user = User.objects.create()
        usuario = Usuario.objects.create(usuario=user, rol=rol, cedula='0999999999', nombre='christian', apellido='jaramillo')
        Paciente.objects.create(usuario=usuario)
        Empresa.objects.create(nombre='Kala Fitness', iva='12')

    def testCrearFactura(self):
        factura = Facturas.objects.create(empresa=Empresa.objects.filter(nombre='Kala Fitness').first(),
                                          paciente=Paciente.objects.filter(usuario__cedula='0999999999').first(),
                                          serie='5432',
                                          fecha_vencimiento='2017-12-12',
                                          total='500')
        factura.save()
        factura_rec = Facturas.objects.get(serie='5432')
        self.assertEquals(factura.id, factura_rec.id, 'Error facturas no coinciden!')