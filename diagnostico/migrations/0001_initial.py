# -*- coding: utf-8 -*-

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
                ('fecha', models.DateField(auto_now_add=True)),
                ('altura', models.FloatField(default=0)),
                ('peso', models.FloatField(default=0)),
                ('imc', models.FloatField(default=0)),
                ('musculo', models.FloatField(default=0)),
                ('grasa_visceral', models.FloatField(default=0)),
                ('grasa_porcentaje', models.FloatField(default=0)),
                ('cuello', models.FloatField(default=0)),
                ('hombros', models.FloatField(default=0)),
                ('pecho', models.FloatField(default=0)),
                ('brazo_derecho', models.FloatField(default=0)),
                ('brazo_izquierdo', models.FloatField(default=0)),
                ('antebrazo_derecho', models.FloatField(default=0)),
                ('antebrazo_izquierdo', models.FloatField(default=0)),
                ('cintura', models.FloatField(default=0)),
                ('cadera', models.FloatField(default=0)),
                ('muslo_derecho', models.FloatField(default=0)),
                ('muslo_izquierdo', models.FloatField(default=0)),
                ('pantorrilla_derecha', models.FloatField(default=0)),
                ('pantorrilla_izquierda', models.FloatField(default=0)),
                ('flexiones', models.PositiveSmallIntegerField(default=0)),
                ('cadera_arriba', models.PositiveSmallIntegerField(default=0)),
                ('abdomen', models.PositiveSmallIntegerField(default=0)),
                ('espinales', models.PositiveSmallIntegerField(default=0)),
                ('lumbares', models.PositiveSmallIntegerField(default=0)),
                ('sentadillas', models.PositiveSmallIntegerField(default=0)),
                ('condiciones_previas', models.CharField(default='', max_length=200)),
                ('area_afectada', models.CharField(default='', max_length=200)),
                ('receta', models.CharField(default='', max_length=200)),
                ('rutina', models.CharField(default='', max_length=200)),
                ('estado', models.CharField(default='A', max_length=1)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='paciente.Paciente')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal.Personal')),
            ],
            options={
                'db_table': 'diagnostico',
            },
        ),
    ]
