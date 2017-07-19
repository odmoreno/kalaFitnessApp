# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('serie', models.CharField(max_length=10, unique=True)),
                ('fecha_vencimiento', models.DateField(default=django.utils.timezone.now)),
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
