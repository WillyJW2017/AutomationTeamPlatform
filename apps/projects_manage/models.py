import uuid

from datetime import datetime
from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=255, primary_key=True, verbose_name='Project Name', help_text='Project Name')
    key = models.CharField(max_length=255, null=True, blank=True, verbose_name='Project Abbreviations', help_text='Project Abbreviations')
    projectLead = models.CharField(max_length=50, null=True, blank=True,verbose_name='Project Leader', help_text='Project Leader')
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name='Project URL', help_text='Project URL')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')

    class Meta:
        verbose_name = 'ProjectName'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Sprints(models.Model):
    project = models.ForeignKey(Projects, verbose_name='Project Name', help_text='Project Name')
    name = models.CharField(max_length=255, verbose_name='Sprint Name', help_text='Sprint Name')
    startDate = models.DateField(verbose_name='Start Date', help_text='Start Date')
    endDate = models.DateField(verbose_name='End Date', help_text='End Date')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')
    last_update_user = models.CharField(default=None, max_length=100, verbose_name='Last Update User', help_text='Last Update User')
    last_update_time = models.DateTimeField(default=None, verbose_name='Last Update Time', help_text='Last Update Time')

    class Meta:
        verbose_name = 'SprintName'
        verbose_name_plural = verbose_name
        unique_together = ('project', 'name')

    def __str__(self):
        return self.name

class Releases(models.Model):
    project = models.ForeignKey(Projects, verbose_name='Project Name', help_text='Project Name')
    name = models.CharField(max_length=255, verbose_name='Release Name',help_text='Release Name')
    startDate = models.DateField(verbose_name='Start Date', help_text='Start Date')
    endDate = models.DateField(verbose_name='End Date', help_text='End Date')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')
    last_update_user = models.CharField(default=None, max_length=100, verbose_name='Last Update User',
                                        help_text='Last Update User')
    last_update_time = models.DateTimeField(default=None, verbose_name='Last Update Time', help_text='Last Update Time')

    class Meta:
        verbose_name = 'ReleaseName'
        verbose_name_plural = verbose_name
        unique_together = ('project', 'name')

    def __str__(self):
        return self.name

class Story(models.Model):
    project = models.ForeignKey(Projects, verbose_name='Project Name', help_text='Project Name')
    sprint = models.CharField(max_length=255, null=True, blank=True, verbose_name='Sprint Name', help_text='Sprint Name')
    release = models.CharField(max_length=255, null=True, blank=True, verbose_name='Release Name', help_text='Release Name')
    story_id = models.CharField(max_length=255, verbose_name='Story ID', help_text='Story ID')
    summary = models.CharField(max_length=255, null=True, blank=True, verbose_name='Story Summary', help_text='Story Summary')
    assignee = models.CharField(max_length=50, null=True, blank=True, verbose_name='Assignee', help_text='Assignee')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')
    last_update_user = models.CharField(default=None, max_length=100, verbose_name='Last Update User',
                                        help_text='Last Update User')
    last_update_time = models.DateTimeField(default=None, verbose_name='Last Update Time', help_text='Last Update Time')

    class Meta:
        verbose_name = 'StoryID'
        verbose_name_plural = verbose_name
        unique_together = ('project', 'story_id', 'sprint')

    def __str__(self):
        return self.story_id

class TestCases(models.Model):
    FRAMEWORK_CHOICES = (
        ('Selenium', 'Selenium'), ('Cucumber', 'Cucumber'), ('UFT', 'UFT'),
    )
    APPLICATION_CHOICES = (
        ('Web', 'Web'), ('Mobile', 'Mobile'), ('API', 'API'),
        ('Siebel', 'Siebel'), ('C/S', 'Client/Server'),
    )
    name = models.CharField(max_length=255, verbose_name='Test Case Name', help_text='Test Case Name')
    project = models.ForeignKey(Projects, verbose_name='Project Name', help_text='Project Name')
    functionArea = models.CharField(max_length=255, verbose_name='Function Area', help_text='Function Area')
    framework = models.CharField(max_length=20, choices=FRAMEWORK_CHOICES)
    application = models.CharField(max_length=20, choices=APPLICATION_CHOICES)
    tag = models.CharField(max_length=255, verbose_name='Tag', help_text='Tag')
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='Test Case Description', help_text='Test Case Description')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')
    updatePerson = models.CharField(max_length=50, default='', verbose_name='Last Update User', help_text='Last Update User')
    updateDate = models.DateField(default=None, verbose_name='Last Update Date', help_text='Last Update Date')

    class Meta:
        verbose_name = 'Test Case Name'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'project')

    def __str__(self):
        return self.name

class SubTestCases(models.Model):
    FRAMEWORK_CHOICES = (
        ('Selenium', 'Selenium'), ('Cucumber', 'Cucumber'), ('UFT', 'UFT'),
    )
    APPLICATION_CHOICES = (
        ('Web', 'Web'), ('Mobile', 'Mobile'), ('API', 'API'),
        ('Siebel', 'Siebel'), ('C/S', 'Client/Server'),
    )
    COUNTRY_CHOICES = (
        ('US', 'US'), ('UK', 'UK'), ('DE', 'DE'), ('JP', 'JP'),
        ('IT', 'IT'), ('FR', 'FR'), ('CHN', 'CHN'),
    )
    OS_CHOICES = (
        ('IOS', 'IOS'), ('Android', 'Android'),
    )
    PLATFORM_CHOICES = (
        ('iphone', 'iphone'), ('ipad', 'ipad'), ('androidPhone', 'androidPhone'), ('androidTablet', 'androidTablet'),
    )
    name = models.ForeignKey(TestCases, verbose_name='Test Case Name', help_text='Test Case Name')
    sub = models.ForeignKey(TestCases, related_name='subcases', null=True, blank=True)
    project = models.ForeignKey(Projects, verbose_name='Project Name', help_text='Project Name')
    framework = models.CharField(max_length=20, choices=FRAMEWORK_CHOICES)
    application = models.CharField(max_length=20, choices=APPLICATION_CHOICES)
    tag = models.CharField(max_length=255, verbose_name='Tag', help_text='Tag')
    functionArea = models.CharField(max_length=255, verbose_name='Function Area', help_text='Function Area')
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='Test Case Description',
                                   help_text='Test Case Description')
    os = models.CharField(max_length=20, choices=OS_CHOICES)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    # storyId = models.ForeignKey(Story, verbose_name='story id')
    storyId = models.CharField(max_length=255, null=True, blank=True, verbose_name='Story ID', help_text='Story ID')
    status = models.CharField(default='Todo', max_length=50, verbose_name='Test case Status', help_text='Test case Status')
    result = models.CharField(default='',null=True,blank=True, max_length=50, verbose_name='Execution Result', help_text='Execution Result')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')
    last_update_user = models.CharField(default='', max_length=100, verbose_name='Last Update User',
                                        help_text='Last Update User')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='Last Update Time', help_text='Last Update Time')


    class Meta:
        verbose_name = 'Sub Test Case'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'os', 'platform', 'country')

    def __str__(self):
        return self.storyId


































