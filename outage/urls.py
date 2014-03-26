from django.conf.urls import patterns, include, url
from outage.views import DBOutage, Outage

urlpatterns = patterns('',
    url(r'^outage/$', Outage.as_view(), name='outage',),
    url(r'^db_outage/$', DBOutage.as_view(), name='db_outage',),
)

