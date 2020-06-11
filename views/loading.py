
import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UILabel, UIPanel, UIScrollingContainer, UIVerticalScrollBar


class Loading:
    def __init__(self):

        self.manager = UIManager((800, 600), 'themes/loading.json')

        self.title = UILabel(relative_rect=pygame.Rect(400 - 100, 20, 200, 50),
                             text='Charger une partie',
                             manager=self.manager, object_id='#title')
        self.scrollingContainer = UIScrollingContainer(relative_rect=pygame.Rect(100, 100, 700, 400),
                                                       manager=self.manager)

        self.verticalScrollBar = UIVerticalScrollBar(
            relative_rect=pygame.Rect(680, 0, 20, 400),
            manager=self.manager, visible_percentage=0.8, container=self.scrollingContainer)

        self.background = UIPanel(relative_rect=pygame.Rect(0, 0, 500, 80), starting_layer_height=0,
                                  manager=self.manager, container=self.scrollingContainer)

        self.name = UILabel(relative_rect=pygame.Rect(10, 10, 200, 20),
                            text='Charger une partie',
                            manager=self.manager, object_id='#text-button', container=self.background)

        self.date = UILabel(relative_rect=pygame.Rect(300, 10, 200, 20),
                            text='date de la partie',
                            manager=self.manager, object_id='#text-button', container=self.background)

        self.currentScore = UILabel(relative_rect=pygame.Rect(10, 40, 200, 20),
                                    text='45544',
                                    manager=self.manager, object_id='#text-button', container=self.background)

        self.maxScore = UILabel(relative_rect=pygame.Rect(300, 40, 200, 20),
                                text='1255454',
                                manager=self.manager, object_id='#text-button', container=self.background)

        self.buttonCreating = UIButton(relative_rect=pygame.Rect(0, 0, 500, 80), text='',
                                       manager=self.manager, container=self.scrollingContainer)

        self.buttonLogout = UIButton(relative_rect=pygame.Rect(800 - 220, 20, 200, 50),
                                     text='Déconnexion',
                                     manager=self.manager, object_id='#button-logout')

    def createButton(self):
        pass

    def getManager(self):
        return self.manager

    def getView(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                print(self.verticalScrollBar)
                # 'scrolling_container.vertical_scroll_bar.#bottom_button'
                # 'scrolling_container.vertical_scroll_bar.#top_button
                # 'ui_object_id': 'scrolling_container.vertical_scroll_bar.#sliding_button'

                if event.ui_object_id == 'scrolling_container.vertical_scroll_bar.#sliding_button':
                    print(event)
                elif event.ui_object_id == 'scrolling_container.vertical_scroll_bar.#top_button':
                    pass
                elif event.ui_object_id == 'scrolling_container.vertical_scroll_bar.#bottom_button':
                    pass

                if event.ui_element == self.buttonCreating:
                    print("fdhuhdgqjdkhfsfdskfdsfsqffqd")
                    return "loading"
                elif event.ui_element == self.buttonLogout:
                    return "loading"

        return self
