from django.conf.urls import patterns, include, url
from outage.views import Outage

urlpatterns = patterns('',
    url(r'^outage/$', Outage.as_view(), name='outage',),
)
