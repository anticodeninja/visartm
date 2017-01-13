# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0006_term_model_id'),
        ('visual', '0004_topterm_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTopicRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.FloatField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Document')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visual.ArtmModel')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visual.Topic')),
            ],
        ),
    ]
