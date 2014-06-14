from django.db import models


STATUS_CHOICES = (
    ('reserved', 'Reserved'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
)

VISIBILITY_CHOICES = (
    ('public', 'Public'),
    ('private', 'Private'),
)


class Event(models.Model):
    event_name = models.CharField(max_length=255, blank=False)
    setup_start = models.DateTimeField()
    setup_end = models.DateTimeField()
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    teardown_start = models.DateTimeField()
    teardown_end = models.DateTimeField()
    needed_resources = models.ManyToManyField('Resource')
    status = models.CharField(default='reserved', choices=STATUS_CHOICES, max_length=255, blank=False)
    visibility = models.CharField(default='public', choices=VISIBILITY_CHOICES, max_length=255, blank=False)
    location = models.ForeignKey('Location')
    contact_name = models.CharField(max_length=255, blank=False)
    contact_phone_number = models.CharField(max_length=11, blank=True)
    contact_email = models.CharField(max_length=255)

    def title(self):
        if self.visibility == 'private':
            return "** Private ** ({})".format(self.location.location_name)
        else:
            return "{} ({})".format(self.event_name, self.location.location_name)


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
