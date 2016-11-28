# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-26 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20161119_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='color',
            field=models.CharField(choices=[('red', 'red'), ('blue', 'blue'), ('green', 'green'), ('black', 'black')], default='blue', max_length=15, verbose_name='cor'),
        ),
    ]