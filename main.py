#!/usr/bin/env python3

import sys
import pygame as pg
from pygame.math import Vector2 as Vec
from pygame.rect import Rect
from pygame.time import get_ticks
import widgets
import game
import battlefield


testmap = \
"""____________________
____________________
____________________
____________________
____####____________
____________________
___________######___
___#####____________
____##______________
____________________
____________________
____________________
####________________
____________________
____________________
____________________
____________________
_________##########_
____________________
____________________"""


def frame_step(delta):
    screen.fill((100, 0, 0)) # Just for testing
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            uitree.on_click(Vec(event.pos))
    uitree.on_hover(Vec(pg.mouse.get_pos()))
    uitree._update(delta)
    screen.blit(uitree.surface, (0, 0))
    pg.display.update()
    pg.display.flip()

bf = battlefield.load_battlefield(testmap)
screen = pg.display.set_mode((800, 800))

uitree = widgets.UIRoot(None, Rect(0, 0, 800, 800))
uitree.children = [
        game.Game(uitree, Rect(0, 0, 768, 800), bf)
        ]

lasttime = get_ticks()
while True:
    now = get_ticks()
    frame_step(now - lasttime)
    lasttime = now


