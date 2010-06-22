# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class Board(models.Model):
    title       = models.CharField(_(u'title'), max_length=50, )
    
    def __unicode__(self):
        return self.title

    def display_sections(self):
        return "<br/>".join([s.title for s in Section.objects.filter(board=self)])
    display_sections.allow_tags = True

    class Meta:
        verbose_name = _(u'board')
        verbose_name_plural = _(u'boards')
        
class Section(models.Model):
    board       = models.ForeignKey(Board, verbose_name=_(u'board'), related_name='sections', )
    order       = models.IntegerField(_(u'order'), )
    title       = models.CharField(_(u'title'), max_length=50, )
    subtitle    = models.CharField(_(u'subtitle'), max_length=50, blank=True, )
    max         = models.PositiveIntegerField(_(u'max tasks'), )
    vertical    = models.BooleanField(_(u'vertical orientation'), default=True, )
    wide        = models.BooleanField(_(u'extra wide tiles'), default=False, )
    color       = models.CharField(_(u'RGB colour'), max_length=6, default='FFFFFF', )

    def __unicode__(self):
        return self.title

    def display_tiles(self):
        return "<br/>".join([t.title for t in Tile.objects.filter(section=self)])
    display_tiles.allow_tags = True

    class Meta:
        verbose_name = _(u'section')
        verbose_name_plural = _(u'sections')
        ordering = ['order',]

    
class Tile(models.Model):
    section     = models.ForeignKey(Section, verbose_name=_(u'section'), related_name='tiles', )
    order       = models.IntegerField(_(u'order'), )
    title       = models.CharField(_(u'title'), max_length=50, blank=True, )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'tile')
        verbose_name_plural = _(u'tiles')
        ordering = ['section__order',]

    
class Task(models.Model):
    tile        = models.ForeignKey(Tile, verbose_name=_(u'tile'), related_name='tasks', )
    user        = models.ForeignKey(User, verbose_name=_(u'user'), related_name='user_tasks', blank=True, )
    order       = models.IntegerField(_(u'order'), )
    #user        = models.ForeignKey(UserProfile, _(u'user'), blank=True)
    title       = models.CharField(_(u'title'), max_length=50, )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'task')
        verbose_name_plural = _(u'tasks')
        ordering = ['order',]
