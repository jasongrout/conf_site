# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-16 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_schedule', '0006_content_override_html_is_not_editable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='abstract_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
    ]