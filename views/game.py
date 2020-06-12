
import pygame
import pygame_gui
from pygame.locals import *
from pygame_gui import UIManager
from pygame_gui.elements import UILabel, UIImage, UIPanel, UIButton
from controllers.perso import Perso
from controllers.enemy import Enemy


class Game:
    def __init__(self):
        self.manager = UIManager((800, 600), 'themes/game.json')

        image = pygame.image.load('assets/background.png')

        self.background = UIImage(relative_rect=pygame.Rect(0, 0, 800, 600),
                                  manager=self.manager,  image_surface=image)

        self.allPlayers = pygame.sprite.Group()
        self.player = Perso(self)
        self.allPlayers.add(self.player)
        self.pressed = {}
        self.allEnemy = pygame.sprite.Group()
        self.score = 0

        self.labelScore = UILabel(relative_rect=pygame.Rect(0, 600 - 50, 200, 50),
                                  text=str(self.score),
                                  manager=self.manager, object_id="#label-score")

        self.playerImage = UIImage(relative_rect=pygame.Rect((self.player.rect.x, self.player.rect.y), (50, 50)),
                                   manager=self.manager,  image_surface=self.player.image)

    def menuGameOver(self):

        self.panel = UIPanel(relative_rect=pygame.Rect(0, 0, 800, 600), starting_layer_height=1,
                             manager=self.manager, object_id="#panel-game-over")

        self.labelGameOver = UILabel(relative_rect=pygame.Rect(400 - 100, 300 - 50, 200, 50),
                                     text="Game Over",
                                     manager=self.manager, object_id="#label-game-over", container=self.panel)

        self.buttonMenu = UIButton(relative_rect=pygame.Rect(400 - 100, 300 + 50, 200, 50), text='Revenir au menu',
                                   manager=self.manager, container=self.panel)

        self.buttonParty = UIButton(
            relative_rect=pygame.Rect((400 - 100, 300 + 50 + 80),
                                      (200, 50)),
            text='Recommencer', manager=self.manager, container=self.panel)

    def setLabelScore(self):
        self.labelScore.set_text(str(self.score))

    def getManager(self):
        return self.manager

    def updatePosPlayer(self):
        self.playerImage.set_relative_position((self.player.rect.x, self.player.rect.y))

    def getEvent(self, event):
        if not self.player.isDead():
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.attack(self.manager)

                self.pressed[event.key] = True
            elif event.type == KEYUP:
                self.pressed[event.key] = False

    def updatePosEnemy(self, enemy, x, y):
        enemy.ennemyImage.set_relative_position((x, y))

    def spawnEnemy(self, health, x):
        enemy = Enemy(health, self.manager, x, self)
        self.updatePosEnemy(enemy, enemy.rect.x, enemy.rect.y)
        self.allEnemy.add(enemy)

    def checkColision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
