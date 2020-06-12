import pygame
from controllers.missile import Missile


class Perso(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 3
        # self.attack = 1
        self.velocity = 10
        self.allMissile = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400 - 25
        self.rect.y = 600 - 70

    def move(self, direction):
        if direction == 'right' and self.rect.x < 750:
            self.rect.x += self.velocity
        elif direction == 'left' and self.rect.x > 0:
            self.rect.x -= self.velocity

    def attack(self, manager):
        self.allMissile.add(Missile(self, manager))

    def isDead(self):
        pass
