# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0004_tabel_berita'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabel_berita',
            name='konten_berita',
            field=models.TextField(null=True),
        ),
    ]
