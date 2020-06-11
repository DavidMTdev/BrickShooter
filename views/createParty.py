
import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
# from controllers.main import App


class CreateParty:
    def __init__(self):

        self.manager = UIManager((800, 600), 'themes/createParty.json')

        self.labelParty = UILabel(relative_rect=pygame.Rect(10, 92, 150, 50),
                                  text='Nom de la partie',
                                  manager=self.manager)

        self.party = UITextEntryLine(relative_rect=pygame.Rect(330, 100, 150, 50),
                                     manager=self.manager)

        self.buttonCreate = UIButton(relative_rect=pygame.Rect(330, 200, 150, 50),
                                     text='Creer une partie',
                                     manager=self.manager)

    def getManager(self):
        return self.manager

    def getButtonCreate(self):
        return self.buttonCreate

    def getParty(self):
        return self.party

    def getView(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.getButtonCreate():
                    return "game"

        return self
