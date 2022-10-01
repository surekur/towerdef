#!/usr/bin/env python3

import sys
import pygame as pg
from pygame.math import Vector2 as Vec
from pygame.rect import Rect
from pygame.time import get_ticks

TILESIZE = 32


class UiElement:
    def __init__(self):
        self.surface = pg.surface.Surface(100, 100)

    def on_click(self, pos):
        pass

    def re_draw():

class MapTile:
    def __init__(self):
        self.passable = True
        self.bitmap = get_image('foo.png')

    def update(self):
        """
        Called on every frame step.
        """
        pass

    def think(self):
        """
        Called irregularly and less often than update.
        Place more time consuming logic here!
        """
        pass

    def draw(self, pos):
        print("draw()")
        pos = Vec(pos) * TILESIZE
        screen.blit(self.bitmap, pos)


class DynEnt:
    def __init__(self, pos):
        self.pos = Vec(pos)
        self.collides = False

    def update(self, delta):
        """
        Called in every 1 second.
        """
        pass

    def think(self):
        """
        Called irregularly and less often than update.
        Place more time consuming logic here!
        """
        pass

    def draw(self, delta): 
        """
        Called on every frame step.
        """
        pass

    def move(v):
        self.pos += Vec(v)

class Animated:
    def __init__(self, animationspeed):
        self.frames = []
        self.animspeed = animationspeed
        self.activeframe = 0

    def draw(self, pos):
        self.

class Collideable(DynEnt):
    def __init__(self, pos):
        super().__init__(pos)
        self.collisionrect = Rect(pos, (32, 32))

    def test_collision():
        for otherent in entities:
            if otherent.collides and
            self.collisionrect.colliderect(otherent.collisionrect):
                self.on_colide(otherent)

    def on_colide(self, otherent):
        pass

    def move(v):
        self.pos += Vec(v)
        self.collisionrect.move(v)


class Cow(Collideable. Animated):
    def __init__(pos):
        super().__init__(pos)
        self.frames = [
                    get_image("data/cow.png"),
                ]

    def update(delta):
        self.move(Vec(0,1) *delta * self.speed)

        


def load_battlefield():
    bf = {}
    for x in range(16):
        for y in range(16):
            bf[(x, y)] = MapTile()
    return bf

def get_image(path):
    """
    Returns the image with the given relative path.
    Never loads an image from a file twice, so using
    this method is more optimal than calling image.load()
    directly.
    """
    if not path in bitmaps:
        try:
            bitmaps[path] = pg.image.load(path)
        except Exception as exc:
            print("Cant load image: "+str(path))
            print(exc)
    return bitmaps[path]


def frame_step(delta):
    for cords in battlefield:
        print(cords)
        battlefield[cords].draw(cords)
    pg.display.update()
    pg.display.flip()

screen = pg.display.set_mode((800, 800))
battlefield = {}
bitmaps = {}
entities = set()



battlefield = load_battlefield()

while True:
    frame_step(1)


