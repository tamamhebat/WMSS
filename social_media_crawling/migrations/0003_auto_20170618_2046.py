# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-18 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_crawling', '0002_auto_20170618_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittercrawl',
            name='Retweet_post',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='twittercrawl',
            name='Retweet_user',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='twittercrawl',
            name='hashtag',
            field=models.CharField(max_length=100, null=True),
        ),
    ]