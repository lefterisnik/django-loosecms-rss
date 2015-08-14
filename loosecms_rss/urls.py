# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

app_urlpatterns = [
    url(r'^rss/(?P<rss_slug>[0-9A-Za-z-_.]+)/$', rss, name='rss-info'),
]

urlpatterns = []