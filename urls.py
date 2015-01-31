from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'demo.core.views.home', name='home'),
    url(r'^entries/(?P<entry_id>\d+)$', 'demo.core.views.entries', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
