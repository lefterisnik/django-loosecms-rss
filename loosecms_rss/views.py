# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.shortcuts import render
from django.http import Http404
from .models import Rss

import feedparser


def rss(request, rss_slug):
    try:
        rss = Rss.objects.get(slug=rss_slug)
    except Rss.DoesNotExist:
        raise Http404

    #if rss.timeout != 0:
    #    content = cache.get(rss.slug)
    #    if not content:
    #        content = feedparser.parse(rss.feed)
    #        cache.set(rss.slug, content, rss.timeout)
    #else:
    content = feedparser.parse(rss.feed)

    return render(request, 'templatetags/show_rss_content.html', {'rss': rss, 'content': content})