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
        Resource.objects.get_or_create(
            is_fixed=True,
            resource_type="speakers",
            description="Bose 5.1",
            location=location
        )
