# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20170212_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlineissue',
            name='slug',
            field=models.SlugField(default='test-slug', max_length=100),
            preserve_default=False,
        ),
    ]
