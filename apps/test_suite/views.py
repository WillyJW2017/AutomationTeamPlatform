import json
from datetime import datetime
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from collections import OrderedDict
from django_filters.rest_framework import DjangoFilterBackend

from .models import TestSuite, TestSuiteResult, SubTestCaseResult
from .serializers import TestSuiteSerializer, TestSuiteResultSerializer, SubTestCaseResultSerializer
from .filters import TestSuiteFilter, TestSuiteResultFilter

class TestSuitePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 50

    def get_paginated_response(self, data):
        for list_data in data:
            list_data['cases'] = list_data['cases'].split(',')
            list_data['config'] = json.loads(list_data['config'])

        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('suites', data)
        ]))

class TestSuiteViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = TestSuite.objects.all().order_by('name')
    serializer_class = TestSuiteSerializer
    pagination_class = TestSuitePagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = TestSuiteFilter

class TestSuiteOperateViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteSerializer

    def create(self, request, *args, **kwargs):
        cases = self.request.data['suite']['cases']
        config = self.request.data['suite']['config']
        self.request.data['suite']['cases'] = ','.join(cases)
        self.request.data['suite']['config'] = json.dumps(config)

        serializer = self.get_serializer(data=request.data['suite'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        request_url = self.request._request.path
        if '/suite/batch-delete/' in request_url:
            delete_id = self.request.query_params.get('ids')
        elif '/suite/delete/' in request_url:
            delete_id = self.request.query_params.get('id')
        else:
            delete_id = ''

        if (delete_id != '') and (delete_id is not None):
            delete_id_list = delete_id.split(',')
            for del_id in delete_id_list:
                queryset = TestSuite.objects.filter(id__exact=del_id)
                queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class TestSuiteResultPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 50

    def get_paginated_response(self, data):
        for list_data in data:
            list_data['config'] = json.loads(list_data['config'])
        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('suiteResults', data)
        ]))

class TestSuiteResultViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = TestSuiteResult.objects.all().order_by('startTime')
    serializer_class = TestSuiteResultSerializer
    pagination_class = TestSuiteResultPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = TestSuiteResultFilter

















