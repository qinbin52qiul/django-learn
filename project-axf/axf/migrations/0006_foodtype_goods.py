# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-19 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0005_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=16)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=16)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.IntegerField(default=1)),
                ('pmdesc', models.CharField(max_length=100)),
                ('specifics', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('marketprice', models.FloatField(default=1)),
                ('categoryid', models.CharField(max_length=16)),
                ('childcid', models.CharField(max_length=16)),
                ('childcidname', models.CharField(max_length=100)),
                ('dealerid', models.CharField(max_length=16)),
                ('storenums', models.IntegerField(default=1)),
                ('productnum', models.IntegerField(default=1)),
            ],
        ),
    ]