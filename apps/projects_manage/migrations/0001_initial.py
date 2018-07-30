# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-28 14:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('name', models.CharField(help_text='Project Name', max_length=255, primary_key=True, serialize=False, verbose_name='Project Name')),
                ('key', models.CharField(blank=True, help_text='Project Abbreviations', max_length=255, null=True, verbose_name='Project Abbreviations')),
                ('projectLead', models.CharField(blank=True, help_text='Project Leader', max_length=50, null=True, verbose_name='Project Leader')),
                ('url', models.CharField(blank=True, help_text='Project URL', max_length=255, null=True, verbose_name='Project URL')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, help_text='Created Time', verbose_name='Created Time')),
            ],
            options={
                'verbose_name': 'ProjectName',
                'verbose_name_plural': 'ProjectName',
            },
        ),
        migrations.CreateModel(
            name='Releases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Release Name', max_length=255, verbose_name='Release Name')),
                ('startDate', models.DateField(help_text='Start Date', verbose_name='Start Date')),
                ('endDate', models.DateField(help_text='End Date', verbose_name='End Date')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, help_text='Created Time', verbose_name='Created Time')),
                ('last_update_user', models.CharField(blank=True, default='', help_text='Last Update User', max_length=100, null=True, verbose_name='Last Update User')),
                ('last_update_time', models.DateTimeField(default=datetime.datetime.now, help_text='Last Update Time', verbose_name='Last Update Time')),
                ('project', models.ForeignKey(help_text='Project Name', on_delete=django.db.models.deletion.CASCADE, to='projects_manage.Projects', verbose_name='Project Name')),
            ],
            options={
                'verbose_name': 'ReleaseName',
                'verbose_name_plural': 'ReleaseName',
            },
        ),
        migrations.CreateModel(
            name='Sprints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Sprint Name', max_length=255, verbose_name='Sprint Name')),
                ('startDate', models.DateField(help_text='Start Date', verbose_name='Start Date')),
                ('endDate', models.DateField(help_text='End Date', verbose_name='End Date')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, help_text='Created Time', verbose_name='Created Time')),
                ('last_update_user', models.CharField(blank=True, default='', help_text='Last Update User', max_length=100, null=True, verbose_name='Last Update User')),
                ('last_update_time', models.DateTimeField(default=datetime.datetime.now, help_text='Last Update Time', verbose_name='Last Update Time')),
                ('project', models.ForeignKey(help_text='Project Name', on_delete=django.db.models.deletion.CASCADE, to='projects_manage.Projects', verbose_name='Project Name')),
            ],
            options={
                'verbose_name': 'SprintName',
                'verbose_name_plural': 'SprintName',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sprint', models.CharField(blank=True, help_text='Sprint Name', max_length=255, null=True, verbose_name='Sprint Name')),
                ('release', models.CharField(blank=True, help_text='Release Name', max_length=255, null=True, verbose_name='Release Name')),
                ('story_id', models.CharField(help_text='Story ID', max_length=255, verbose_name='Story ID')),
                ('summary', models.CharField(blank=True, help_text='Story Summary', max_length=255, null=True, verbose_name='Story Summary')),
                ('assignee', models.CharField(blank=True, help_text='Assignee', max_length=50, null=True, verbose_name='Assignee')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, help_text='Created Time', verbose_name='Created Time')),
                ('last_update_user', models.CharField(blank=True, default='', help_text='Last Update User', max_length=100, null=True, verbose_name='Last Update User')),
                ('last_update_time', models.DateTimeField(default=datetime.datetime.now, help_text='Last Update Time', verbose_name='Last Update Time')),
                ('project', models.ForeignKey(help_text='Project Name', on_delete=django.db.models.deletion.CASCADE, to='projects_manage.Projects', verbose_name='Project Name')),
            ],
            options={
                'verbose_name': 'StoryID',
                'verbose_name_plural': 'StoryID',
            },
        ),
        migrations.CreateModel(
            name='SubTestCases',
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
                ('created_time', models.DateTimeField(default=datetime.datetime.now, help_text='Created Time', verbose_name='Created Time')),
                ('last_update_user', models.CharField(blank=True, default='', help_text='Last Update User', max_length=100, null=True, verbose_name='Last Update User')),
                ('last_update_time', models.DateTimeField(default=datetime.datetime.now, help_text='Last Update Time', verbose_name='Last Update Time')),
            ],
            options={
                'verbose_name': 'Sub Test Case',
                'verbose_name_plural': 'Sub Test Case',
            },
        ),
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Test Case Name', max_length=255, verbose_name='Test Case Name')),
                ('functionArea', models.CharField(help_text='Function Area', max_length=255, verbose_name='Function Area')),
                ('framework', models.CharField(choices=[('Selenium', 'Selenium'), ('Cucumber', 'Cucumber'), ('UFT', 'UFT')], max_length=20)),
                ('application', models.CharField(choices=[('Web', 'Web'), ('Mobile', 'Mobile'), ('API', 'API'), ('Siebel', 'Siebel'), ('C/S', 'Client/Server')], max_length=20)),
                ('tag', models.CharField(help_text='Tag', max_length=255, verbose_name='Tag')),
                ('description', models.CharField(blank=True, help_text='Test Case Description', max_length=500, null=True, verbose_name='Test Case Description')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, help_text='Created Time', verbose_name='Created Time')),
                ('updatePerson', models.CharField(blank=True, default='', help_text='Last Update User', max_length=50, null=True, verbose_name='Last Update User')),
                ('updateDate', models.DateField(default='2018-07-28', help_text='Last Update Date', verbose_name='Last Update Date')),
                ('project', models.ForeignKey(help_text='Project Name', on_delete=django.db.models.deletion.CASCADE, to='projects_manage.Projects', verbose_name='Project Name')),
            ],
            options={
                'verbose_name': 'Test Case Name',
                'verbose_name_plural': 'Test Case Name',
            },
        ),
        migrations.AddField(
            model_name='subtestcases',
            name='name',
            field=models.ForeignKey(help_text='Test Case Name', on_delete=django.db.models.deletion.CASCADE, to='projects_manage.TestCases', verbose_name='Test Case Name'),
        ),
        migrations.AddField(
            model_name='subtestcases',
            name='project',
            field=models.ForeignKey(help_text='Project Name', on_delete=django.db.models.deletion.CASCADE, to='projects_manage.Projects', verbose_name='Project Name'),
        ),
        migrations.AddField(
            model_name='subtestcases',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcases', to='projects_manage.TestCases'),
        ),
        migrations.AlterUniqueTogether(
            name='testcases',
            unique_together=set([('name', 'project')]),
        ),
        migrations.AlterUniqueTogether(
            name='subtestcases',
            unique_together=set([('name', 'os', 'platform', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='story',
            unique_together=set([('project', 'story_id', 'sprint')]),
        ),
        migrations.AlterUniqueTogether(
            name='sprints',
            unique_together=set([('project', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='releases',
            unique_together=set([('project', 'name')]),
        ),
    ]
