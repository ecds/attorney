from django.db import models
from attorney.apps.people.models import Grantee
from attorney.apps.geo.models import Place


class Event(models.Model):
    'Event when power of attorney signed'

    objects = models.Manager()

    event_id = models.CharField(max_length=30, primary_key=True,)
    citation = models.CharField(max_length=20)
    date = models.IntegerField() # year
    power_type = models.CharField(max_length=10, verbose_name="Type of Power")
    cabildo = models.CharField(max_length=50)
    translator = models.CharField(max_length=50, blank=True)
    translation_detail = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=255, blank=True)
    grantees = models.ManyToManyField(Grantee, blank=True)
    location = models.ForeignKey(Place, blank=True, null=True)

    def __unicode__(self):  
        return self.event_id

    class Meta:
        ordering = ['event_id']