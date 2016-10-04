# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0132_auto_20161004_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='downtimes',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='domain',
            name='influences',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='domain',
            name='secrets',
            field=models.BooleanField(default=True),
        ),
    ]
