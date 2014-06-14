from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .models import Event
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
