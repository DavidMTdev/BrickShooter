
import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UITextEntryLine


class Login:
    def __init__(self):

        self.manager = UIManager((800, 600), 'themes/theme.json')

        self.hello_button = UIButton(relative_rect=pygame.Rect(30, 20, 100, 50),
                                     text='Say Hello',
                                     manager=self.manager, object_id='#id2')

        self.pseudo = UITextEntryLine(relative_rect=pygame.Rect(200, 100, 100, 50),
                                      manager=self.manager, object_id='#id1')

        self.password = UITextEntryLine(relative_rect=pygame.Rect(200, 400, 100, 50),
                                        manager=self.manager, object_id='#id1')

    def getManager(self):
        return self.manager

    def getButton(self):
        return self.hello_button

    def getPseudo(self):
        return self.pseudo

    def getPassword(self):
        return self.password

    def getInstance(self):
        return self

    def getView(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.getButton():
                    return 'home'

        return self
