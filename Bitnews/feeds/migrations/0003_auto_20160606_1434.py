# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20160606_0855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsfeeditems',
            options={'verbose_name_plural': 'News Feed Items'},
        ),
        migrations.RemoveField(
            model_name='newsfeeditems',
            name='description',
        ),
        migrations.RemoveField(
            model_name='newsfeeditems',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='newsfeeditems',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='newsfeeditems',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='newsfeeditems',
            name='image_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='newsfeeditems',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='newsfeeditems',
            name='pubdate',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='newsfeeditems',
            name='source',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newsfeeditems',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newsfeeditems',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
