from django.contrib import admin

from .models import Location
from .models import Event
from .models import Resource
from .models import Discipline


class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'setup_start', 'teardown_end']


admin.site.register(Location)
admin.site.register(Event, EventAdmin)
admin.site.register(Resource)
admin.site.register(Discipline)
