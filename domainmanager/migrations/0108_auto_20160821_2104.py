# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0107_auto_20160821_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='domain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Domain'),
        ),
    ]
