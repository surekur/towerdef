#!/usr/bin/env python3

import sys
import pygame as pg
from pygame.math import Vector2 as Vec
from pygame.rect import Rect
from pygame.time import get_ticks
import widgets
import game
import battlefield
from constans import testmap



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

uitree = widgets.UIRoot(None, Rect(0, 0, 800, 800))
gameinstance = game.Game(uitree, Rect(0, 0, 768, 800) )
bf = battlefield.load_battlefield(testmap, gameinstance)
gameinstance.battlefield = bf
screen = pg.display.set_mode((800, 800))

uitree.children.append(gameinstance)
        

lasttime = get_ticks()
while True:
    now = get_ticks()
    frame_step(now - lasttime)
    lasttime = now


