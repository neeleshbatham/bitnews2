# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20160606_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pubdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
