from django.contrib import admin
from django.conf import settings
from attorney.apps.events.models import Event 


class EventAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'date', 'power_type', 'cabildo']
    search_fields = ['citation', 'event_id', 'date', 'power_type', 'cabildo']
    filter_horizontal = ['grantees']

admin.site.register(Event, EventAdmin)
