# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalaapp', '0002_auto_20170604_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='tipo',
            field=models.CharField(choices=[('administrador', 'administrador'), ('paciente', 'paciente'), ('fisioterapista', 'fisioterapista'), ('nutricionista', 'nutricionista'), ('invitado', 'invitado')], default='invitado', max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
