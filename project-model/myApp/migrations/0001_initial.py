# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-17 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20)),
                ('gdate', models.DateTimeField()),
                ('ggrilnum', models.IntegerField()),
                ('gboynum', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'grades',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(db_column='name', max_length=20)),
                ('sgender', models.BooleanField(db_column='gender', default=False)),
                ('sage', models.IntegerField(db_column='age')),
                ('scontent', models.CharField(db_column='content', max_length=30)),
                ('isDelete', models.BooleanField(db_column='isDelete', default=False)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('lastTime', models.DateTimeField(auto_now=True)),
                ('sgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Grades')),
            ],
            options={
                'db_table': 'students',
                'ordering': ['id'],
            },
        ),
    ]