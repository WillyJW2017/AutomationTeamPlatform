import time
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
from .serializers import StorySerializer, StoryUpdateInfoSerializer, TestCaseSerializer, TestCaseInfoSerializer, SubTestCaseSerializer, SubTestCaseInfoSerializer, SubTestCaseEditSerializer
from .filters import StoryFilter, TestCaseFilter, SubTestCaseFilter


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
    # lookup_field = 'name'

class TestCaseOperateViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = TestCases.objects.all()
    serializer_class = TestCaseInfoSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        project = self.request.data['testcase']['project']
        tag = self.request.data['testcase']['tag']
        self.request.data['testcase']['project'] = ','.join(project)
        self.request.data['testcase']['tag'] = ','.join(tag)

        serializer = self.get_serializer(data=request.data['testcase'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        project = self.request.data['testcase']['project']
        last_update_user = self.request.data['username']
        test_case = serializer.save(project_id=project, updateDate=time.strftime('%Y-%m-%d',time.localtime(time.time())), updatePerson=last_update_user)
        sub_cases_data = self.request.data['testcase']['subcases']

        for sub_data in sub_cases_data:
            sub_case = SubTestCases()
            sub_case.name = test_case
            sub_case.sub = test_case
            sub_case.project = test_case.project
            sub_case.framework = test_case.framework
            sub_case.tag = test_case.tag
            sub_case.functionArea =  test_case.functionArea
            sub_case.description = test_case.description


            sub_case.storyId = ''
            sub_case.application = sub_data['application']
            sub_case.os = sub_data['os']
            sub_case.platform = sub_data['platform']
            sub_case.country = sub_data['country']
            sub_case.status = sub_data['status']
            sub_case.last_update_user = test_case.updatePerson

            sub_case.save()
        return test_case

    def update(self, request, *args, **kwargs):
        project = self.request.data['testcase']['project']
        tag = self.request.data['testcase']['tag']
        self.request.data['testcase']['project'] = ','.join(project)
        self.request.data['testcase']['tag'] = ','.join(tag)

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data['testcase'], partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        name = self.request.data['testcase']['name']
        project = self.request.data['testcase']['project']
        last_update_user = self.request.data['username']
        test_case = serializer.save(project_id=project,
                                    updateDate=time.strftime('%Y-%m-%d', time.localtime(time.time())),
                                    updatePerson=last_update_user)
        sub_cases_data = self.request.data['testcase']['subcases']

        # Delete the existing sub cases from SubTestCases table, then add new sub cases
        updated_test_cases = TestCases.objects.filter(name=name)
        updated_test_case_id = ''
        for updated_test_case in updated_test_cases:
            updated_test_case_id = updated_test_case.id

        delete_sub_cases = SubTestCases.objects.filter(name=updated_test_case_id)
        for sub_case in delete_sub_cases:
            sub_case.delete()

        for sub_data in sub_cases_data:
            sub_case = SubTestCases()
            sub_case.name = test_case
            sub_case.sub = test_case
            sub_case.project = test_case.project
            sub_case.framework = test_case.framework
            sub_case.tag = test_case.tag
            sub_case.functionArea = test_case.functionArea
            sub_case.description = test_case.description

            sub_case.storyId = ''
            sub_case.application = sub_data['application']
            sub_case.os = sub_data['os']
            sub_case.platform = sub_data['platform']
            sub_case.country = sub_data['country']
            sub_case.status = sub_data['status']
            sub_case.last_update_user = test_case.updatePerson

            sub_case.save()
        return test_case

class SubTestCasePagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100

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
            ('subcases', data)
        ]))


class SubTestCaseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    Get Sub test case list --- list, filter, order
    '''
    queryset = SubTestCases.objects.all().order_by('name')
    serializer_class = SubTestCaseSerializer
    pagination_class = SubTestCasePagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SubTestCaseFilter

class SubTestCaseOperateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    '''
    Operate sub Test cases ---- update
    '''
    queryset = SubTestCases.objects.all()
    serializer_class = SubTestCaseEditSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data['subcase'], partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        storyId = self.request.data['subcase']['storyId']
        # last_update_user = self.request.data['username']
        serializer.save(storyId=storyId, last_update_time = datetime.now())












































