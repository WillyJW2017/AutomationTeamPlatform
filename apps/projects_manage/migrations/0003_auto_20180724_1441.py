# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-24 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_manage', '0002_auto_20180723_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='assignee',
            field=models.CharField(blank=True, help_text='Assignee', max_length=50, null=True, verbose_name='Assignee'),
        ),
        migrations.AlterField(
            model_name='story',
            name='release',
            field=models.CharField(blank=True, help_text='Release Name', max_length=255, null=True, verbose_name='Release Name'),
        ),
        migrations.AlterField(
            model_name='story',
            name='sprint',
            field=models.CharField(blank=True, help_text='Sprint Name', max_length=255, null=True, verbose_name='Sprint Name'),
        ),
        migrations.AlterField(
            model_name='story',
            name='summary',
            field=models.CharField(blank=True, help_text='Story Summary', max_length=255, null=True, verbose_name='Story Summary'),
        ),
    ]
