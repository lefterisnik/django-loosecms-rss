# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import RssManager, Rss
from .plugin import RssPlugin

admin.site.register(RssManager, RssPlugin)
admin.site.register(Rss)