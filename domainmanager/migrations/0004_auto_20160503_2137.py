# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0003_vampire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vampire',
            name='sire',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='master', to='domainmanager.Vampire'),
        ),
    ]
