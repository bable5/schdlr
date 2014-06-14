from django.conf.urls import patterns, include, url

from rest_framework import viewsets, routers

from schedule.models import Location, Resource, Event
from schedule.feeds import EventFeed
from schedule.serializers import LocationSerializer

from django.contrib import admin

import django_filters

admin.autodiscover()

from schedule.views import EventList


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    model = Resource
    filter_fields = ('resource_type', 'description', 'location')


class EventViewSet(viewsets.ModelViewSet):
    model = Event
    filter_fields = ('location', 'visibility', 'status')


router = routers.DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'resource', ResourceViewSet)
router.register(r'event', EventViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    # url(r'^blog/', include('blog.urls')),

    (r'^ical/$', EventFeed()),
    url(r'calendarevent/', EventList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
)
