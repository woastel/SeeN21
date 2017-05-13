# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_auto_20170512_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='cable_charakter_avalible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='component',
            name='electronic_charakter_avalible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='component',
            name='mechanic_charakter_avalible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='component',
            name='thermal_charakter_avalible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='cable_charakter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='components.Component_cable_type'),
        ),
        migrations.AlterField(
            model_name='component',
            name='electronic_charakter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='components.Component_electronik_charackter'),
        ),
        migrations.AlterField(
            model_name='component',
            name='mechanic_charakter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='components.Component_mechanik_charackter'),
        ),
        migrations.AlterField(
            model_name='component',
            name='thermal_charakter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='components.Component_thermal_charackter'),
        ),
    ]
