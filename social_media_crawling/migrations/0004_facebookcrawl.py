# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-18 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_crawling', '0003_auto_20170618_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookCrawl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=63206)),
                ('like', models.CharField(max_length=10, null=True)),
                ('comment', models.CharField(max_length=10, null=True)),
                ('share', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
