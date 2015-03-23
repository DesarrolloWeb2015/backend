from django.conf.urls import patterns, include, url
from rest_framework import routers, serializers, viewsets
from clients import views as clientsViews
from projects import views as projectsViews
from django.contrib import admin

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'clients', clientsViews.ClientsViewSet)
router.register(r'projects', projectsViews.ProjectViewSet)
router.register(r'gallery', projectsViews.GalleryViewSet)
router.register(r'images', projectsViews.ImageViewSet)
router.register(r'projects/(\d{projectid})/gallery', projectsViews.GalleryViewSet)
router.register(r'projects/(\d{projectid})/gallery/images', projectsViews.ImageViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tecnocrowd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
