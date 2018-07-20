# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-20 11:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Login Name', max_length=255, unique=True, verbose_name='Login Name')),
                ('password', models.CharField(help_text='Password', max_length=255, verbose_name='password')),
                ('name', models.CharField(blank=True, help_text='Nick Name', max_length=30, null=True, verbose_name='Nick Name')),
                ('email', models.CharField(blank=True, help_text='Email Address', max_length=100, null=True, verbose_name='Email Address')),
                ('avatar', models.CharField(blank=True, help_text='User Profile', max_length=500, null=True, verbose_name='User Profile')),
                ('currentProject', models.CharField(blank=True, help_text='Current Project Name', max_length=100, null=True, verbose_name='Current Project Name')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, help_text='Created Time', verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(default=datetime.datetime.now, help_text='Updated Time', verbose_name='Updated Time')),
            ],
            options={
                'verbose_name': 'UserName',
                'verbose_name_plural': 'UserName',
            },
        ),
    ]
