from django.conf.urls import patterns, include, url

from rest_framework import viewsets, routers

from schedule.models import Location, Resource

from django.contrib import admin
admin.autodiscover()


class LocationViewSet(viewsets.ModelViewSet):
    model = Location


class ResourceViewSet(viewsets.ModelViewSet):
    model = Resource


router = routers.DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'resource', ResourceViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
