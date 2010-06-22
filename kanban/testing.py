#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management import setup_environ
    
import settings
setup_environ(settings)

from django.contrib.auth.models import Group, User
from django.db.models import get_model, Count

from os.path import basename, splitext

from board.models import *

def print_list(list):
    for item in list:
        print item
        print item.tiles_in_section
    print
    
def main():
    tiles = Tile.objects.all().annotate(tiles_in_section=Count('section__tiles'))
    print_list( tiles )
    
if __name__ == '__main__':
    main()

