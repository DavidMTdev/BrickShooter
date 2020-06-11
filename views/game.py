
import pygame
import pygame_gui
from pygame.locals import *
from pygame_gui import UIManager
from pygame_gui.elements import UILabel, UIImage, UIPanel, UIButton
from controllers.perso import Perso


class Game:
    def __init__(self):

        self.manager = UIManager((800, 600))

        image = pygame.image.load('assets/original.gif')

        self.background = UIImage(relative_rect=pygame.Rect(0, 0, 800, 600),
                                  manager=self.manager,  image_surface=image)

        self.player = Perso()
        self.pressed = {}

        self.playerImage = UIImage(relative_rect=pygame.Rect((self.player.rect.x, self.player.rect.y), (50, 50)),
                                   manager=self.manager,  image_surface=self.player.image)

        # self.panel = None
        # self.buttonQuit = None
        # self.buttonContinue = None
        # self.escapeActive = False

    def getManager(self):
        return self.manager

    def updatePosPlayer(self):
        self.playerImage.set_relative_position((self.player.rect.x, self.player.rect.y))

    def getEvent(self, event):
        if event.type == KEYDOWN:
            self.pressed[event.key] = True
        elif event.type == KEYUP:
            self.pressed[event.key] = False

        # if event.type == pygame.USEREVENT:
        #     if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        #         # if event.ui_element == self.buttonContinue:
        #         pass
