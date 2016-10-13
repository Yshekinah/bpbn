# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import domainmanager.models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0145_auto_20161013_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=domainmanager.models.set_upload_directory_path),
        ),
    ]
