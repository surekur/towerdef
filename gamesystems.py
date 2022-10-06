import ents
from random import randint
from constans import *
from pygame.math import Vector2 as Vec

class FoeSpawner(ents.Entity):
    def __init__(self, game):
        super().__init__((0,0), game)
        self.possiblefoes = [ents.Truck]

    def update(self, delta):
        # We only spawning 
        n = 100
        i = randint(0, n)
        if i < len(self.possiblefoes):
            pos = Vec(21* TILESIZE, randint(0, 20)*TILESIZE)
            self.game.ents.add(self.possiblefoes[i](pos, self.game))

