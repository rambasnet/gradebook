# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-16 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avg',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='test3',
            field=models.FloatField(default=0),
        ),
    ]
