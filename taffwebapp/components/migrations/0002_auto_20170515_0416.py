# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='component',
            name='thermal_charakter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='components.Component_thermal_charackter'),
        ),
    ]