# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-19 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str1', tinymce.models.HTMLField()),
            ],
        ),
    ]
