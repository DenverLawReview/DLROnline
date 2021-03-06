# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20170212_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='online_issue',
        ),
        migrations.RemoveField(
            model_name='article',
            name='print_issue',
        ),
        migrations.AddField(
            model_name='onlineissue',
            name='articles',
            field=models.ManyToManyField(blank=True, to='articles.Article'),
        ),
        migrations.AddField(
            model_name='printissue',
            name='articles',
            field=models.ManyToManyField(blank=True, to='articles.Article'),
        ),
    ]
