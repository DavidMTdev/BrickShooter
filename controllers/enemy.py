import pygame
from pygame.locals import *
from pygame_gui.elements import UIImage


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, manager, x, game, asset):
        super().__init__()
        self.game = game
        self.health = health
        self.asset = asset
        self.velocity = 1
        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.ennemyImage = UIImage(relative_rect=pygame.Rect((0, 0), (50, 50)),
                                   manager=manager,  image_surface=self.image)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = -100

    def down(self):
        if not self.game.checkColision(self, self.game.allPlayers):
            self.rect.y += self.velocity
            self.ennemyImage.set_position((self.rect.x, self.rect.y))
        else:
            if self.game.player.hit():
                self.remove()

        if self.rect.y > 530:
            self.game.score -= 50
            self.game.setLabelScore()
            self.remove()

    def remove(self):
        self.ennemyImage.kill()
        self.game.allEnemy.remove(self)


    
