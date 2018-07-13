from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(models.Model):
    '''
    User Information
    '''
    username = models.CharField(max_length=255, unique=True, verbose_name='Login Name', help_text='Login Name')
    password = models.CharField(max_length=255, null=False, blank=False, verbose_name='password', help_text='Password')
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Nick Name', help_text='Nick Name')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='Email Address', help_text='Email Address')
    avatar = models.CharField(max_length=500, null=True, blank=True, verbose_name='User Profile', help_text='User Profile')
    currentProject = models.CharField(max_length=100, null=True, blank=True, verbose_name='Current Project Name', help_text='Current Project Name')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='Created Time', help_text='Created Time')
    updated_time = models.DateTimeField(default=datetime.now, verbose_name='Updated Time', help_text='Updated Time')

    class Meta:
        verbose_name = 'UserName'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
