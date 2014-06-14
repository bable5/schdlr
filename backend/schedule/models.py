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
    discipline = models.ManyToManyField('Discipline')

    def title(self):
        if self.visibility == 'private':
            return u"** Private **"
        else:
            return u"{}".format(self.event_name)

    def location_name(self):
        return self.location.location_name


class Location(models.Model):
    square_footage = models.IntegerField()
    capacity = models.IntegerField()
    location_name = models.CharField(max_length=255, blank=False)
    availability = models.CharField(max_length=255, blank=False)
    contact_name = models.CharField(max_length=255, blank=False)
    contact_phone_number = models.CharField(max_length=11, blank=True)
    contact_email = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s - %s' % (self.location_name)


class Resource(models.Model):
    is_fixed = models.BooleanField()
    resource_type = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    location = models.ForeignKey(Location, null=True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.resource_type, self.description)


class Discipline(models.Model):
    description = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=False)
    
    def __unicode__(self):
        return u'%s - %s' % (self.name, self.description)