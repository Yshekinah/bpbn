# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0133_auto_20161004_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='agecategory',
            name='startingsecrets',
            field=models.IntegerField(default=4),
        ),
    ]
