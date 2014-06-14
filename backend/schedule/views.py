from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .models import Event, Location
from .serializers import EventSerializer


class EventList(generics.ListAPIView):
    serializer_class = EventSerializer
    model = Event

    def get_queryset(self):
        qs = Event.objects.all()

        if self.request.GET.get('location'):
            locations = [int(val) for val in self.request.GET.get('location').split(',')]
            qs = qs.filter(location__in=locations)

        print str(qs)

        #if self.request.GET.get('visiblity'):
        #    qs = qs | Event.objects.filter(visibility=self.request.GET.get('visibility'))

        return qs


class OpenLocationsList(generics.ListAPIView):
    model = Location

    def get_queryset(self):

        datetime = self.request.GET.get('datetime')
        datetime = '2014-06-14'
        base = 'select * from schedule_location sl inner join schedule_event se on se.location_id=sl.id'
        base = base + ' where {} between se.setup_start and se.teardown_end'.format(datetime)
        qs = Location.objects.raw(base)
        return qs
