# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 02:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pop', '0005_auto_20161023_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='item',
            old_name='catagory',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='score',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='user',
        ),
        migrations.AddField(
            model_name='master',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pop.Item'),
        ),
        migrations.AddField(
            model_name='master',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
