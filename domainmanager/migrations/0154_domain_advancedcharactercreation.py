# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0153_agecategory_startingbackgrounds'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='advancedcharactercreation',
            field=models.BooleanField(default=True),
        ),
    ]
