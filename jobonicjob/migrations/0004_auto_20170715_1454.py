# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobonicjob', '0003_auto_20170715_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_created',
            field=models.BooleanField(default=True),
        ),
    ]