# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-25 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobonicUsers', '0007_auto_20171125_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='global_login_key',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
