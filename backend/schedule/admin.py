from django.contrib import admin

from .models import Location
from .models import Event
from .models import Resource


admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Resource)
