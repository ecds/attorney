from django.contrib import admin
from downtime.models import Period
from eultheme.models import Banner

admin.site.unregister(Period)
admin.site.unregister(Banner)

# Register your models here.
