# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 12:14
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0066_auto_20160729_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='boon',
            name='approvedbymaster',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default=1, max_length=100, no_check_for_status=True),
        ),
        migrations.AddField(
            model_name='boon',
            name='approvedbymaster_note',
            field=models.TextField(default='Place for additional notes'),
        ),
    ]
