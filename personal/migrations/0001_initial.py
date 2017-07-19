# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kalaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(default='A', max_length=1)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kalaapp.Usuario')),
            ],
            options={
                'db_table': 'personal',
            },
        ),
        migrations.AlterUniqueTogether(
            name='personal',
            unique_together=set([('id', 'usuario')]),
        ),
    ]
