# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-01 17:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTestCaseResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('framework', models.CharField(choices=[('Selenium', 'Selenium'), ('Cucumber', 'Cucumber'), ('UFT', 'UFT')], max_length=20)),
                ('application', models.CharField(choices=[('Web', 'Web'), ('Mobile', 'Mobile'), ('API', 'API'), ('Siebel', 'Siebel'), ('C/S', 'Client/Server')], max_length=20)),
                ('tag', models.CharField(help_text='Tag', max_length=255, verbose_name='Tag')),
                ('functionArea', models.CharField(help_text='Function Area', max_length=255, verbose_name='Function Area')),
                ('description', models.CharField(blank=True, help_text='Test Case Description', max_length=500, null=True, verbose_name='Test Case Description')),
                ('os', models.CharField(choices=[('IOS', 'IOS'), ('Android', 'Android')], max_length=20)),
                ('platform', models.CharField(choices=[('iphone', 'iphone'), ('ipad', 'ipad'), ('androidPhone', 'androidPhone'), ('androidTablet', 'androidTablet')], max_length=50)),
                ('country', models.CharField(choices=[('US', 'US'), ('UK', 'UK'), ('DE', 'DE'), ('JP', 'JP'), ('IT', 'IT'), ('FR', 'FR'), ('CHN', 'CHN')], max_length=20)),
                ('storyId', models.CharField(blank=True, help_text='Story ID', max_length=255, null=True, verbose_name='Story ID')),
                ('status', models.CharField(default='Todo', help_text='Test case Status', max_length=50, verbose_name='Test case Status')),
                ('result', models.CharField(blank=True, default='', help_text='Execution Result', max_length=50, null=True, verbose_name='Execution Result')),
                ('issueType', models.CharField(blank=True, default='', help_text='Issue Type', max_length=50, null=True, verbose_name='Issue Type')),
                ('comments', models.CharField(blank=True, default='', help_text='Comments', max_length=5000, null=True, verbose_name='Comments')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, help_text='Created Time', verbose_name='Created Time')),
                ('updatePerson', models.CharField(blank=True, default='', help_text='Last Update User', max_length=50, null=True, verbose_name='Last Update User')),
                ('updateTime', models.DateTimeField(default=datetime.datetime.now, help_text='Last Update Date', verbose_name='Last Update Date')),
                ('case_name', models.ForeignKey(help_text='Sub Case Name', on_delete=django.db.models.deletion.CASCADE, to='projects_manage.SubTestCases', verbose_name='Sub Case Name')),
                ('project', models.ForeignKey(help_text='Project Name', on_delete=django.db.models.deletion.CASCADE, to='projects_manage.Projects', verbose_name='Project Name')),
            ],
            options={
                'verbose_name': 'Sub Test Case Result',
                'verbose_name_plural': 'Sub Test Case Result',
            },
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Test Suite Name', max_length=255, verbose_name='Test Suite Name')),
                ('application', models.CharField(choices=[('Web', 'Web'), ('Mobile', 'Mobile'), ('API', 'API'), ('Siebel', 'Siebel'), ('C/S', 'Client/Server')], max_length=20)),
                ('framework', models.CharField(choices=[('Selenium', 'Selenium'), ('Cucumber', 'Cucumber'), ('UFT', 'UFT')], max_length=20)),
                ('cases', models.CharField(blank=True, help_text='Test Case ID', max_length=5000, null=True, verbose_name='Test Case ID')),
                ('config', models.CharField(blank=True, help_text='Run Config Info', max_length=5000, null=True, verbose_name='Run Config Info')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, help_text='Created Time', verbose_name='Created Time')),
                ('updatePerson', models.CharField(blank=True, default='', help_text='Last Update User', max_length=50, null=True, verbose_name='Last Update User')),
                ('updateDate', models.DateField(default='2018-08-01', help_text='Last Update Date', verbose_name='Last Update Date')),
                ('project', models.ForeignKey(help_text='Project Name', on_delete=django.db.models.deletion.CASCADE, to='projects_manage.Projects', verbose_name='Project Name')),
            ],
            options={
                'verbose_name': 'Test Suite',
                'verbose_name_plural': 'Test Suite',
            },
        ),
        migrations.CreateModel(
            name='TestSuiteResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField(default=datetime.datetime.now, help_text='Start Time', verbose_name='Start Time')),
                ('endTime', models.DateTimeField(default=datetime.datetime.now, help_text='End Time', verbose_name='End Time')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, help_text='Created Time', verbose_name='Created Time')),
                ('project', models.ForeignKey(help_text='Project Name', on_delete=django.db.models.deletion.CASCADE, to='projects_manage.Projects', verbose_name='Project Name')),
                ('suiteId', models.ForeignKey(help_text='Test Suite Name', on_delete=django.db.models.deletion.CASCADE, to='test_suite.TestSuite', verbose_name='Test Suite Name')),
            ],
            options={
                'verbose_name': 'Test Suite Result',
                'verbose_name_plural': 'Test Suite Result',
            },
        ),
        migrations.AddField(
            model_name='subtestcaseresult',
            name='test_suit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='test_suite.TestSuiteResult'),
        ),
        migrations.AlterUniqueTogether(
            name='testsuite',
            unique_together=set([('name', 'project')]),
        ),
    ]
