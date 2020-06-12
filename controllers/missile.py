import pygame
from pygame.locals import *
from pygame_gui.elements import UIImage


class Missile(pygame.sprite.Sprite):
    def __init__(self, player, manager):
        super().__init__()
        self.velocity = 10
        self.player = player
        self.image = pygame.image.load('assets/missile.png')
        self.missileImage = UIImage(relative_rect=pygame.Rect(
            (self.player.rect.x + 25 - 5, self.player.rect.y - 50),
            (10, 50)),
            manager=manager, image_surface=self.image)
        self.rect = self.missileImage.get_relative_rect()

        self.rect.x = player.rect.x + 25 - 5
        self.rect.y = player.rect.y - 50

    def remove(self):
        self.player.allMissile.remove(self)
        self.missileImage.kill()

    def move(self):
        self.rect.y -= self.velocity
        self.missileImage.set_position((self.rect.x, self.rect.y))

        if self.rect.y < 0:
            self.remove()
