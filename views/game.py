
import pygame
import pygame_gui
from pygame.locals import *
from pygame_gui import UIManager
from pygame_gui.elements import UILabel, UIImage, UIPanel, UIButton
from controllers.perso import Perso
from controllers.enemy import Enemy
from controllers.niveau import Niveau


class Game:
    def __init__(self, session):
        self.manager = UIManager((800, 600), 'themes/game.json')
        image = pygame.image.load('assets/background.png')

        self.background = UIImage(relative_rect=pygame.Rect(0, 0, 800, 600),
                                  manager=self.manager,  image_surface=image)

        self.session = session
        self.allPlayers = pygame.sprite.Group()
        self.player = Perso(self, self.session)
        self.allPlayers.add(self.player)
        self.pressed = {}
        self.allEnemy = pygame.sprite.Group()
        self.addScore = 100
        self.score = 0
        self.level = Niveau(self, self.score)

        self.panelTop = UIPanel(relative_rect=pygame.Rect(0, 0, 800, 20), starting_layer_height=2,
                                manager=self.manager, object_id="#panel-top")

        self.labelHealthTitle = UILabel(relative_rect=pygame.Rect(0, 0, 50, 20),
                                        text="Vie :",
                                        manager=self.manager, object_id="#label-score", container=self.panelTop)

        self.labelHealth = UILabel(relative_rect=pygame.Rect(30, 0, 50, 20),
                                   text=str(self.player.health),
                                   manager=self.manager, object_id="#label-score", container=self.panelTop)

        self.labelAsset = UILabel(relative_rect=pygame.Rect(800 - 100, 0, 50, 20),
                                  text=str(self.level.assetIsActive[2]),
                                  manager=self.manager, object_id="#label-score", container=self.panelTop)

        self.labelScore = UILabel(relative_rect=pygame.Rect(0, 600 - 50, 200, 50),
                                  text=str(self.score),
                                  manager=self.manager, object_id="#label-score")

        self.playerImage = UIImage(relative_rect=pygame.Rect((self.player.rect.x, self.player.rect.y), (50, 50)),
                                   manager=self.manager,  image_surface=self.player.image)

        self.panel = UIPanel(relative_rect=pygame.Rect((0, 0),
                                                       (0, 0)), starting_layer_height=3,
                             manager=self.manager, object_id="#panel-game-over")

        self.labelGameOver = UILabel(relative_rect=pygame.Rect(400 - 100, 300 - 50, 200, 50),
                                     text="Game Over",
                                     manager=self.manager, object_id="#label-game-over", container=self.panel)

        self.buttonMenu = UIButton(relative_rect=pygame.Rect(400 - 100, 300 + 50, 200, 50), text='Quitter',
                                   manager=self.manager, container=self.panel)

        self.buttonParty = UIButton(
            relative_rect=pygame.Rect((400 - 100, 300 + 50 + 80),
                                      (200, 50)),
            text='Recommencer', manager=self.manager, container=self.panel)

        self.panelPause = UIPanel(relative_rect=pygame.Rect((0, 0),
                                                            (0, 0)), starting_layer_height=3,
                                  manager=self.manager, object_id="#panel-game-over")

        self.labelPause = UILabel(relative_rect=pygame.Rect(400 - 100, 300 - 50, 200, 50),
                                  text="Pause",
                                  manager=self.manager, object_id="#label-game-over", container=self.panelPause)

        self.buttonSave = UIButton(relative_rect=pygame.Rect(400 - 100, 300 + 50, 200, 50),
                                   text='Sauvegarder et quitter', manager=self.manager, container=self.panelPause)

        self.buttonQuit = UIButton(
            relative_rect=pygame.Rect((400 - 100, 300 + 50 + 80),
                                      (200, 50)),
            text='Quitter', manager=self.manager, container=self.panelPause)

        self.panelAsset = UIPanel(relative_rect=pygame.Rect((0, 0),
                                                            (0, 0)), starting_layer_height=3,
                                  manager=self.manager, object_id="#panel-game-over")

        self.labelEquipment = UILabel(relative_rect=pygame.Rect(400 - 100, 50, 200, 50),
                                      text="Pause",
                                      manager=self.manager, object_id="#label-game-over", container=self.panelAsset)

        self.button1 = UIButton(relative_rect=pygame.Rect(400 - 100, 50 + 50, 200, 50),
                                text="Double l'attaque 10C", manager=self.manager, container=self.panelAsset)

        self.button2 = UIButton(
            relative_rect=pygame.Rect((400 - 100, 120 + 50),
                                      (200, 50)),
            text='3 Missiles 100C', manager=self.manager, container=self.panelAsset)

        self.button3 = UIButton(
            relative_rect=pygame.Rect((400 - 100, 190 + 50),
                                      (200, 50)),
            text='Double Score 20C', manager=self.manager, container=self.panelAsset)

        self.button4 = UIButton(
            relative_rect=pygame.Rect((400 - 100, 260 + 50),
                                      (200, 50)),
            text="Temps d'apparition 50C", manager=self.manager, container=self.panelAsset)

        self.labelCredit = UILabel(relative_rect=pygame.Rect(400 - 100, 330 + 50, 200, 50),
                                   text=str(self.player.credit),
                                   manager=self.manager, object_id="#label-game-over", container=self.panelAsset)

        self.pause = True

    def menuGameOver(self):
        self.panel.set_dimensions((800, 600))

    def setLabelHealth(self):
        self.labelHealth.set_text(str(self.player.health))

    def setLabelScore(self):
        self.labelScore.set_text(str(self.score))

    def setLabelAsset(self):
        self.labelAsset.set_text(str(self.level.assetIsActive[2]))

    def setLabelCredit(self):
        self.player.credit += 1
        self.labelCredit.set_text(str(self.player.credit))

    def getManager(self):
        return self.manager

    def updatePosPlayer(self):
        self.playerImage.set_relative_position((self.player.rect.x, self.player.rect.y))

    def getPause(self):
        return self.pause

    def getEvent(self, event):
        if not self.player.isDead():
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.buttonQuit:
                        pygame.quit()
                    elif event.ui_element == self.buttonSave:
                        self.session.setCredit(self.player.credit)
                        self.session.setScore(self.score)
                        pygame.quit()

                    elif event.ui_element == self.button1:
                        if self.player.credit >= 10 and self.level.assetIsActive[0] == False:
                            self.player.credit -= 10
                            self.player.getSurprise("damage")

                            self.panelAsset.set_dimensions((0, 0))

                            self.pause = True
                    elif event.ui_element == self.button2:
                        if self.player.credit >= 100 and self.level.assetIsActive[0] == False:
                            self.player.credit -= 100
                            self.player.getSurprise("attack")

                            self.panelAsset.set_dimensions((0, 0))
                            self.pause = True
                    elif event.ui_element == self.button3:
                        if self.player.credit >= 20 and self.level.assetIsActive[0] == False:
                            self.player.credit -= 20
                            self.player.getSurprise("score")

                            self.panelAsset.set_dimensions((0, 0))
                            self.pause = True
                    elif event.ui_element == self.button4:
                        if self.player.credit >= 50 and self.level.assetIsActive[0] == False:
                            self.player.credit -= 50
                            self.player.getSurprise("reload")

                            self.panelAsset.set_dimensions((0, 0))
                            self.pause = True

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    if self.pause:
                        self.panelPause.set_dimensions((800, 600))
                        self.pause = False

                    else:
                        self.panelPause.set_dimensions((0, 0))
                        self.pause = True

                    return self.pause

                if event.key == pygame.K_RETURN:

                    if self.pause:
                        self.panelAsset.set_dimensions((800, 600))
                        self.pause = False

                    else:
                        self.panelAsset.set_dimensions((0, 0))
                        self.pause = True

                    return self.pause

                if event.key == pygame.K_SPACE:
                    self.player.attack(self.manager)

                self.pressed[event.key] = True
            elif event.type == KEYUP:
                self.pressed[event.key] = False
            return None
        else:
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.buttonParty:
                        return "restart"
                    elif event.ui_element == self.buttonMenu:
                        pygame.quit()

    def updatePosEnemy(self, enemy, x, y):
        enemy.ennemyImage.set_relative_position((x, y))

    def spawnEnemy(self, health, x, asset):
        enemy = Enemy(health, self.manager, x, self, asset)
        self.updatePosEnemy(enemy, enemy.rect.x, enemy.rect.y)
        self.allEnemy.add(enemy)

    def checkColision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def run(self):
        self.level.generate()
        self.level.setScore(self.score)
