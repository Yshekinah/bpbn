# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0115_auto_20160823_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='postcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='street',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
