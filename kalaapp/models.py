# -*- coding: utf-8 -*-
# Create your models here.
# 19262203
# This is an auto-generated Django model module.
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.six import StringIO
from PIL import Image
from django.conf import settings
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class TimeModel(models.Model):
    creado = models.DateTimeField(_('creado'), auto_now_add=True)
    actualizado = models.DateTimeField(_('actualizado'), auto_now=True)

    class Meta:
        abstract = True


class Rol(TimeModel):
    ROLES = (('administrador', 'administrador'), ('paciente', 'paciente'), ('fisioterapista', 'fisioterapista'),
             ('nutricionista', 'nutricionista'), ('invitado', 'invitado'))
    tipo = models.CharField(max_length=30, choices=ROLES, default='invitado')
    es_personal = models.BooleanField(_('es_personal'), default=False, blank=False)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        db_table = 'rol'


class Usuario(TimeModel):
    ESTADO_CIVIL = (('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Viudo', 'Viudo'), ('Divorciado', 'Divorciado'))
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    cedula = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    ocupacion = models.CharField(max_length=200, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    edad = models.PositiveSmallIntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='usuario/',
                             default='usuario/noimagen.jpg', null=True,
                             blank=True, editable=True,
                             help_text="Foto")
    estado_civil = models.CharField(max_length=30, choices=ESTADO_CIVIL, default='Soltero', null=False)
    estado = models.CharField(max_length=1, default='A')
    is_anonymous = False
    is_authenticated = False

    USERNAME_FIELD = 'cedula'
    REQUIRED_FIELDS = ['rol', 'username', 'password', 'email']

    class Meta:
        db_table = 'usuario'

    def save(self, *args, **kwargs):
        if self.foto and self.foto.name.find('noimagen.jpg') == -1:
            try:
                img = Image.open(self.foto)
                width, height = img.size
                basewidth = 600
                baseheight = 600

                if img.mode != 'RGB':
                    img = img.convert('RGB')

                if width >= height and width > basewidth:
                    height_size = int((float(height) * float(basewidth / float(width))))
                    width = basewidth
                    height = height_size
                elif width < height and height > baseheight:
                    width_size = int((float(width) * float(baseheight / float(height))))
                    width = width_size
                    height = baseheight

                img = img.resize((width, height), Image.ANTIALIAS)
                output = StringIO()
                img.save(output, format='JPEG', quality=90)
                output.seek(0)
                self.foto = InMemoryUploadedFile(output, 'foto', "%s.jpg" % self.cedula, 'image/jpeg', output.len, None)
            except Exception as e:
                print str(e) + ' Error al  guardar la foto'

        super(Usuario, self).save(*args, **kwargs)


class Empresa(TimeModel):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    propietario_nombre = models.CharField(max_length=200,blank=True, null=True)
    propietario_apellido = models.CharField(max_length=200,blank=True, null=True)
    ruc = models.CharField(max_length=50,blank=False, null=False)
    telefono = models.CharField(max_length=50,blank=True, null=True)
    direccion = models.CharField(max_length=200,blank=True, null=True)
    iva = models.IntegerField()
    #planificacion = models.ForeignKey('Planificaciones', models.DO_NOTHING)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        #managed = False
        db_table = 'empresa'


