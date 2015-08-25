from django.contrib import admin
from django.conf import settings
from attorney.apps.geo.models import Place 


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['place_id', 'name', 'alt_name', 'uri']
    search_fields = ['name', 'alt_name']

admin.site.register(Place, PlaceAdmin)