# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0015_auto_20170118_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='artmmodel',
            name='text_id',
            field=models.TextField(default='xxx'),
        ),
    ]
