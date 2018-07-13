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
from projects_manage.views import ProjectsViewSet, SprintsViewSet, SprintsOperateViewSet

router = DefaultRouter()

# configure the login url
router.register(r'login', UserLoginViewSet, base_name='login')

# configure the user register url
router.register(r'register',UserRegisterViewSet, base_name='register')

# configure the project list page url --- return all projects all information
router.register(r'project/list-page',ProjectsViewSet, base_name='project/list-page')

#configure the project list url --- return all projects name
router.register(r'project/list',ProjectsViewSet, base_name='project/list')

#configure the user update url
router.register(r'system-user/update', UserUpdateInfoViewSet, base_name='system-user/update')

router.register(r'sprint/list', SprintsViewSet, base_name='sprint/list')
router.register(r'sprint/list-page', SprintsViewSet, base_name='sprint/list-page')

router.register(r'sprint/add', SprintsOperateViewSet, base_name='sprint/add')
router.register(r'sprint/delete', SprintsOperateViewSet, base_name='sprint/delete')
router.register(r'sprint/edit', SprintsOperateViewSet, base_name='sprint/edit')

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'docs/', include_docs_urls(title='Automation Team Platform')), # drf文档入口

    # url(r'^login/', obtain_jwt_token),


]
