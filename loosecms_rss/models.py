# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models
from loosecms.models import Plugin


class RssManager(Plugin):
    title = models.CharField(_('title'), max_length=200,
                             help_text=_('Give the name of the rss manager.'))
    ctime = models.DateTimeField(auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)


class Rss(models.Model):
    title = models.CharField(_('title'), max_length=50,
                             help_text=_('Give the name of the rss.'))
    slug = models.SlugField(_('slug'), unique=True,
                            help_text=_('Give the slug of the rss'))
    feed = models.CharField(_('feed'), max_length=200,
                            help_text=_('Give the feed url'))
    timeout = models.IntegerField(_('timeout'),
                                  help_text=_('Give the timeout to reload rss. If the values is 0, each time will begin '
                                              'request to feed url to download rss content(adding delaying).'))
    image = models.ImageField(_('image'), upload_to='rss', null=True)

    manager = models.ForeignKey(RssManager, verbose_name=_('manager'),
                                help_text=_('Select the rss manager.'))
    order = models.IntegerField(_('order'))

    published = models.BooleanField(_('published'), default=True)

    def __unicode__(self):
        return self.title