# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_news_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pubdate',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
