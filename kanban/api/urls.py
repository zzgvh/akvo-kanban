# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from piston.resource import Resource

from handlers import TaskHandler, TileHandler, SectionHandler, BoardHandler

task_handler        = Resource(TaskHandler)
tile_handler        = Resource(TileHandler)
section_handler     = Resource(SectionHandler)
board_handler       = Resource(BoardHandler)


urlpatterns = patterns('',    
    url(r'^task/$',                         task_handler, name='task_handler'), # /task/
    url(r'^task/(?P<task_id>\d+)/$',        task_handler, name='task_handler'), # /task/17/

    url(r'^tile/$',                         tile_handler, name='tile_handler'), # /tile/
    url(r'^tile/(?P<tile_id>\d+)/$',        tile_handler, name='tile_handler'), # /tile/17/

    url(r'^section/$',                      section_handler, name='section_handler'), # /section/
    url(r'^section/(?P<section_id>\d+)/$',  section_handler, name='section_handler'), # /section/17/

    url(r'^board/$',                        board_handler, name='board_handler'), # /board/
    url(r'^board/(?P<board_id>\d+)/$',      board_handler, name='board_handler'), # /board/17/
)
