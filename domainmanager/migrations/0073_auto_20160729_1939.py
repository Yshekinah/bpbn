# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 17:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0072_auto_20160729_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='initalizecharactercreation',
            new_name='initalizeatcharactercreation',
        ),
    ]