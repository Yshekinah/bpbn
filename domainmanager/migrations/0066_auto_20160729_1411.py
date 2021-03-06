# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0065_auto_20160728_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterShopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Character')),
            ],
        ),
        migrations.AlterField(
            model_name='boon',
            name='approvedbygm',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default=1, max_length=100, no_check_for_status=True),
        ),
        migrations.AlterField(
            model_name='boon',
            name='approvedbyslave',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default=1, max_length=100, no_check_for_status=True),
        ),
    ]
