# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 17:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0111_auto_20160823_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='description',
        ),
    ]
