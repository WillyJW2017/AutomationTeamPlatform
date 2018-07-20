from datetime import datetime
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from collections import OrderedDict
from django_filters.rest_framework import DjangoFilterBackend

from .models import Projects, Sprints, Releases
from .serializers import ProjectSerializer, SprintSerializer, SprintInfoSerializer, ReleaseSerializer, ReleaseInfoSerializer
from .filters import ProjectsFilter, SprintsFilter, ReleasesFilter


# customized pagination function
class ProjectsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('projects', data)
        ]))

class ProjectsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Projects.objects.all().order_by('name')
    serializer_class = ProjectSerializer
    pagination_class = ProjectsPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = ProjectsFilter

class SprintsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('sprints', data)
        ]))

class SprintsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    Get sprint list --- list, filter, order
    '''
    queryset = Sprints.objects.all().order_by('name')
    serializer_class = SprintSerializer
    pagination_class = SprintsPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SprintsFilter
    ordering_fields = ('name', )


class SprintsOperateViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    '''
    Operate sprint ---- create, update, delete
    '''
    queryset = Sprints.objects.all()
    serializer_class = SprintInfoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data['sprint'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        project = self.request.data['sprint']['project']
        last_update_user = self.request.data['username']
        serializer.save(project_id=project, last_update_time = datetime.now(), last_update_user=last_update_user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data['sprint'], partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        # project = self.request.data['sprint']['project']
        last_update_user = self.request.data['username']
        # serializer.save(project_id=project, last_update_time=datetime.now(), last_update_user=last_update_user)
        serializer.save(last_update_time=datetime.now(), last_update_user=last_update_user)

class ReleasesPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('releases', data)
        ]))

class ReleasesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    Get release list --- list, filter, order
    '''
    queryset = Releases.objects.all().order_by('name')
    serializer_class = ReleaseSerializer
    pagination_class = ReleasesPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ReleasesFilter
    ordering_fields = ('name', )


class ReleasesOperateViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    '''
    Operate release ---- create, update, delete
    '''
    queryset = Releases.objects.all()
    serializer_class = ReleaseInfoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data['release'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        project = self.request.data['release']['project']
        last_update_user = self.request.data['username']
        serializer.save(project_id=project, last_update_time = datetime.now(), last_update_user=last_update_user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data['release'], partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        # project = self.request.data['release']['project']
        last_update_user = self.request.data['username']
        serializer.save(last_update_time = datetime.now(), last_update_user=last_update_user)


class ReleasesDeleteViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    def get_queryset(self):
        return Releases.objects.filter(id__in=self.request.query_params['ids'])






