# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0003_auto_20170512_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='cable_charakter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='components.Component_cable_type'),
        ),
        migrations.AlterField(
            model_name='component',
            name='electronic_charakter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='components.Component_electronik_charackter'),
        ),
        migrations.AlterField(
            model_name='component',
            name='mechanic_charakter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='components.Component_mechanik_charackter'),
        ),
        migrations.AlterField(
            model_name='component',
            name='thermal_charakter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='components.Component_thermal_charackter'),
        ),
    ]
