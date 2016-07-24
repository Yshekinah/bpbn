# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-24 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0040_auto_20160724_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='sire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_sire', to='domainmanager.Character'),
        ),
        migrations.AlterField(
            model_name='characterdiscipline',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cd_character', to='domainmanager.Character'),
        ),
        migrations.AlterField(
            model_name='characterproperty',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cp_character', to='domainmanager.Character'),
        ),
    ]
