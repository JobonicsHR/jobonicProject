# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobonicusers', '0003_jobonicuser_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobonicuser',
            name='company',
        ),
    ]