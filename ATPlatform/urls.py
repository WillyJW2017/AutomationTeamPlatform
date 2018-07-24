"""ATPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from users.views import UserLoginViewSet, UserRegisterViewSet, UserUpdateInfoViewSet
from projects_manage.views import ProjectsViewSet, SprintsViewSet, SprintsOperateViewSet, ReleasesViewSet, ReleasesOperateViewSet
from projects_manage.views import ReleasesDeleteViewSet
from projects_manage.test_cases_views import StoryViewSet, StoryOperateViewSet, TestCaseViewSet, TestCaseOperateViewSet, SubTestCaseViewSet, SubTestCaseOperateViewSet

router = DefaultRouter()

# configure the user related url(login, register, update)
router.register(r'login', UserLoginViewSet, base_name='login')
router.register(r'register',UserRegisterViewSet, base_name='register')
router.register(r'system-user/update', UserUpdateInfoViewSet, base_name='system-user/update')

# configure the project related (list) url
router.register(r'project/list-page',ProjectsViewSet, base_name='project/list-page')
router.register(r'project/list',ProjectsViewSet, base_name='project/list')

#configure the sprint related(list, add, update, delete) url
router.register(r'sprint/list', SprintsViewSet, base_name='sprint/list')
router.register(r'sprint/list-page', SprintsViewSet, base_name='sprint/list-page')
router.register(r'sprint/add', SprintsOperateViewSet, base_name='sprint/add')
router.register(r'sprint/delete', SprintsOperateViewSet, base_name='sprint/delete')
router.register(r'sprint/edit', SprintsOperateViewSet, base_name='sprint/edit')

#configure the release related(list, add, update, delete) url
router.register(r'release/list', ReleasesViewSet, base_name='release/list')
router.register(r'release/list-page', ReleasesViewSet, base_name='release/list-page')
router.register(r'release/add', ReleasesOperateViewSet, base_name='release/add')
router.register(r'release/edit', ReleasesOperateViewSet, base_name='release/edit')
router.register(r'release/delete', ReleasesOperateViewSet, base_name='release/delete')
router.register(r'release/batch-delete', ReleasesDeleteViewSet, base_name='release/batch-delete')

#configure the story related(list, update) url
router.register(r'story/list-page', StoryViewSet, base_name='story/list-page')
router.register(r'story/edit', StoryOperateViewSet, base_name='story/edit')
router.register(r'story/unselected',StoryViewSet, base_name='story/unselected')
router.register(r'story/selected',StoryViewSet, base_name='story/selected')

#configure the case related(list, add, update, delete) url
router.register(r'case/list-page', TestCaseViewSet, base_name='case/list-page')
router.register(r'case/add', TestCaseOperateViewSet, base_name='case/add')
router.register(r'case/edit', TestCaseOperateViewSet, base_name='case/edit')
router.register(r'case/delete', TestCaseOperateViewSet, base_name='case/delete')

router.register(r'subcase/selected', SubTestCaseViewSet, base_name='subcase/selected')
router.register(r'subcase/unselected', SubTestCaseViewSet, base_name='subcase/unselected')
router.register(r'subcase/edit', SubTestCaseOperateViewSet, base_name='subcase/edit')

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'docs/', include_docs_urls(title='Automation Team Platform')), # drf文档入口

]
