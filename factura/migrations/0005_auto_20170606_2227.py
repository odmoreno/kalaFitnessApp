# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0004_auto_20170604_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturas',
            name='serie',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]