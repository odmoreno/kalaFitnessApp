# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 06:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostico', '0002_auto_20170726_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosticonutricion',
            name='area_afectada',
        ),
    ]
