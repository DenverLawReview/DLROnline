# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 02:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_onlineissue_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='printissue',
            options={'ordering': ['-volume', '-issue'], 'verbose_name': 'print issue', 'verbose_name_plural': 'print issues'},
        ),
        migrations.AlterUniqueTogether(
            name='printissue',
            unique_together=set([('volume', 'issue')]),
        ),
    ]
