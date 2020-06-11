
import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UITextEntryLine
# from controllers.main import App


class Home:
    def __init__(self):

        self.manager = UIManager((800, 600), 'themes/home.json')

        self.labelPseudo = UILabel(relative_rect=pygame.Rect(255, 92, 100, 50),
                                   text='Pseudo',
                                   manager=self.manager)

        self.button1 = UIButton(relative_rect=pygame.Rect(30, 20, 100, 50),
                                text='inscription',
                                manager=self.manager, object_id='#id2')

        self.button2 = UIButton(relative_rect=pygame.Rect(100, 100, 100, 50),
                                text='connexion',
                                manager=self.manager, object_id='#id1')

    def getManager(self):
        return self.manager

    def getButton1(self):
        return self.button1

    def getButton2(self):
        return self.button2

    def getView(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.getButton1():
                    return "signup"
                if event.ui_element == self.getButton2():
                    return "login"

        return self
