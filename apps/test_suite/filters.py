import django_filters
from django_filters import rest_framework as filters

from .models import TestSuite, TestSuiteResult, SubTestCaseResult

class TestSuiteFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    class Meta:
        model = TestSuite
        fields = ['name']

class TestSuiteResultFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='suiteId', lookup_expr='exact')
    class Meta:
        model = TestSuiteResult
        fields = ['name']