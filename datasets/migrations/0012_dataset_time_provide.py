# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0011_auto_20170113_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='time_provide',
            field=models.BooleanField(default=True),
        ),
    ]
