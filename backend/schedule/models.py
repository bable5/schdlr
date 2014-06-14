from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    setup_start = models.DateTimeField()
    setup_end = models.DateTimeField()
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    teardown_start = models.DateTimeField()
    teardown_end = models.DateTimeField()
    needed_resources = models.ManyToManyField('Resource')
    status = models.CharField(max_length=255, blank=False)
    visibility = models.CharField(max_length=255, blank=False)
    location = models.ForeignKey('Location')
    contact_name = models.CharField(max_length=255, blank=False)
    contact_phone_number = models.CharField(max_length=11, blank=True)
    contact_email = models.CharField(max_length=255)


class Location(models.Model):
    square_footage = models.IntegerField()
    capacity = models.IntegerField()
    location_name = models.CharField(max_length=255, blank=False)
    availability = models.CharField(max_length=255, blank=False)
    contact_name = models.CharField(max_length=255, blank=False)
    contact_phone_number = models.CharField(max_length=11, blank=True)
    contact_email = models.CharField(max_length=255)


class Resource(models.Model):
    is_fixed = models.BooleanField()
    resource_type = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    location = models.ForeignKey(Location, null=True)
