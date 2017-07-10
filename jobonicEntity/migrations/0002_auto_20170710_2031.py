# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobonicEntity', '0001_initial'),
        ('jobonicsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entityprofile',
            name='company_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobonicsapp.EntitySize'),
        ),
        migrations.AddField(
            model_name='entityprofile',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobonicsapp.Country'),
        ),
        migrations.AddField(
            model_name='entityprofile',
            name='entity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobonicEntity.Entity'),
        ),
        migrations.AddField(
            model_name='entityprofile',
            name='primary_industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobonicsapp.Industry'),
        ),
    ]
