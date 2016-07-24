# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-23 07:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0038_auto_20160721_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='domain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property_domain', to='domainmanager.Domain'),
        ),
        migrations.AddField(
            model_name='propertytype',
            name='domain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='propertytype_domain', to='domainmanager.Domain'),
        ),
        migrations.AlterField(
            model_name='characterproperty',
            name='value',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
