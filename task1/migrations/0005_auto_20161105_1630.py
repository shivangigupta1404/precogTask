# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-05 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0004_auto_20161105_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='retweet',
            old_name='type',
            new_name='category',
        ),
    ]
