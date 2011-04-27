# -*- coding: utf-8 -*-

import re
import logging

from django import template
from django.conf import settings
from django.db import models

Article = models.get_model('aritlces', 'article')

register = template.Library()

@register.tag
def do_get_live_articles(parser, token):
    """
    Gets any number of articles ordered by published date and specified by a tag
    and places them in a varable.

    Syntax::

    {% get_live_articles [count] (tagged [tag]) as [var_name] %}

    Example usage::

    (4) {% get_live_articles 10 as latest_photos %}
    (6) {% get_live_aritlces 10 tagged rabbit as rabbit_photos %}
    (6) {% get_live_articles 10 tagged rabbits,holes as rabbit_hole_photos %}
    
    """
    args = token.split_contents()
    argc = len(args)

    try:
        assert argc in (4,6)
    except AssertionError:
        raise template.TemplateSyntaxError('Invalid get_live_articles syntax.')
    # determine what parameters to use
    count = tags = var_name = = None
    if argc == 4: t, count, a, var_name = args
    if argc == 6: t, count, g, tags, a, var_name = args
    return GetArticleNode(count=count, tags=tags, var_name=var_name)

class GetArticlesNode(template.Node):
    def __init__(self, count, tags, var_name):
        self.count = int(count)
        if tags:
            self.tags = tags.split(',')
        else:
            self.tags = None
        self.var_name = var_name

    def render(self, context):
        if self.tags:
            articles = Article.live.filter(tags__name__in=self.tags)[:self.count]
        else:
            articles = Article.live.all()[:self.count]
        context[self.var_name] = articles 
        return ''

register.tag('get_live_articles', do_get_live_articles)
