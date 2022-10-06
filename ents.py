from pygame.math import Vector2 as Vec
from pygame.time import get_ticks
from pygame.rect import Rect
from utils import *
from pygame.gfxdraw import line

class Entity:
    def __init__(self, pos, game):
        self.pos = Vec(pos)
        self.collides = False
        self.game = game

    def update(self, delta):
        """
        Called in every framestep.
        """
        pass

    def think(self):
        """
        Called irregularly and less often than update.
        Place more time consuming logic here!
        """
        pass

    def draw(self, screen): 
        """
        Called on every frame step.
        """
        pass

    def move(self, v):
        self.pos += Vec(v)

    def pre_save(self):
        """
        Called just before saving the game to the sqlite db.
        We should remove unnececery data, like bitmaps from the
        objects, so they will not waste space on the harddrive.
        """
        if hasattr(self, "surface"):
            self.surface = None

    def on_loadgame(self):
        if hasattr(self, "surfacefile"):
            self.surface = get_image(self.surfacefile)

class Animated:
    def __init__(self, animationspeed, pos):
        self.frames = []
        self.animspeed = animationspeed
        # self.activeframe = 0

    def draw(self, pos, screen):
        frame = int( len(self.frames) // (get_ticks()*self.animspeed) )
        screen.blit(self.frames[frame])

class Collideable(Entity):
    def __init__(self, pos, game):
        super().__init__(pos, game)
        self.collisionrect = Rect(pos, (TILESIZE, TILESIZE))
        self.collides = True

    def test_collision(self, ents):
        for otherent in ents:
            if otherent is not self and otherent.collides and \
            self.collisionrect.colliderect(otherent.collisionrect):
                self.on_colide(otherent)

    def on_colide(self, otherent):
        pass

    def move(self, v):
        self.pos += Vec(v)
        self.collisionrect.move(v)


class Cow(Animated):
    def __init__(self, pos, game):
        super().__init__(pos, game)
        self.speed = Vec(-1, 0)
        self.frames = [
                    get_image("data/cow.png"),
                ]

    def update(self, delta):
        #self.move(self.speed * delta * self.speed)
        pass


class Truck(Collideable):
    def __init__(self, pos, game):
        super().__init__(pos, game)
        self.speed = Vec(-1, 0)
        self.maxacceleration = 1
        self.topspeed = 1
        self.hitpoints = 100
        self.path = []
        self.surface = get_image("data/truck-left1.png")
        self.surfacefile = "data/truck-left1.png"
        self.game.foes.add(self)

    def find_path(self):
        pass

    def update(self, delta):
        # TODO  Uncomment when pathfinding is implemented!
        #if self.path:
        #    acceleration = (self.path[0] - self.pos).scale_to_length(self.maxacceleration)
        #    self.speed += acceleration * delta
        if self.speed.length() > self.topspeed:
            self.speed.scale_to_length(self.topspeed)
        self.move(self.speed)

    def draw(self, screen):
        screen.blit(self.surface, self.pos)
    
class Bullet(Collideable):
    def __init__(self, pos, speed, game):
        super().__init__(pos, game)
        self.speed = Vec(speed)
        self.oldpos = Vec(pos)

    def update(self, delta):
        self.oldpos = self.pos
        self.move(self.speed)

    def draw(self, screen):
        line(screen, self.oldpos.x, self.oldpos.y, self.pos.x, self.pos.y,
                (100, 0, 0))

