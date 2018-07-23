import django_filters
from django_filters import rest_framework as filters

from .models import Projects, Sprints, Releases, Story, TestCases, SubTestCases


class ProjectsFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    class Meta:
        model = Projects
        fields = ['name']

class SprintsFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    project = django_filters.CharFilter(name='project', lookup_expr='exact')
    class Meta:
        model = Sprints
        fields = ['name', 'project']

class ReleasesFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    project = django_filters.CharFilter(name='project', lookup_expr='exact')
    class Meta:
        model = Releases
        fields = ['name', 'project']

class StoryFilter(filters.FilterSet):
    sprint = django_filters.CharFilter(name='sprint', lookup_expr='exact')
    release = django_filters.CharFilter(name='release', lookup_expr='exact')
    id = django_filters.CharFilter(name='story_id', lookup_expr='icontains')
    summary = django_filters.CharFilter(name='summary', lookup_expr='icontains')
    project = django_filters.CharFilter(name='project', lookup_expr='exact')
    class Meta:
        model = Story
        fields = ['sprint', 'release', 'id', 'summary', 'project']

class TestCaseFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    class Meta:
        model = TestCases
        fields = ['name']

class SubTestCaseFilter(filters.FilterSet):
    class Meta:
        model = SubTestCases
        fields = ['storyId', ]
