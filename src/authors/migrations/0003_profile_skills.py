# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20160829_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]
