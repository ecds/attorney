from django.db import models
from attorney.apps.geo.models import Place


class Grantee(models.Model):
    'Individuals granted power of attorney'

    objects = models.Manager()

    grantee_id = models.CharField(max_length=30, primary_key=True,)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    identifiers = models.ManyToManyField('Identifier', blank=True)
    professional_location = models.ForeignKey(Place, blank=True, null=True, related_name='professional_location')
    standard_location = models.ForeignKey(Place, blank=True, null=True, related_name='standard_location')
    alt_location = models.ForeignKey(Place, blank=True, null=True, related_name='alt_location')

    def __unicode__self():
        return self.name


class GrantorName(models.Model):
    'Names of people granted power of attorney'

    objects = models.Manager()

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    event = models.ForeignKey('events.Event')

    def __unicode__self():
        return self.name


class Identifier(models.Model):
    'Social/Cultural/Racial Identifier'

    objects = models.Manager()

    name = models.CharField(max_length=255)

    def __unicode__self():
        return self.name