import sys
import pygame as pg
from constans import *
from pygame.math import Vector2 as Vec

bitmaps = {}

def get_image(path):
    """
    Returns the image with the given relative path.
    Never loads an image from a file twice, hence using
    this method is more optimal than calling image.load()
    directly.
    """
    if not path in bitmaps:
        try:
            bitmaps[path] = pg.image.load(path)
        except Exception as exc:
            print("Cant load image: "+str(path))
            print(exc)
            sys.exit(1)
    return bitmaps[path]

def cord_from_pos(pos):
    return tuple(Vec(pos) // TILESIZE)

