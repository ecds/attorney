from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sites.models import Site

admin.autodiscover()
admin.site.unregister(Site)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'attorney.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
