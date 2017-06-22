# -*- coding: utf-8 -*-
# Create your models here.
# 19262203
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `#managed = False` lines if you wish to allow Django to create, modify, and delete the table
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

class TimeModel(models.Model):
    creado = models.DateTimeField(_('creado'), auto_now_add=True)
    actualizado = models.DateTimeField(_('actualizado'), auto_now=True)

    class Meta:
        abstract = True

ROLES =(('administrador', 'administrador'),
        ('paciente', 'paciente'),
        ('fisioterapista', 'fisioterapista'),
        ('nutricionista', 'nutricionista'),
        ('invitado','invitado'))

class Rol(TimeModel):
    tipo = models.CharField(max_length=30, choices=ROLES, default='invitado', unique=True)
    es_personal = models.BooleanField(_('es_personal'), default=False, blank=False)
    estado = models.CharField(max_length=1, default='A')

    class Meta:
        db_table = 'rol'



class Usuario(TimeModel):
        usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
        rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
        nombre = models.CharField(db_column='first_name', max_length=30, blank=False, null=False )
        apellido = models.CharField(db_column='last_name', max_length=30, blank=False, null=False )
        cedula = models.CharField(max_length=10, unique=True)
        direccion = models.CharField(max_length=200, blank=True, null=True)
        telefono = models.CharField(max_length=50, blank=True, null=True)
        ocupacion = models.CharField(max_length=200, blank=True, null=True)
        genero = models.CharField(max_length=1, blank=True, null=True)
        edad = models.IntegerField(blank=True, null=True)
        fecha_nacimiento = models.DateField(blank=True, null=True)
        foto = models.ImageField(upload_to = 'usuario/',
                                 default = 'usuario/noimagen.jpg', null=True,
                                 blank=True, editable=True,
                                 help_text="Foto")
        estado = models.CharField(max_length=1, default='A')
        is_anonymous = False
        is_authenticated = False

        USERNAME_FIELD = 'cedula'
        REQUIRED_FIELDS = ['rol', 'username', 'password', 'email']

        class Meta:
            db_table = 'usuario'

        def save(self, *args, **kwargs):

            # fotoNombre = request.FILES['foto'].name
            # fotoExtension = fotoNombre.split('.')[len(fotoNombre.split('.')) - 1].lower()
            #
            # if fotoExtension not in settings.IMAGE_FILE_TYPES:
            #     form.add_error('foto', 'Imagen no valida, solo las siguientes extensiones son permitidas: %s' % ', '.join(
            #             settings.IMAGE_FILE_TYPES))

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
                    messages.add_message(request, messages.WARNING, 'No se puedo guardar la foto. ' + e.__str__())

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
'''
class Citas(models.Model):
    detalle = models.CharField(max_length=200)
    #citas_estado = models.ForeignKey('CitasEstados', models.DO_NOTHING)
    rango = models.ForeignKey('Rangos', models.DO_NOTHING)
    estado = models.CharField(max_length=1)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'citas'


# class CitasEstados(models.Model):
#     detalle = models.CharField(max_length=200)
#     estado = models.CharField(max_length=1)
#     creado = models.DateTimeField()
#     actualizado = models.DateTimeField()
#
#     class Meta:
#         #managed = False
#         db_table = 'citas_estados'




class FichasGenerales(models.Model):
    personal = models.ForeignKey('Personal', models.DO_NOTHING)
    usuario = models.ForeignKey('Pacientes', models.DO_NOTHING)
    altura = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    imc = models.FloatField(blank=True, null=True)
    musculo = models.FloatField(blank=True, null=True)
    grasa_visceral = models.FloatField(blank=True, null=True)
    grasa = models.FloatField(blank=True, null=True)
    cuello = models.FloatField(blank=True, null=True)
    hombros = models.FloatField(blank=True, null=True)
    pecho = models.FloatField(blank=True, null=True)
    brazo_derecho = models.FloatField(blank=True, null=True)
    brazo_izquierdo = models.FloatField(blank=True, null=True)
    antebrazo_derecho = models.FloatField(blank=True, null=True)
    antebrazo_izquierdo = models.FloatField(blank=True, null=True)
    cintura = models.FloatField(blank=True, null=True)
    cadera = models.FloatField(blank=True, null=True)
    muslo_derecho = models.FloatField(blank=True, null=True)
    muslo_izquierdo = models.FloatField(blank=True, null=True)
    pantorrilla_derecha = models.FloatField(blank=True, null=True)
    pantorrilla_izquierda = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=1)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'fichas_generales'


class Horarios(models.Model):
    detalle = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=1)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'horarios'


class Mensajes(models.Model):
    usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING)
    mensaje_tipo = models.ForeignKey('MensajesTipo', models.DO_NOTHING)
    #mensaje_estado = models.ForeignKey('MensajesEstados', models.DO_NOTHING)
    mensaje = models.CharField(max_length=999)
    estado = models.CharField(max_length=1)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'mensajes'


# class MensajesEstados(models.Model):
#     detalle = models.CharField(max_length=200)
#     estado = models.CharField(max_length=1)
#     creado = models.DateTimeField()
#     actualizado = models.DateTimeField()
#
#     class Meta:
#         #managed = False
#         db_table = 'mensajes_estados'


class MensajesTipo(models.Model):
    detalle = models.CharField(max_length=200)
    estado = models.CharField(max_length=1)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'mensajes_tipo'


class Planificaciones(models.Model):
    horario = models.ForeignKey(Horarios, models.DO_NOTHING)
    rango = models.ForeignKey('Rangos', models.DO_NOTHING)
    fecha_vigencia = models.DateField()
    estado = models.CharField(max_length=1)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'planificaciones'


class Rangos(models.Model):
    inicio = models.ForeignKey('Tiempos', models.DO_NOTHING, db_column='inicio', related_name='rango_inicio')
    fin = models.ForeignKey('Tiempos', models.DO_NOTHING, db_column='fin', related_name='rango_fin')
    estado = models.CharField(max_length=1)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'rangos'

class SesionesFisioterapia(models.Model):
    personal = models.ForeignKey(Personal, models.DO_NOTHING)
    fichas_general = models.ForeignKey(FichasGenerales, models.DO_NOTHING)
    fuerza_ts = models.FloatField(blank=True, null=True)
    fuerza_ti = models.FloatField(blank=True, null=True)
    flexiones_p = models.IntegerField(blank=True, null=True)
    sentadillas = models.IntegerField(blank=True, null=True)
    salto_largo = models.IntegerField(blank=True, null=True)
    suspension = models.IntegerField(blank=True, null=True)
    abdominales_bajos = models.IntegerField(blank=True, null=True)
    abdominales_altos = models.IntegerField(blank=True, null=True)
    espinales = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=1)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'sesiones_fisioterapia'


class SesionesNutricion(models.Model):
    personal = models.ForeignKey(Personal, models.DO_NOTHING)
    fichas_general = models.ForeignKey(FichasGenerales, models.DO_NOTHING)
    horas_sueno = models.IntegerField(blank=True, null=True)
    comidas_diarias = models.IntegerField(blank=True, null=True)
    enfermedad_digestiva = models.IntegerField(blank=True, null=True)
    alimentos_permitidos = models.CharField(max_length=999, blank=True, null=True)
    alimentos_no_permitidos = models.CharField(max_length=999, blank=True, null=True)
    biotipo = models.CharField(max_length=200, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=1)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'sesiones_nutricion'


class Tiempos(models.Model):
    hora = models.IntegerField()
    minuto = models.IntegerField()
    estado = models.CharField(max_length=1)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'tiempos'
'''
'''
from usuario.models import Usuario
from usuario.models import Rol


r = Rol.objects.all()
r = Rol.objects.all().order_by('id').first()
roles = Rol.objects.bulk_create([Rol(tipo='administrador', es_personal=False),
                                 Rol(tipo='paciente', es_personal=False),
                                 Rol(tipo='fisioterapista', es_personal=True),
                                 Rol(tipo='nutricionista', es_personal=True)])
for x in roles:
    x.save()

for x in roles:
    x.save()

r = Rol.objects.all().order_by('id').first()
u = Usuario.objects.create_superuser(username='chaljara', email='chaljara@espol.edu.ec', cedula='0921825345',
                                     password='adminadmin', rol=r)

p=Personal.objects.create(rol=r, username="chaljara2", email="chaljara@espol.edu.ec", cedula="09218255345", first_name="christian", last_name="jaramillo", password="adminadmin")
'''