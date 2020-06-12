import pygame
from pygame.locals import *


class Niveau:

    def __init__(self, game, level):
        self.game = game
        self.level = level
        self.enemy1 = 95
        self.enemy2 = 0
        self.enemy3 = 0
        self.enemySurprise = 5

    def generate(self):
        for i in range(0, 11):
            self.game.spawnEnemy(2, 75 * i)
