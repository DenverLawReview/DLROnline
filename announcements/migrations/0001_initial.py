# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('published', models.BooleanField()),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
