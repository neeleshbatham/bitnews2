# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='new_tags',
            new_name='news_tags',
        ),
    ]
