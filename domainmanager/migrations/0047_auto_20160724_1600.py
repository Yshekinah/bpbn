# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-24 14:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0046_property_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='properties',
            field=models.ManyToManyField(through='domainmanager.CharacterProperty', to='domainmanager.Property'),
        ),
        migrations.AlterField(
            model_name='property',
            name='initial',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
