# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20160601_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscategory',
            name='image_url',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=b'category-images'),
        ),
        migrations.AlterField(
            model_name='newslanguage',
            name='image_url',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=b'languages-images'),
        ),
    ]