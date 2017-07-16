# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0005_tabel_berita_konten_berita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kalimat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kalimat', models.TextField()),
                ('tipe', models.CharField(max_length=10, null=True)),
                ('clean', models.TextField()),
                ('f2', models.DecimalField(decimal_places=4, max_digits=5)),
                ('f4', models.DecimalField(decimal_places=4, max_digits=5)),
                ('f5', models.DecimalField(decimal_places=4, max_digits=5)),
                ('accepted', models.BooleanField(default=False)),
                ('index_kalimat', models.IntegerField()),
                ('berita', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crawling.Tabel_Berita')),
            ],
        ),
    ]
