# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_collegepages_keyword_search_science'),
    ]

    operations = [
        migrations.CreateModel(
            name='twitter_tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('tweet_text', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('favourite_count', models.IntegerField()),
            ],
        ),
    ]
