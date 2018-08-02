# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-02 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcases',
            name='updateDate',
            field=models.DateField(default='2018-08-02', help_text='Last Update Date', verbose_name='Last Update Date'),
        ),
        migrations.AlterUniqueTogether(
            name='story',
            unique_together=set([('project', 'story_id', 'sprint')]),
        ),
    ]
