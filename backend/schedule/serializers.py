from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title', read_only=True)
    start = serializers.DateTimeField(source='setup_start', read_only=True)
    end = serializers.DateTimeField(source='teardown_end', read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'start', 'end', 'visibility', )
