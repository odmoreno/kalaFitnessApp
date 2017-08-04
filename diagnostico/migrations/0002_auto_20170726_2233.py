# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('personal', '0001_initial'),
        ('diagnostico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosticoNutricion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('condiciones_previas', models.CharField(default='', max_length=1000)),
                ('area_afectada', models.CharField(default='', max_length=1000)),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'diagnostico_nut',
            },
        ),
        migrations.CreateModel(
            name='Dieta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'dieta',
            },
        ),
        migrations.CreateModel(
            name='PlanNutDiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('dia', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado'), ('Domingo', 'Domingo')], default='Lunes', max_length=30)),
                ('desayuno', models.CharField(default='', max_length=1000)),
                ('colacion1', models.CharField(default='', max_length=1000)),
                ('almuerzo', models.CharField(default='', max_length=1000)),
                ('colacion2', models.CharField(default='', max_length=1000)),
                ('cena', models.CharField(default='', max_length=1000)),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'plan_nut_diario',
            },
        ),
        migrations.RenameModel(
            old_name='Diagnostico',
            new_name='DiagnosticoFisioterapia',
        ),
        migrations.AlterModelTable(
            name='diagnosticofisioterapia',
            table='diagnostico_fis',
        ),
        migrations.AddField(
            model_name='dieta',
            name='plan_nut_diario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagnostico.PlanNutDiario'),
        ),
        migrations.AddField(
            model_name='diagnosticonutricion',
            name='dieta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='diagnostico.Dieta'),
        ),
        migrations.AddField(
            model_name='diagnosticonutricion',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='paciente.Paciente'),
        ),
        migrations.AddField(
            model_name='diagnosticonutricion',
            name='personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal.Personal'),
        ),
    ]