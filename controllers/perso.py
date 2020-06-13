import pygame
from controllers.missile import Missile


class Perso(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.health = 3
        self.game = game
        self.damage = 1
        self.velocity = 10
        self.allMissile = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
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

    def hit(self):
        if self.health > 0:
            self.health -= 1

        return True

    def isDead(self):
        if self.health <= 0:
            return True
        return False
