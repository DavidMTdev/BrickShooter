import pygame
from pygame.locals import *
from pygame_gui.elements import UIImage


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, manager, x, game):
        super().__init__()
        self.game = game
        self.health = health
        self.velocity = 2
        self.image = pygame.image.load('assets/player.png')
        self.ennemyImage = UIImage(relative_rect=pygame.Rect((0, 0), (50, 50)),
                                   manager=manager,  image_surface=self.image)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = -100

    def down(self):
        # if not self.game.checkColision(self, self.game.allPlayers):
        self.rect.y += self.velocity
        self.ennemyImage.set_position((self.rect.x, self.rect.y))
        if self.rect.y > 530:
            self.remove()

    def remove(self):
        self.ennemyImage.kill()
        self.game.allEnemy.remove(self)
        self.game.player.health -= 1
        print(self.game.player.health)
