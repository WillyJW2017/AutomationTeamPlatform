from datetime import datetime
from django.db import models

# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=255, primary_key=True, null=False, blank=False, verbose_name='Project Name', help_text='Project Name')
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
    project = models.ForeignKey(Projects, verbose_name='Project Name')
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Sprint Name', help_text='Sprint Name')
    startDate = models.DateField(verbose_name='Start Date', help_text='Start Date')
    endDate = models.DateField(verbose_name='End Date', help_text='End Date')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')

    class Meta:
        verbose_name = 'SprintName'
        verbose_name_plural = verbose_name
        unique_together = ('project', 'name')

    def __str__(self):
        return self.name

