import datetime
import time
from datetime import timedelta
from time import mktime
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
                            'Stage West Office': {'letterMap': 'J', 'description' : 'desc goes here', 'capacity': 100, 'square_footage': 1000, 'price' : 100},
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

        events = {'Dance Class' : { 'sstart' : datetime.datetime(2014, 6, 8, 8, 0, 1), 'status' : 'pending', 'location' : 'Viaduct Gallery' },
                  'Cooking Class' : { 'sstart' : datetime.datetime(2014, 6, 8, 12, 0, 1), 'status' : 'pending', 'location' : 'Capres Kafe' },
                  'Art Show' : { 'sstart' : datetime.datetime(2014, 6, 8, 16, 0, 1), 'status' : 'pending', 'location' : 'Viaduct Gallery' },
                  'Jazz Concert' : { 'sstart' : datetime.datetime(2014, 6, 8, 17, 0, 1), 'status' : 'confirmed', 'location' : 'Blue Moon Recording Studio' },
                  'A Concert of Awesome' : { 'sstart' : datetime.datetime(2014, 6, 9, 9, 0, 1), 'status' : 'pending', 'location' : 'Civic Music Association Office' },
                  'Handball' : { 'sstart' : datetime.datetime(2014, 6, 9, 11, 0, 1), 'status' : 'pending', 'location' : 'Handball Court' },
                  'Art Class' : { 'sstart' : datetime.datetime(2014, 6, 10, 16, 0, 1), 'status' : 'pending', 'location' : 'Studio A' },
                  'Charity Fundraiser' : { 'sstart' : datetime.datetime(2014, 6, 9, 15, 0, 1), 'status' : 'confirmed', 'location' : 'ALS Association Iowa Office' },
                  'Office Meeting' : { 'sstart' : datetime.datetime(2014, 6, 10, 18, 0, 1), 'status' : 'pending', 'visibility':'private', 'location' : 'RTI Office' },
                  'Sushi Class' : { 'sstart' : datetime.datetime(2014, 6, 11, 8, 0, 1), 'status' : 'confirmed', 'location' : 'Capres Kafe' },
                  'Some Recording Session' : { 'sstart' : datetime.datetime(2014, 6, 11, 10, 0, 1), 'status' : 'confirmed', 'location' : 'Studio A' },
                  'Music Class' : { 'sstart' : datetime.datetime(2014, 6, 11, 16, 0, 1), 'status' : 'pending', 'location' : 'Blue Moon Recording Studio' },
                  'Cooking Class' : { 'sstart' : datetime.datetime(2014, 6, 11, 20, 0, 1), 'status' : 'confirmed', 'location' : 'Capres Kafe' },
                  'Dance Class' : { 'sstart' : datetime.datetime(2014, 6, 12, 12, 0, 1), 'status' : 'pending', 'location' : 'Movement Room' },
                  'Indian Cooking' : { 'sstart' : datetime.datetime(2014, 6, 12, 13, 0, 1), 'status' : 'pending', 'location' : 'Capres Kafe' },
                  'Wood Working Class' : { 'sstart' : datetime.datetime(2014, 6, 12, 16, 0, 1), 'status' : 'confirmed', 'location' : 'Workshop' },
                  'Finger Painting' : { 'sstart' : datetime.datetime(2014, 6, 13, 7, 0, 1), 'status' : 'pending', 'location' : 'Viaduct Gallery' },
                  'How to make food' : { 'sstart' : datetime.datetime(2014, 6, 13, 11, 0, 1), 'status' : 'confirmed', 'location' : 'Capres Kafe' },
                  'A Fundraiser' : { 'sstart' : datetime.datetime(2014, 6, 14, 10, 0, 1), 'status' : 'confirmed', 'location' : 'ALS Association Iowa Office' },
                  'Cooking Class' : { 'sstart' : datetime.datetime(2014, 6, 14, 14, 0, 1), 'status' : 'confirmed', 'location' : 'Capres Kafe' }
        }

        for event in events.iterkeys():
            Event.objects.get_or_create(
                event_name=event,
                setup_start=events[event]['sstart'],
                setup_end=events[event]['sstart'] + timedelta(minutes=30),
                event_start=events[event]['sstart'] + timedelta(minutes=30),
                event_end=events[event]['sstart'] + timedelta(hours=2.5),
                teardown_start=events[event]['sstart'] + timedelta(hours=2.5),
                teardown_end=events[event]['sstart'] + timedelta(hours=3),
                status=events[event]['status'],
                visibility= 'private' if event == 'Office Meeting' else 'public',
                location=Location.objects.get(location_name = events[event]['location']),
                contact_name='John Richard',
                contact_email='john.richard@gmail.com'
            )
