# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-20 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('condiciones_previas', models.CharField(default='', max_length=1000)),
                ('area_afectada', models.CharField(default='', max_length=1000)),
                ('receta', models.CharField(default='', max_length=1000)),
                ('estado', models.CharField(default='A', max_length=1)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='paciente.Paciente')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal.Personal')),
            ],
            options={
                'db_table': 'diagnostico',
            },
        ),
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'rutina',
            },
        ),
        migrations.CreateModel(
            name='Subrutina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('nombre', models.CharField(default='', max_length=1000)),
                ('detalle', models.CharField(default='', max_length=1000)),
                ('veces', models.PositiveSmallIntegerField(default=0)),
                ('repeticiones', models.PositiveSmallIntegerField(default=0)),
                ('descanso', models.PositiveSmallIntegerField(default=0)),
                ('link', models.URLField(default='', max_length=500)),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'subrutina',
            },
        ),
        migrations.AddField(
            model_name='rutina',
            name='subrutina',
            field=models.ManyToManyField(to='diagnostico.Subrutina'),
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='rutina',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='diagnostico.Rutina'),
        ),
    ]
