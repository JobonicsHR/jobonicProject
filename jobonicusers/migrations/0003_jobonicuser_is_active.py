# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobonicusers', '0002_jobonicuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobonicuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]