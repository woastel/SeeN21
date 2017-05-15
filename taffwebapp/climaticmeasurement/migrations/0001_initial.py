# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eut', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AmbientTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Climaticmeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField()),
                ('ambient_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='climaticmeasurement.AmbientTemp')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('eut_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eut.Eut')),
            ],
        ),
        migrations.CreateModel(
            name='MeasureValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('info', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SensorMax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_list', models.CharField(max_length=500)),
                ('max1', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max2', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max3', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max4', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max5', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max6', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max7', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max8', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max9', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max10', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max11', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max12', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max13', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max14', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max15', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max16', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max17', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max18', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max19', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max20', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max21', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max22', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max23', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max24', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max25', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max26', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max27', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max28', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max29', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max30', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max31', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max32', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max33', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max34', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max35', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max36', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max37', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max38', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max39', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max40', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max41', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max42', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max43', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max44', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max45', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max46', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max47', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max48', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max49', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max50', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max51', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max52', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max53', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max54', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max55', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max56', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max57', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max58', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max59', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max60', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='SensorName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_list', models.CharField(max_length=500)),
                ('name1', models.CharField(max_length=100)),
                ('name2', models.CharField(max_length=100)),
                ('name3', models.CharField(max_length=100)),
                ('name4', models.CharField(max_length=100)),
                ('name5', models.CharField(max_length=100)),
                ('name6', models.CharField(max_length=100)),
                ('name7', models.CharField(max_length=100)),
                ('name8', models.CharField(max_length=100)),
                ('name9', models.CharField(max_length=100)),
                ('name10', models.CharField(max_length=100)),
                ('name11', models.CharField(max_length=100)),
                ('name12', models.CharField(max_length=100)),
                ('name13', models.CharField(max_length=100)),
                ('name14', models.CharField(max_length=100)),
                ('name15', models.CharField(max_length=100)),
                ('name16', models.CharField(max_length=100)),
                ('name17', models.CharField(max_length=100)),
                ('name18', models.CharField(max_length=100)),
                ('name19', models.CharField(max_length=100)),
                ('name20', models.CharField(max_length=100)),
                ('name21', models.CharField(max_length=100)),
                ('name22', models.CharField(max_length=100)),
                ('name23', models.CharField(max_length=100)),
                ('name24', models.CharField(max_length=100)),
                ('name25', models.CharField(max_length=100)),
                ('name26', models.CharField(max_length=100)),
                ('name27', models.CharField(max_length=100)),
                ('name28', models.CharField(max_length=100)),
                ('name29', models.CharField(max_length=100)),
                ('name30', models.CharField(max_length=100)),
                ('name31', models.CharField(max_length=100)),
                ('name32', models.CharField(max_length=100)),
                ('name33', models.CharField(max_length=100)),
                ('name34', models.CharField(max_length=100)),
                ('name35', models.CharField(max_length=100)),
                ('name36', models.CharField(max_length=100)),
                ('name37', models.CharField(max_length=100)),
                ('name38', models.CharField(max_length=100)),
                ('name39', models.CharField(max_length=100)),
                ('name40', models.CharField(max_length=100)),
                ('name41', models.CharField(max_length=100)),
                ('name42', models.CharField(max_length=100)),
                ('name43', models.CharField(max_length=100)),
                ('name44', models.CharField(max_length=100)),
                ('name45', models.CharField(max_length=100)),
                ('name46', models.CharField(max_length=100)),
                ('name47', models.CharField(max_length=100)),
                ('name48', models.CharField(max_length=100)),
                ('name49', models.CharField(max_length=100)),
                ('name50', models.CharField(max_length=100)),
                ('name51', models.CharField(max_length=100)),
                ('name52', models.CharField(max_length=100)),
                ('name53', models.CharField(max_length=100)),
                ('name54', models.CharField(max_length=100)),
                ('name55', models.CharField(max_length=100)),
                ('name56', models.CharField(max_length=100)),
                ('name57', models.CharField(max_length=100)),
                ('name58', models.CharField(max_length=100)),
                ('name59', models.CharField(max_length=100)),
                ('name60', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typee', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SensorTypeList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_list', models.CharField(max_length=500)),
                ('typee1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='das', to='climaticmeasurement.SensorType')),
                ('typee10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Norrqrne', to='climaticmeasurement.SensorType')),
                ('typee11', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nobzbzbanifne', to='climaticmeasurement.SensorType')),
                ('typee12', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nosdfgdsne', to='climaticmeasurement.SensorType')),
                ('typee13', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nxcbone', to='climaticmeasurement.SensorType')),
                ('typee14', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonhrzne', to='climaticmeasurement.SensorType')),
                ('typee15', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Non7575e', to='climaticmeasurement.SensorType')),
                ('typee16', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No4538ne', to='climaticmeasurement.SensorType')),
                ('typee17', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No98689ne', to='climaticmeasurement.SensorType')),
                ('typee18', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No7287ne', to='climaticmeasurement.SensorType')),
                ('typee19', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No45ne', to='climaticmeasurement.SensorType')),
                ('typee2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='da431s', to='climaticmeasurement.SensorType')),
                ('typee20', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonecrwe', to='climaticmeasurement.SensorType')),
                ('typee21', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nocercne', to='climaticmeasurement.SensorType')),
                ('typee22', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nsgnetzbone', to='climaticmeasurement.SensorType')),
                ('typee23', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nwertone', to='climaticmeasurement.SensorType')),
                ('typee24', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nsdfgone', to='climaticmeasurement.SensorType')),
                ('typee25', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Noxvne', to='climaticmeasurement.SensorType')),
                ('typee26', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonss78698756645ge', to='climaticmeasurement.SensorType')),
                ('typee27', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nlkljkjsfhone', to='climaticmeasurement.SensorType')),
                ('typee28', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonwerge', to='climaticmeasurement.SensorType')),
                ('typee29', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonhte', to='climaticmeasurement.SensorType')),
                ('typee3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Non1234e', to='climaticmeasurement.SensorType')),
                ('typee30', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonasdfe', to='climaticmeasurement.SensorType')),
                ('typee31', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nunztone', to='climaticmeasurement.SensorType')),
                ('typee32', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonsdrgeegcrtgfge', to='climaticmeasurement.SensorType')),
                ('typee33', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nosdsdsdsdsddfgne', to='climaticmeasurement.SensorType')),
                ('typee34', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Non235234e', to='climaticmeasurement.SensorType')),
                ('typee35', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No46484ne', to='climaticmeasurement.SensorType')),
                ('typee36', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No523156ne', to='climaticmeasurement.SensorType')),
                ('typee37', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No45684ne', to='climaticmeasurement.SensorType')),
                ('typee38', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nokiysdne', to='climaticmeasurement.SensorType')),
                ('typee39', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No4684ne', to='climaticmeasurement.SensorType')),
                ('typee4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No234577456ne', to='climaticmeasurement.SensorType')),
                ('typee40', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Noxcvbxcne', to='climaticmeasurement.SensorType')),
                ('typee41', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nofghne', to='climaticmeasurement.SensorType')),
                ('typee42', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonfgne', to='climaticmeasurement.SensorType')),
                ('typee43', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nosdfne', to='climaticmeasurement.SensorType')),
                ('typee44', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonsdfe', to='climaticmeasurement.SensorType')),
                ('typee45', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nxcvbone', to='climaticmeasurement.SensorType')),
                ('typee46', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nosdfgnesdf', to='climaticmeasurement.SensorType')),
                ('typee47', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Noyssdfgne', to='climaticmeasurement.SensorType')),
                ('typee48', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nosdfgnesdfgne', to='climaticmeasurement.SensorType')),
                ('typee49', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Noddsdfgne', to='climaticmeasurement.SensorType')),
                ('typee5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No235ne', to='climaticmeasurement.SensorType')),
                ('typee50', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nosdfgne', to='climaticmeasurement.SensorType')),
                ('typee51', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nasfone', to='climaticmeasurement.SensorType')),
                ('typee52', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonrewfe', to='climaticmeasurement.SensorType')),
                ('typee53', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Noerfne', to='climaticmeasurement.SensorType')),
                ('typee54', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonasde', to='climaticmeasurement.SensorType')),
                ('typee55', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonyxcve', to='climaticmeasurement.SensorType')),
                ('typee56', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonfghjfe', to='climaticmeasurement.SensorType')),
                ('typee57', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonjke', to='climaticmeasurement.SensorType')),
                ('typee58', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonasfve', to='climaticmeasurement.SensorType')),
                ('typee59', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nonefdghdfgh', to='climaticmeasurement.SensorType')),
                ('typee6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nogebrene', to='climaticmeasurement.SensorType')),
                ('typee60', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nasdasdfa', to='climaticmeasurement.SensorType')),
                ('typee7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Noyvfbne', to='climaticmeasurement.SensorType')),
                ('typee8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nowerwene', to='climaticmeasurement.SensorType')),
                ('typee9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Noqwrwerne', to='climaticmeasurement.SensorType')),
            ],
        ),
        migrations.CreateModel(
            name='SensorValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_list', models.CharField(max_length=500)),
                ('value1', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value2', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value3', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value4', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value5', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value6', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value7', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value8', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value9', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value10', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value11', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value12', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value13', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value14', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value15', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value16', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value17', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value18', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value19', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value20', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value21', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value22', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value23', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value24', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value25', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value26', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value27', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value28', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value29', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value30', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value31', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value32', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value33', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value34', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value35', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value36', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value37', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value38', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value39', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value40', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value41', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value42', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value43', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value44', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value45', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value46', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value47', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value48', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value49', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value50', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value51', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value52', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value53', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value54', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value55', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value56', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value57', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value58', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value59', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value60', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='TestLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='measurevalues',
            name='sensorMax_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climaticmeasurement.SensorMax'),
        ),
        migrations.AddField(
            model_name='measurevalues',
            name='sensorName_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climaticmeasurement.SensorName'),
        ),
        migrations.AddField(
            model_name='measurevalues',
            name='sensorValue_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climaticmeasurement.SensorValue'),
        ),
        migrations.AddField(
            model_name='climaticmeasure',
            name='measureValues_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='climaticmeasurement.MeasureValues'),
        ),
        migrations.AddField(
            model_name='climaticmeasure',
            name='sensorTypeList_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climaticmeasurement.SensorTypeList'),
        ),
        migrations.AddField(
            model_name='climaticmeasure',
            name='testload_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='climaticmeasurement.TestLoad'),
        ),
    ]
