
import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UILabel


class Home:
    def __init__(self):

        self.manager = UIManager((800, 600), 'themes/home.json')

        self.title = UILabel(relative_rect=pygame.Rect(400 - 100, 20, 200, 50),
                             text='Accueil',
                             manager=self.manager, object_id='#title')

        self.buttonCreating = UIButton(relative_rect=pygame.Rect(400 - 100, 100, 200, 50),
                                       text='Creer partie',
                                       manager=self.manager)

        self.buttonLoading = UIButton(relative_rect=pygame.Rect(400 - 100, 180, 200, 50),
                                      text='Charger une partie',
                                      manager=self.manager)

        self.buttonInstruction = UIButton(relative_rect=pygame.Rect(400 - 100, 260, 200, 50),
                                          text='Instruction',
                                          manager=self.manager)

        self.buttonShop = UIButton(relative_rect=pygame.Rect(400 - 100, 340, 200, 50),
                                   text='Magasin',
                                   manager=self.manager)

        self.buttonRanking = UIButton(relative_rect=pygame.Rect(400 - 100, 420, 200, 50),
                                      text='Classement',
                                      manager=self.manager)

        self.buttonLogout = UIButton(relative_rect=pygame.Rect(800 - 220, 20, 200, 50),
                                     text='Déconnexion',
                                     manager=self.manager, object_id='#button-logout')

    def getManager(self):
        return self.manager

    def getView(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.buttonCreating:
                    return "creating"
                elif event.ui_element == self.buttonLoading:
                    return "loading"
                elif event.ui_element == self.buttonInstruction:
                    return "instruction"
                elif event.ui_element == self.buttonShop:
                    return "shop"
                elif event.ui_element == self.buttonRanking:
                    return "ranking"
                elif event.ui_element == self.buttonLogout:
                    return "logout"

        return self
