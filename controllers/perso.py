import pygame
from controllers.missile import Missile
# from models.player import Player


class Perso(pygame.sprite.Sprite):
    def __init__(self, game, session):
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
        self.attackIsActive = False
        self.credit = session.credit
        print(self.credit)

    def move(self, direction):
        if direction == 'right' and self.rect.x < 750:
            self.rect.x += self.velocity
        elif direction == 'left' and self.rect.x > 0:
            self.rect.x -= self.velocity

    def attack(self, manager):
        self.allMissile.add(Missile(self, manager, 0))

        if self.attackIsActive:
            self.allMissile.add(Missile(self, manager, 20))
            self.allMissile.add(Missile(self, manager, -20))

    def hit(self):
        if self.health > 0:
            self.health -= 1
            self.game.setLabelHealth()

        return True

    def isDead(self):
        if self.health <= 0:
            return True
        return False

    def getSurprise(self, asset):
        if asset != False and self.game.level.assetIsActive[2] == "":

            if asset == "damage":
                self.damage += 1
                self.game.level.assetIsActive[0] = True
                self.game.level.assetIsActive[2] = "damage"
                self.game.level.assetIsActive[1] += 1000  # 1000 equivalent à 10 apparition de ligne ennemie

            elif asset == "reload":
                self.game.level.reload = 200

            elif asset == "attack":
                self.attackIsActive = True
                self.game.level.assetIsActive[0] = True
                self.game.level.assetIsActive[1] += 400
                self.game.level.assetIsActive[2] = "attack"

            elif asset == "score":
                self.game.score += 200
                self.game.level.assetIsActive[0] = True
                self.game.level.assetIsActive[1] += 500
                self.game.level.assetIsActive[2] = "score"

            self.game.setLabelAsset()
