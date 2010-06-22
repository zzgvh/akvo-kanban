# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db.models import get_model
from django.forms import ModelForm 
from django.utils.translation import ugettext, ugettext_lazy as _


class SectionInLine(admin.TabularInline):
    model = get_model('board', 'Section')
    extra = 3

class BoardAdmin(admin.ModelAdmin):
    model = get_model('board', 'Board')
    inlines = [SectionInLine, ]
    list_display = ('__unicode__', 'display_sections', )

admin.site.register(get_model('board', 'Board'), BoardAdmin)


class TileInLine(admin.TabularInline):
    model = get_model('board', 'Tile')
    extra = 3

class SectionAdmin(admin.ModelAdmin):
    model = get_model('board', 'Section')
    inlines = [TileInLine, ]
    list_display = ('__unicode__', 'display_tiles', )

admin.site.register(get_model('board', 'Section'), SectionAdmin)


class TileAdmin(admin.ModelAdmin):
    model = get_model('board', 'Tile')
    list_display = ('__unicode__', )

admin.site.register(get_model('board', 'Tile'), TileAdmin)


class TaskAdmin(admin.ModelAdmin):
    model = get_model('board', 'Task')
    list_display = ('__unicode__', )

admin.site.register(get_model('board', 'Task'), TaskAdmin)

