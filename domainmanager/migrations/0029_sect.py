# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0028_auto_20160720_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]