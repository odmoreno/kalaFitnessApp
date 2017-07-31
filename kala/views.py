# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
import random
import string
from . import settings
from django.http import HttpResponseRedirect


def generar_password(size=6, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def enviar_password_email(destinatario, usuario, password):
    try:
        send_mail(subject='Kala Fitness App',
                  message='Su usuario es: ' + usuario +
                  '\nSu contraseña generada es: ' + password +
                  '\nEs recomendable que cambie la contraseña luego de iniciar sesión',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[destinatario],
                  fail_silently=False)
    except Exception, e:
        pass
        #print "SEND EMAIL EXCEPT: " + str(e)
