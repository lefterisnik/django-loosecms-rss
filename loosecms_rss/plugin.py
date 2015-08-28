# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import *

from loosecms.plugin_pool import plugin_pool
from loosecms.plugin_modeladmin import PluginModelAdmin


class RssInline(admin.StackedInline):
    model = Rss
    extra = 1
    prepopulated_fields = {'slug': ('title', )}


class RssPlugin(PluginModelAdmin):
    model = RssManager
    name = _('Rss')
    form = RssManagerForm
    template = "plugin/rss.html"
    plugin = True
    inlines = [
        RssInline,
    ]
    extra_initial_help = None
    fields = ('type', 'placeholder', 'title', 'published')

    def update_context(self, context, manager):
        rsss = Rss.objects.select_related().filter(manager=manager, published=True).order_by('order')

        context['rsss'] = rsss
        return context

    def get_changeform_initial_data(self, request):
        initial = {}
        if self.extra_initial_help:
            initial['type'] = self.extra_initial_help['type']
            initial['placeholder'] = self.extra_initial_help['placeholder']

            return initial
        else:
            return {'type': 'RssPlugin'}

plugin_pool.register_plugin(RssPlugin)