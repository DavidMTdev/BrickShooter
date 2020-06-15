
import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel


class Signup:
    def __init__(self):

        self.manager = UIManager((800, 600), 'themes/signup.json')

        self.title = UILabel(relative_rect=pygame.Rect(350, 50, 100, 50),
                                      text='Inscription',
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

        self.buttonSignup = UIButton(relative_rect=pygame.Rect(350, 320, 110, 50),
                                     text="S'inscrire",
                                     manager=self.manager)

        self.buttonLogin = UIButton(relative_rect=pygame.Rect(330, 400, 150, 50),
                                     text="Déja un compte ?",
                                     manager=self.manager)

    def getManager(self):
        return self.manager

    def getButtonSignup(self):
        return self.buttonSignup

    def getButtonLogin(self):
        return self.buttonLogin

    def getPseudo(self):
        return self.pseudo

    def getPassword(self):
        return self.password

    def getView(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.getButtonSignup():
                    return 'home'
                if event.ui_element == self.getButtonLogin():
                    return 'login'    
        return self
