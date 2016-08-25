# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0116_auto_20160823_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='agecategory',
            name='domain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Domain'),
        ),
        migrations.AddField(
            model_name='politicalfuntion',
            name='domain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Domain'),
        ),
    ]