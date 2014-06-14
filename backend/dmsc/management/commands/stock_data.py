from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User

from schedule.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.create(username='admin')

        location, _ = Location.objects.get_or_create(
            location_name='Location 1',
            square_footage=100,
            capacity=100
        )
        resource = Resource.objects.get_or_create(
            is_fixed=True,
            resource_type="speakers",
            description="Bose 5.1",
            location=location
        )
        event = Event.objects.create(
            setup_start=datetime.now(),
            setup_end=datetime.now(),
            event_start=datetime.now(),
            event_end=datetime.now(),
            teardown_start=datetime.now(),
            teardown_end=datetime.now(),
            status='pending',
            visibility='public',
            location=location,
            contact_name='John Richard',
            contact_email='john.richard@gmail.com'
        )
