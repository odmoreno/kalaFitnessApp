# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.test import TestCase
from directmessages.apps import Inbox
from directmessages.models import Message
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory, Client
from .views import listar_fichas, crear_ficha
from paciente.models import Paciente
from personal.models import Personal
from fisioterapia.models import Ficha

from paciente.tests import ingresarPacienteTestCase

class EnviarMensajeTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='Usuario1')
        self.u2 = User.objects.create(username='Usuario2')

    def test_enviar_mensaje(self):
        init_value = Message.objects.all().count()

        message, status = Inbox.send_message(self.u1, self.u2, "Mensaje Mensaje Mensaje")

        after_value = Message.objects.all().count()

        self.assertEqual(init_value + 1, after_value)
        self.assertEqual(status, 200)
        self.assertEqual(message.content, "Mensaje Mensaje Mensaje")


class LeerMensajeTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='Usuario1')
        self.u2 = User.objects.create(username='Usuario2')

    def test_mensajes_unread(self):
        Inbox.send_message(self.u1, self.u2, "Mensaje Mensaje Mensaje")

        unread_messages = Inbox.get_unread_messages(self.u1)
        unread_messages2 = Inbox.get_unread_messages(self.u2)

        self.assertEqual(unread_messages.count(), 0)
        self.assertEqual(unread_messages2.count(), 1)

    def test_leer_mensajes(self):
        Inbox.send_message(self.u2, self.u1, "Mensaje Mensaje Mensaje")

        unread_messages = Inbox.get_unread_messages(self.u1)
        self.assertEqual(unread_messages.count(), 1)

        message = Inbox.read_message(unread_messages[0].id)
        unread_messages_after = Inbox.get_unread_messages(self.u1)

        self.assertEqual(message, "Mensaje Mensaje Mensaje")
        self.assertEqual(unread_messages_after.count(), 0)

class listarfichas(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_listar_fichas(self):
       request = self.factory.get('/fisioterapia/ficha/lista')
       response = listar_fichas(request)
       #print  response.content
       self.assertEqual(response.status_code, 200)

class crearficha(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        paciente = ingresarPacienteTestCase.testIngreso

        print paciente


    def test_crear_ficha(self):

        request = self.factory.get('/fisioterapia/ficha')
        response = crear_ficha(request)
        self.assertEqual(response.status_code, 200)
