# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0157_auto_20161115_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactercreation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charactercreation',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
