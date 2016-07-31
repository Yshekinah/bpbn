# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-27 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0053_propertytype_xpmultiplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xpspent',
            old_name='value',
            new_name='oldvalue',
        ),
        migrations.AddField(
            model_name='xpspent',
            name='newvalue',
            field=models.IntegerField(default=1),
        ),
    ]