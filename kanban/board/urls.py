# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'board.views.index', name='index'),
)
