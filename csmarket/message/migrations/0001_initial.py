# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-24 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_name', models.CharField(max_length=30, verbose_name='类别标题')),
                ('cate_time', models.DateTimeField(verbose_name='添加时间')),
                ('cate_num', models.IntegerField(unique=True, verbose_name='类别编号')),
            ],
            options={
                'verbose_name_plural': '信息类别管理',
                'verbose_name': '信息类别',
                'db_table': 'cate_message_table',
            },
        ),
    ]