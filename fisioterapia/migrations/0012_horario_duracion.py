# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisioterapia', '0011_auto_20170816_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='duracion',
            field=models.PositiveSmallIntegerField(default=10),
        ),
    ]
