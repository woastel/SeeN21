# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_auto_20170512_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='component_thermal_charackter',
            name='required_air_flow',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='component_thermal_charackter',
            name='max_temperature',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
