from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User

from schedule.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin, _ = User.objects.get_or_create(username='admin', is_superuser=True, is_staff=True)
        admin.set_password('admin')
        admin.save()

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
            event_name='Testing Event',
            setup_start=timezone.now(),
            setup_end=timezone.now(),
            event_start=timezone.now(),
            event_end=timezone.now(),
            teardown_start=timezone.now(),
            teardown_end=timezone.now(),
            status='pending',
            visibility='public',
            location=location,
            contact_name='John Richard',
            contact_email='john.richard@gmail.com'
        )
