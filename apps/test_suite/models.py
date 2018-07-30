import time
from datetime import datetime
from django.db import models

from projects_manage.models import Projects
from projects_manage.models import SubTestCases


class TestSuite(models.Model):
    FRAMEWORK_CHOICES = (
        ('Selenium', 'Selenium'), ('Cucumber', 'Cucumber'), ('UFT', 'UFT'),
    )
    APPLICATION_CHOICES = (
        ('Web', 'Web'), ('Mobile', 'Mobile'), ('API', 'API'),
        ('Siebel', 'Siebel'), ('C/S', 'Client/Server'),
    )
    name = models.CharField(max_length=255, verbose_name='Test Suite Name', help_text='Test Suite Name')
    project = models.ForeignKey(Projects, verbose_name='Project Name', help_text='Project Name')
    application = models.CharField(max_length=20, choices=APPLICATION_CHOICES)
    framework = models.CharField(max_length=20, choices=FRAMEWORK_CHOICES)
    cases = models.CharField(max_length=5000, null=True, blank=True, verbose_name='Test Case ID', help_text='Test Case ID')
    config = models.CharField(max_length=5000, null=True, blank=True, verbose_name='Run Config Info', help_text='Run Config Info')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')
    updatePerson = models.CharField(max_length=50, default='', null=True, blank=True, verbose_name='Last Update User',
                                    help_text='Last Update User')
    updateDate = models.DateField(default=time.strftime('%Y-%m-%d',time.localtime(time.time())), verbose_name='Last Update Date', help_text='Last Update Date')

    class Meta:
        verbose_name = 'Test Suite'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'project')

    def __str__(self):
        return self.name


class TestSuiteResult(models.Model):
    suiteId = models.ForeignKey(TestSuite, verbose_name='Test Suite Name', help_text='Test Suite Name')
    project = models.ForeignKey(Projects, verbose_name='Project Name', help_text='Project Name')
    startTime = models.DateTimeField(default=datetime.now, verbose_name='Start Time', help_text='Start Time')
    endTime = models.DateTimeField(default=datetime.now, verbose_name='End Time', help_text='End Time')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')
    class Meta:
        verbose_name = 'Test Suite Result'
        verbose_name_plural = verbose_name
        # unique_together = ('name', 'os', 'platform', 'country')

    def __str__(self):
        return self.suiteId

class SubTestCaseResult(models.Model):
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
    case_name = models.ForeignKey(SubTestCases, verbose_name='Sub Case Name', help_text='Sub Case Name')
    test_suit = models.ForeignKey(TestSuiteResult, related_name='details', null=True, blank=True)
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
    storyId = models.CharField(max_length=255, null=True, blank=True, verbose_name='Story ID', help_text='Story ID')
    status = models.CharField(default='Todo', max_length=50, verbose_name='Test case Status',
                              help_text='Test case Status')
    result = models.CharField(default='', null=True, blank=True, max_length=50, verbose_name='Execution Result',
                              help_text='Execution Result')
    issueType = models.CharField(default='', null=True, blank=True, max_length=50, verbose_name='Issue Type', help_text='Issue Type')
    comments = models.CharField(default='', null=True, blank=True, max_length=5000, verbose_name='Comments', help_text='Comments')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')
    updatePerson = models.CharField(max_length=50, default='', null=True, blank=True, verbose_name='Last Update User',
                                    help_text='Last Update User')
    updateTime = models.DateTimeField(default=datetime.now, verbose_name='Last Update Date', help_text='Last Update Date')

    class Meta:
        verbose_name = 'Sub Test Case Result'
        verbose_name_plural = verbose_name
        # unique_together = ('name', 'os', 'platform', 'country')

    def __str__(self):
        return self.name.name


