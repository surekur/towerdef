from widgets import UIElement
from pygame.math import Vector2 as Vec
from constans import *
from utils import get_image

canbuild = get_image("data/can-build.png")
cantbuild = get_image("data/cant-build.png")
class Game(UIElement):
    """
    This is the widget where we implementing our actual game word.
    """
    def __init__(self, parent, area, battlefield):
        super().__init__(parent, area)
        self.battlefield = battlefield
        self.ents = set()
        self.foes = set()
        self.systems = []
        self.tileundercursor = Vec(0, 0)
        self.thinkerent = 0

    def on_hover(self, pos):
        self.tileundercursor = Vec(pos) // TILESIZE

    def update(self, delta):
        # only 1 entity "thinks" per framestep.
        i = 0
        if self.thinkerent > len(self.ents):
            self.thinkerent = 0
        for ent in self.ents:
            if self.thinkerent == i:
                ent.on_think()
                self.thinkerent += 1
            ent.update
            ent.test_collision(self.ents)
        self.re_draw()
        for system in self.systems:
            system.update(delta)

    def re_draw(self):
        self.surface.fill((20,20,230))
        for cords in self.battlefield:
            pos = Vec(cords) * TILESIZE
            self.battlefield[cords].draw(pos, self.surface)
        for ent in self.ents:
            ent.draw(self.surface)

        tilehash = tuple(self.tileundercursor)
        if tilehash in self.battlefield:
            if self.battlefield[tilehash].canbuildonto:
                buildcursor = canbuild
            else:
                buildcursor = cantbuild
            self.surface.blit(buildcursor, Vec(self.tileundercursor) * TILESIZE)
        self.parent.re_draw()

