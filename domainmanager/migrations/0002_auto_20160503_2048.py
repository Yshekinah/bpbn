# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='salutation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Salutation'),
        ),
        migrations.AlterField(
            model_name='bloodline',
            name='parent_clan',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Clan'),
        ),
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
