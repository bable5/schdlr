from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .models import Event
from .serializers import EventSerializer


class EventList(
    mixins.ListModelMixin,
    generics.GenericAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
