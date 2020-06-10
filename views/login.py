
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

        self.hello_text = UITextEntryLine(relative_rect=pygame.Rect(400, 20, 100, 50),
                                          manager=self.manager, object_id='#id1')

    def getManager(self):
        return self.manager

    def getButton(self):
        return self.hello_button

    def getText(self):
        return self.hello_text

    def getInstance(self):
        return self

    def getView(self, event, instance):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.getButton():
                    return instance

        return self
