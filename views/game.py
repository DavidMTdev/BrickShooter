
import pygame
import pygame_gui
from pygame.locals import *
from pygame_gui import UIManager
from pygame_gui.elements import UILabel, UIImage, UIPanel, UIButton
from controllers.perso import Perso
from controllers.enemy import Enemy


class Game:
    def __init__(self):

        self.manager = UIManager((800, 600))

        image = pygame.image.load('assets/background.png')

        self.background = UIImage(relative_rect=pygame.Rect(0, 0, 800, 600),
                                  manager=self.manager,  image_surface=image)

        self.allPlayers = pygame.sprite.Group()
        self.player = Perso()
        self.allPlayers.add(self.player)
        self.pressed = {}
        self.allEnemy = pygame.sprite.Group()

        for i in range(0, 11):
            self.spawnEnemy(1, 75 * i)

        self.playerImage = UIImage(relative_rect=pygame.Rect((self.player.rect.x, self.player.rect.y), (50, 50)),
                                   manager=self.manager,  image_surface=self.player.image)

    def getManager(self):
        return self.manager

    def updatePosPlayer(self):
        self.playerImage.set_relative_position((self.player.rect.x, self.player.rect.y))

    def getEvent(self, event):
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
        return pygame.sprite.spritecollide(sprite, group, False)

        # if event.type == pygame.USEREVENT:
        #     if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        #         # if event.ui_element == self.buttonContinue:
        #         pass
