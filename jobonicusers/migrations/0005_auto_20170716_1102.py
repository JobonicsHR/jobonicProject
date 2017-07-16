# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobonicusers', '0004_remove_jobonicuser_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobonicuser',
            name='company',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='jobonicuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
