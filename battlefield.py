import sys
from utils import get_image
from pygame.math import Vector2 as Vec


class MapTile:
    def __init__(self, cord, game):
        self.passable = True
        self.destructible = False
        self.canbuildonto = True
        self.bitmap = get_image('data/foo.png')
        self.cord = cord

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


class TowerLike(MapTile):
    def __init__(self, cord, game):
        super().__init__(cord, game)
        self.target = None
        self.optimalrange = 10
        self.firingrate = 1

    def shoot(self):
        pass

    def find_target(self):
        pass


class MGNest(TowerLike):
    def __init__(self, cord, game):
        super().__init__(cord, game)
        self.passable = False
        self.destructible = 7
        self.canbuildonto = False
        self.bitmap = get_image('data/mg_nest.png')


def create_hills(cord, game):
    hills = MapTile(cord, game)
    hills.bitmap = get_image("data/hill.png")
    hills.passable = False
    hills.destructible = False
    hills.canbuildonto = False
    return hills

def create_grass(cord, game):
    grass = MapTile(cord, game)
    grass.passable = True
    grass.destructible = False
    return grass


tilecodes = {
        "_": create_grass,
        "#": create_hills,
        }

def load_battlefield(bfstring, game):
    bf = {}
    x, y = 0, 0
    for char in bfstring:
        if char == "\n":
            x = 0
            y += 1
        else:
            if char in tilecodes:
                bf[(x, y)] = tilecodes[char]((x, y), game)
                x += 1
            else:
                print("The map file is corrupted. The character: \""+char+\
                        "\" is not a valid tilecode.",
                        file=sys.stderr)
                sys.exit(1)
    return bf


