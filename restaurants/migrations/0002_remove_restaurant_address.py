# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 07:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='address',
        ),
    ]
