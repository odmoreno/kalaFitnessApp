# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
import random
import string
from . import settings
from django.http import HttpResponseRedirect


def generar_password(size=6, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def enviar_password_email(request):
    send_mail('Kala Fitness App', 'Su contraseña generada es: ' + generar_password() +
              '\nEs recomendable que cambie la contraseña cuando inicie sesión', settings.EMAIL_HOST,
        ['christianjara21@gmail.com'], fail_silently=False)
    return HttpResponseRedirect('/')

