from datetime import timedelta

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User

from schedule.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin, _ = User.objects.get_or_create(username='admin', is_superuser=True, is_staff=True)
        admin.set_password('admin')
        admin.save()

        LocalLocationData={ 'Capres Kafe': { 'letterMap': 'B', 'description' : 'desc goes here', 'capacity': 100, 'square_footage': 1000, 'price' : 100} ,
                            'Viaduct Gallery': {'letterMap': 'C', 'description' : 'desc goes here', 'capacity': 100, 'square_footage': 1000, 'price' : 100},
                            'Handball Court': {'letterMap': 'E', 'description' : 'This light-filled space is beautifully ', 'square_footage': 1000, 'capacity': 100, 'price': 50},
                            'Movement Room': {'letterMap': 'F', 'description' : 'desc goes here', 'capacity': 100, 'square_footage': 1000, 'price' : 100},
                            'Art Studio': {'letterMap': 'G', 'description' : 'desc goes here', 'capacity': 100,  'square_footage': 1000, 'price' : 100},
                            'Studio A': {'letterMap': 'Z', 'description': 'This brand new space', 'square_footage': 1000, 'capacity': 25, 'price' : 30},
                            'Studio B & C': {'letterMap': 'Y', 'description': '', 'capacity': 20, 'square_footage': 1000, 'price' : 30},
                            'Workshop': {'letterMap': 'H', 'description' : 'desc goes here', 'capacity': 100, 'square_footage': 1000, 'price' : 100},
                            'Blue Moon Recording Studio': {'letterMap': 'I', 'description' : 'desc goes here', 'capacity': 100, 'square_footage': 1000, 'price' : 100},
                            'Stage West Offic': {'letterMap': 'J', 'description' : 'desc goes here', 'capacity': 100, 'square_footage': 1000, 'price' : 100},
                            'ALS Association Iowa Office': {'letterMap': 'K', 'description' : 'Office', 'capacity': 100, 'square_footage': 1000, 'price' : 100},
                            'Civic Music Association Office': {'letterMap': 'L', 'description' : 'Office', 'capacity': 100, 'square_footage': 1000, 'price' : 100},
                            'RTI Office': {'letterMap': 'M', 'description' : 'Office', 'capacity': 100, 'square_footage': 1000, 'price' : 100},
                            'Social Club Office': {'letterMap': 'N', 'description' : 'Office', 'capacity': 100, 'square_footage': 1000, 'price' : 100}
        }
        
        LocalDisciplineData={ 'Education' : 'Cooking Class', 'Visual Art Education' : 'Art Class', 'Literary' : 'Book Club', 'Dance/Movement' : 'Interpretive Dance'}

        for desc in LocalDisciplineData.iterkeys():
            Discipline.objects.get_or_create(
                name = desc,
                description = LocalDisciplineData[desc],
            )
            
        
        for loc_name in LocalLocationData.iterkeys():
            Location.objects.get_or_create(
                location_name=loc_name,
                square_footage=LocalLocationData[loc_name]['square_footage'],
                capacity=LocalLocationData[loc_name]['capacity'],
            )

        Resource.objects.get_or_create(
            is_fixed=True,
            resource_type="speakers",
            description="Bose 5.1",
            location=Location.objects.get(location_name='Handball Court')
        )

        _1 = timezone.now()
        _2 = timezone.now() + timedelta(hours=1)
        _3 = timezone.now() + timedelta(hours=5)
        _4 = timezone.now() + timedelta(hours=6)

        dates = [_1, _2, _3, _4]

        for i in range(10):
            dates.append(dates[-1] + timedelta(hours=1))

        for i, date in enumerate(dates):
            Event.objects.create(
                event_name='Testing Event {}'.format(i),
                setup_start=date,
                setup_end=timezone.now(),
                event_start=timezone.now(),
                event_end=timezone.now(),
                teardown_start=timezone.now(),
                teardown_end=date + timedelta(hours=2),
                status='pending',
                visibility='public' if i != 1 else 'private',
                location=Location.objects.get(location_name='Viaduct Gallery'),
                contact_name='John Richard',
                contact_email='john.richard@gmail.com'
            )

        start = timezone.now() - timedelta(hours=1)
        Event.objects.create(
            event_name='My Testing Event',
            setup_start=start,
            setup_end=start + timedelta(minutes=30),
            event_start=start + timedelta(minutes=30),
            event_end=start + timedelta(hours=2.5),
            teardown_start=start + timedelta(hours=2.5),
            teardown_end=start + timedelta(hours=3),
            status='pending',
            visibility='public' if i != 1 else 'private',
            location=Location.objects.get(location_name='Studio B & C'),
            contact_name='John Richard',
            contact_email='john.richard@gmail.com'
        )
