import django_filters
from django_filters import rest_framework as filters

from .models import Projects, Sprints


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

