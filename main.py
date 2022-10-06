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
import sqlite3


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

class Sql:
    def __init__(self):
        self.connection = sqlite3.connect("userdata.db")
        self.cursor = self.connection.cursor()
        self.execute(
        """
        CREATE TABLE IF NOT EXISTS Saves(
            ut REAL,
            gamememory BLOB
            )
        """)
        self.execute("""
        CREATE TABLE IF NOT EXISTS Maps(
            title TEXT,
            bfstring TEXT,
            author TEXT,
            created REAL
            )
        """)

    def execute(self, command, params=()):
        self.cursor.execute(command, params)
        self.cursor
        self.connection.commit()

sql = Sql()
uitree = widgets.UIRoot(None, Rect(0, 0, 800, 800))
gameinstance = game.Game(uitree, Rect(0, 0, 768, 800) )
bf = battlefield.load_battlefield(testmap, gameinstance)
gameinstance.battlefield = bf
screen = pg.display.set_mode((800, 800))
mainpanel = widgets.MainPanel(uitree, Rect(769, 601, 32, 200),
        gameinstance, sql)

uitree.children.append(gameinstance)
uitree.children.append(mainpanel)

lasttime = get_ticks()
while True:
    now = get_ticks()
    frame_step(now - lasttime)
    lasttime = now


