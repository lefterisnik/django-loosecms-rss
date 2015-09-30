# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^rss/(?P<rss_slug>[0-9A-Za-z-_.]+)/$', rss, name='rss-info'),
]