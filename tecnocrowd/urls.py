from django.conf.urls import patterns, include, url
from rest_framework import routers, serializers, viewsets
#from clients import views as clientsViews
#from projects import views as projectsViews
from tecnocrowd_backend import views
from django.contrib import admin

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet, base_name='Users')
router.register(r'users/(?P<user_id>)/projects/', views.ProjectsViewSet, base_name='Images')
router.register(r'projects', views.ProjectsViewSet)
router.register(r'projects/(?P<project_id>)/images/', views.ImagesViewSet, base_name='Images')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tecnocrowd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
