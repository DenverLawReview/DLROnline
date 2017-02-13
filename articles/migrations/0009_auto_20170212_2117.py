# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20170212_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlineissue',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='onlineissue',
            name='visible',
        ),
        migrations.RemoveField(
            model_name='printissue',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='printissue',
            name='visible',
        ),
        migrations.AddField(
            model_name='article',
            name='online_issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.OnlineIssue'),
        ),
        migrations.AddField(
            model_name='article',
            name='print_issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.PrintIssue'),
        ),
    ]
