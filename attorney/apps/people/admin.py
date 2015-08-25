from django.contrib import admin
from django.conf import settings
from attorney.apps.people.models import Grantee, GrantorName, Identifier


class GranteeAdmin(admin.ModelAdmin):
    list_display = ['grantee_id', 'name', 'title']
    search_fields = ['name', 'title']
    filter_horizontal = ['identifiers']

admin.site.register(Grantee, GranteeAdmin)


class GrantorNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    search_fields = ['name', 'title']

admin.site.register(GrantorName, GrantorNameAdmin)


class IdentifierAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Identifier, IdentifierAdmin)
