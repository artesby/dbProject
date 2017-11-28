# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20171128_0107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistics',
            old_name='avg_attempt',
            new_name='success_rate',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='year',
        ),
        migrations.AddField(
            model_name='statistics',
            name='finish_date',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='start_date',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now),
            preserve_default=False,
        ),
    ]