# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import domainmanager.models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0127_property_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('attachment', models.FileField(blank=True, null=True, upload_to=domainmanager.models.set_upload_directory_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Actions',
            },
        ),
        migrations.CreateModel(
            name='Downtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start', models.DateField(auto_now=True)),
                ('end', models.DateField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Domain')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Event')),
            ],
            options={
                'verbose_name_plural': 'Downtimes',
            },
        ),
    ]