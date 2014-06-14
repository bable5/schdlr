from django.conf.urls import patterns, include, url

from rest_framework import viewsets, routers

from schedule.models import Location, Resource, Event

from django.contrib import admin
admin.autodiscover()


class LocationViewSet(viewsets.ModelViewSet):
    model = Location


class ResourceViewSet(viewsets.ModelViewSet):
    model = Resource


class EventViewSet(viewsets.ModelViewSet):
    model = Event


router = routers.DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'resource', ResourceViewSet)
router.register(r'event', EventViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
)
