# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *

from loosecms.plugin_pool import plugin_pool
from loosecms.plugin_modeladmin import PluginModelAdmin


class RssInline(admin.StackedInline):
    model = Rss
    extra = 1
    prepopulated_fields = {'slug': ('title', )}


class RssManagerPlugin(PluginModelAdmin):
    model = RssManager
    name = _('Rss')
    template = "plugin/rss.html"
    plugin = True
    inlines = [
        RssInline,
    ]

    def update_context(self, context, manager):
        rsss = Rss.objects.select_related().filter(manager=manager, published=True).order_by('order')

        context['rsss'] = rsss
        return context

plugin_pool.register_plugin(RssManagerPlugin)