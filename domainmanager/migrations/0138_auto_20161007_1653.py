# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0137_secret_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genealogy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('generation', models.IntegerField(blank=True, default=10)),
                ('clan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Clan')),
                ('sire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Genealogy')),
            ],
        ),
        migrations.RemoveField(
            model_name='vampire',
            name='clan',
        ),
        migrations.RemoveField(
            model_name='vampire',
            name='sire',
        ),
        migrations.DeleteModel(
            name='Vampire',
        ),
    ]
