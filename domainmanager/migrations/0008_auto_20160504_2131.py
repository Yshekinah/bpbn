# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0007_auto_20160503_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vampire',
            name='column',
        ),
        migrations.AddField(
            model_name='vampire',
            name='columnEnd',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='vampire',
            name='columnStart',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
