import sys
from utils import get_image
from pygame.math import Vector2 as Vec


class MapTile:
    def __init__(self):
        self.passable = True
        self.destructible = False
        self.canbuildonto = True
        self.bitmap = get_image('data/foo.png')

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

    def draw(self, pos, screen):
        screen.blit(self.bitmap, pos)


class MGNest(MapTile):
    def __init__(self):
        self.passable = False
        self.destructible = 7
        self.canbuildonto = False
        self.bitmap = get_image('data/foo.png')


def create_hills():
    hills = MapTile()
    hills.bitmap = get_image("data/hill.png")
    hills.passable = False
    hills.destructible = False
    hills.canbuildonto = False
    return hills

def create_grass():
    grass = MapTile()
    grass.passable = True
    grass.destructible = False
    return grass


tilecodes = {
        "_": create_grass,
        "#": create_hills,
        }

def load_battlefield(bfstring):
    bf = {}
    x, y = 0, 0
    for char in bfstring:
        if char == "\n":
            x = 0
            y += 1
        else:
            if char in tilecodes:
                bf[(x, y)] = tilecodes[char]()
                x += 1
            else:
                print("The map file is corrupted. The character: \""+char+\
                        "\" is not a valid tilecode.",
                        file=sys.stderr)
                sys.exit(1)
    return bf


