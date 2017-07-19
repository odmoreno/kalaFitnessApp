# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('nombre', models.CharField(max_length=200)),
                ('razon_social', models.CharField(blank=True, max_length=200, null=True)),
                ('propietario_nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('propietario_apellido', models.CharField(blank=True, max_length=200, null=True)),
                ('ruc', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('iva', models.IntegerField()),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'empresa',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('tipo', models.CharField(choices=[('administrador', 'administrador'), ('paciente', 'paciente'), ('fisioterapista', 'fisioterapista'), ('nutricionista', 'nutricionista'), ('invitado', 'invitado')], default='invitado', max_length=30)),
                ('es_personal', models.BooleanField(default=False, verbose_name='es_personal')),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'rol',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('nombre', models.CharField(db_column='first_name', max_length=30)),
                ('apellido', models.CharField(db_column='last_name', max_length=30)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=200, null=True)),
                ('genero', models.CharField(blank=True, max_length=1, null=True)),
                ('edad', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, default='usuario/noimagen.jpg', help_text='Foto', null=True, upload_to='usuario/')),
                ('estado_civil', models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Viudo', 'Viudo'), ('Divorciado', 'Divorciado')], default='Soltero', max_length=30)),
                ('estado', models.CharField(default='A', max_length=1)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kalaapp.Rol')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
