import pygame
from pygame.locals import *
from pygame_gui.elements import UIImage


class Missile(pygame.sprite.Sprite):
    def __init__(self, player, manager):
        super().__init__()
        self.velocity = 10
        self.player = player
        self.image = pygame.image.load('assets/missile.png')
        self.image = pygame.transform.scale(self.image, (10, 50))
        # self.rectImage = self.image.get_rect()
        self.missileImage = UIImage(relative_rect=pygame.Rect(
            (self.player.rect.x + 25 - 5, self.player.rect.y - 50),
            (10, 50)),
            manager=manager, image_surface=self.image)
        self.rect = self.image.get_rect()

        self.rect.x = player.rect.x + 25 - 5
        self.rect.y = player.rect.y - 50

    def remove(self):
        self.player.allMissile.remove(self)
        self.missileImage.kill()

    def hit(self, enemy):
        if enemy.health > 0:
            enemy.health -= self.player.damage
            return True

    def isDead(self, enemy):
        if enemy.health <= 0:
            return True

        return False

    def move(self):
        self.rect.y -= self.velocity
        self.missileImage.set_position((self.rect.x, self.rect.y))

        if self.player.game.checkColision(self, self.player.game.allEnemy):
            for enemy in self.player.game.checkColision(self, self.player.game.allEnemy):
                self.hit(enemy)
                if self.isDead(enemy):
                    enemy.remove()
                    self.getSurprise(enemy.asset)
                    enemy.ennemyImage.kill()
                    self.player.game.score += 100
                    self.player.game.setLabelScore()

            self.remove()

        if self.rect.y < 0:
            self.remove()


    def getSurprise(self, asset):
        if asset != False:
            print(asset)
            if asset == "attack":
                if self.player.game.level.attack[0] != True:
                    self.player.damage += 1
                    self.player.game.level.attack[0] = True

                self.player.game.level.attack[1] += 1000 # 1000 equivalent à 10 apparition de ligne ennemie
                print(self.player.game.level.attack[1])

            elif asset == "reload":
                self.player.game.level.reload = 200
                print(self.player.game.level.reload)
