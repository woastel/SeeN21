# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='climaticmeasurement',
            name='climaticmeasurevalues_ptr',
        ),
        migrations.AddField(
            model_name='climaticmeasurement',
            name='measurement_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='measurement.measurement'),
            preserve_default=False,
        ),
    ]