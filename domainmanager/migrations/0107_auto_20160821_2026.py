# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0106_auto_20160821_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='initalizeatcharactercreation',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'No')], default=2, verbose_name='Initialize at character creation'),
        ),
    ]
