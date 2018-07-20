from datetime import datetime
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from collections import OrderedDict
from django_filters.rest_framework import DjangoFilterBackend

from .models import Story, TestCases, SubTestCases
from .serializers import StorySerializer, StoryUpdateInfoSerializer, TestCaseSerializer, TestCaseInfoSerializer, SubTestCaseSerializer, SubTestCaseInfoSerializer
from .filters import StoryFilter, TestCaseFilter


class StoryPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('stories', data)
        ]))

class StoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    Get story list --- list, filter, order
    '''
    queryset = Story.objects.all().order_by('release')
    serializer_class = StorySerializer
    pagination_class = StoryPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = StoryFilter
    ordering_fields = ('story_id', )


class StoryOperateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    '''
    Operate sprint ---- create, update, delete
    '''
    queryset = Story.objects.all()
    serializer_class = StoryUpdateInfoSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data['story'], partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        last_update_user = self.request.data['username']
        serializer.save(last_update_time = datetime.now(), last_update_user=last_update_user)


class TestCasePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 50

    def get_paginated_response(self, data):
        for case_detail in data:
            project_list = []
            project_list.append(case_detail['project'])
            case_detail['project'] = project_list
            case_detail['tag'] = case_detail['tag'].split(',')

        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('cases', data)
        ]))

class TestCaseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    Get test case list --- list, filter, order
    '''
    queryset = TestCases.objects.all().order_by('name')
    serializer_class = TestCaseSerializer
    pagination_class = TestCasePagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TestCaseFilter

class TestCaseOperateViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = TestCases.objects.all()
    serializer_class = TestCaseInfoSerializer




