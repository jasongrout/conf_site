# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-25 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_sponsorship', '0002_auto_20160517_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='added',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='added'),
        ),
    ]