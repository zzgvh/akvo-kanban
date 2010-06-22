# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import get_model, Count
from django.shortcuts import get_object_or_404

from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc

from kanban.board.models import Task, Tile, Section, Board

class BoardHandler(AnonymousBaseHandler):
    """
    Returns Board(s)
    """
    allowed_methods = ('GET',)

    model = Board
    exclude = ()
    
    def read(self, request, board_pk=1):
        return Board.objects.select_related().get(pk=board_pk)


class SectionHandler(AnonymousBaseHandler):
    """
    Returns Section(s)
    """
    allowed_methods = ('GET',)

    model = Section
    exclude = ()


class TileHandler(AnonymousBaseHandler):
    """
    Returns Tile(s)
    """
    allowed_methods = ('GET',)

    model = Tile
    fields = ('id', 'title', 'order', 'tiles_in_section',
                ('section', ('id', 'title', 'subtitle', 'order', 'max', 'vertical', 'wide', 'color',
                    ('board', ('id', 'title',))
                ))
            )

    def read(self, request, tile_id=None):
        if tile_id:
            tiles = Tile.objects.select_related().get(pk=tile_id)
        else:
            tiles = Tile.objects.all().annotate(tiles_in_section=Count('section__tiles'))
        return tiles
    
class TaskHandler(AnonymousBaseHandler):
    """
    Returns Task(s)
    """

    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE',)

    model = Task
    exclude = ()

    def create(self, request):
        if request.content_type:
            data = request.data
            SHORTLIST_TILE = 11
            order = Task.objects.filter(tile__id=SHORTLIST_TILE).count() * 10 + 10
            task = self.model( title=data['title'], user_id=data['user_id'], order=order, tile_id=SHORTLIST_TILE)
            task.save()
            
            return task
        #else:
        #    super(Task, self).create(request)

    def update(self, request):
        if request.content_type:
            data_list = request.data
            for data in data_list:
                #task = self.model(id=data['id'], order=data['order'], title=data['title'], tile_id=data['tile']['id'], )
                task = self.model.objects.get(id=data['id'])
                task.order      = data['order']
                task.tile_id    = data['tile']['id']
                task.save()
            return rc.ALL_OK
        #else:
        #    super(Task, self).create(request)

    def delete(self, request):
        if request.content_type:
            data = request.data
            Task.objects.get(pk=data['id']).delete()            
            return rc.DELETED

    
    def read(self, request, task_id=None):
        if task_id:
            return Task.objects.select_related().get(pk=task_id)
        else:
            return {'users': User.objects.all(), 'tasks': Task.objects.all()}
