from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    setup_start = models.DateField()
    setup_end = models.DateField()
    event_start = models.DateField()
    event_end = models.DateField()
    teardown_start = models.DateField()
    teardown_end = models.DateField()
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
    resourceType = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    location = models.ForeignKey(Location, null=True)
