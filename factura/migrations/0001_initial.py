# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
        ('kalaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(max_length=200)),
                ('fecha_vencimiento', models.DateField()),
                ('subtotal', models.FloatField()),
                ('total', models.FloatField()),
                ('estado', models.CharField(default='A', max_length=1)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalaapp.Empresa')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.Paciente')),
            ],
            options={
                'db_table': 'facturas',
            },
        ),
    ]
