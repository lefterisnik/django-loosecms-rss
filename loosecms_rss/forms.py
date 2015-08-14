# -*- coding:utf-8 -*-
from .models import RssManager, Rss
from loosecms.forms import PluginForm


class RssManagerForm(PluginForm):

    class Meta(PluginForm.Meta):
        model = RssManager
