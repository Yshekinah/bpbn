# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0084_auto_20160803_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='thumbnail',
            new_name='thumb',
        ),
    ]
