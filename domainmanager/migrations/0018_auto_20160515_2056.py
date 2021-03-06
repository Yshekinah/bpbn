# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0017_auto_20160515_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterDiscipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cd_character', to='domainmanager.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('clan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clan', to='domainmanager.Clan')),
            ],
        ),
        migrations.AlterField(
            model_name='characterproperty',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cp_character', to='domainmanager.Character'),
        ),
        migrations.AddField(
            model_name='characterdiscipline',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discipline', to='domainmanager.Discipline'),
        ),
    ]
