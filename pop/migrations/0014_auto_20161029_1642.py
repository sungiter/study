# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0013_auto_20161029_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='new',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='studying',
            field=models.TextField(),
        ),
    ]
