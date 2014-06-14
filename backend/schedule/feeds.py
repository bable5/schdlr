from django_ical.views import ICalFeed

from .models import Event


class EventFeed(ICalFeed):
    #product_id = '-//example.com//Example//EN'
    timezone = 'UTC'

    def items(self):
        return Event.objects.all().order_by('-event_start')

    def item_title(self, item):
        return item.event_name

    def item_description(self, item):
        return ''

    def item_start_datetime(self, item):
        return item.setup_start

    def item_end_datetime(self, item):
        return item.teardown_end

    def item_link(self, item):
        return ''
