import pygame
from pygame.locals import *


class Perso(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = True
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400 - 25
        self.rect.y = 600 - 70

    def move(self, direction):
        if direction == 'right' and self.rect.x < 750:
            self.rect.x += self.velocity
        elif direction == 'left' and self.rect.x > 0:
            self.rect.x -= self.velocity

    def attack(self):
        pass

    def isDead(self):
        pass
