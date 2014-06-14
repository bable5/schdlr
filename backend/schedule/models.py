from django.db import models

class Event(models.Model):
    contacts = models.ManyToMany(Contact)
    capacity = models.IntegerField
    setup_start = models.DateField
    setup_end = model.DateField
    event_start = model.DateField
    event_end = model.DateField
    teardown_start = model.DateField
    teardown_end = model.DateField
    needed_resources = models.ManyToMany(Resource)
    status = models.CharField(length=255, blank=False)
    visibility = models.CharField(length=255, blank=False)
    event_organizer = models.ForeignKey(Organization)

class Location(models.Model):
    personel = models.ForeignKey('User')
    location_name = models.CharField(length=255, blank=False)
    availability = models.CharField(length=255, blank=False)

class Organization(models.Model):
    name = models.CharField(length=255, blank=False)
    phone_number = models.CharField(length=11, blank=True)
    email = models.CharField(length=255)

class Resource(models.Model):
    isFixed = models.BooleanField
    resourceType = models.CharField(length=255, blank=False)
    description = models.CharField(length=255, blank=True)
    location = models.ForeignKey(Location, null=True)

