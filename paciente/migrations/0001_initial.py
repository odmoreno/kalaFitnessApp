# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '0001_initial'),
        ('kalaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('n_hijos', models.PositiveSmallIntegerField(default=0)),
                ('observaciones', models.CharField(default='', max_length=200)),
                ('motivo_consulta', models.CharField(default='', max_length=200)),
                ('estado', models.CharField(default='A', max_length=1)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kalaapp.Usuario')),
            ],
            options={
                'db_table': 'paciente',
            },
        ),
        migrations.CreateModel(
            name='PacientePersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('estado', models.CharField(default='A', max_length=1)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Personal')),
            ],
            options={
                'db_table': 'paciente_personal',
            },
        ),
        migrations.AlterUniqueTogether(
            name='paciente',
            unique_together=set([('id', 'usuario')]),
        ),
    ]
