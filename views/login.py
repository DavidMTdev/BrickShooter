
import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel


class Login:
    def __init__(self):

        self.manager = UIManager((800, 600), 'themes/theme.json')                            

        self.title = UILabel(relative_rect=pygame.Rect(350, 50, 100, 50),
                                      text='Connexion',
                                      manager=self.manager)

        self.labelPseudo = UILabel(relative_rect=pygame.Rect(255, 142, 100, 50),
                                      text='Pseudo',
                                      manager=self.manager)

        self.pseudo = UITextEntryLine(relative_rect=pygame.Rect(330, 150, 150, 50),
                                      manager=self.manager)

        self.labelPassword = UILabel(relative_rect=pygame.Rect(230, 222, 100, 50),
                                      text='Mot de passe',
                                      manager=self.manager)

        self.password = UITextEntryLine(relative_rect=pygame.Rect(330, 230, 150, 50),
                                        manager=self.manager)

        self.buttonLogin = UIButton(relative_rect=pygame.Rect(350, 320, 110, 50),
                                     text='Se connecter',
                                     manager=self.manager)

        self.buttonSignup = UIButton(relative_rect=pygame.Rect(330, 400, 150, 50),
                                     text='Pas de compte ?',
                                     manager=self.manager) 

    def getManager(self):
        return self.manager

    def getButtonLogin(self):
        return self.buttonLogin

    def getButtonSignup(self):
        return self.buttonSignup

    def getPseudo(self):
        return self.pseudo

    def getPassword(self):
        return self.password

    def getInstance(self):
        return self

    def getView(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.getButtonLogin():
                    return 'home'
                if event.ui_element == self.getButtonSignup():
                    return 'signup'

        return self
