# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 02:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0015_auto_20161029_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistics',
            old_name='new',
            new_name='statistics',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='remembered',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='studying',
        ),
    ]
