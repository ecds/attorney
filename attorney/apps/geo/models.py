from django.db import models


class Place(models.Model):
    'Places receiving or granting power of attorney'

    objects = models.Manager()

    place_id = models.CharField(max_length=30, primary_key=True,)
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, blank=True,)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    uri = models.URLField(max_length=200, blank=True, verbose_name="Geonames URL")

    def __unicode__(self):  
        return self.name

    # TODO: set Meta class requiring unique lat-lon combination