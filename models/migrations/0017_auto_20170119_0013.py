# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0016_artmmodel_text_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artmmodel',
            name='text_id',
            field=models.TextField(default=''),
        ),
    ]