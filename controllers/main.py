import pygame
from pygame.locals import *
import pygame_gui
from views.login import Login
from views.signup import Signup


class App:
    def __init__(self):

        pygame.init()

        pygame.display.set_caption('Quick Start')
        self.screen = pygame.display.set_mode((800, 600), RESIZABLE)

        self.background = pygame.Surface((800, 600))
        self.background.fill(pygame.Color('#ffffff'))

        self.uiManager = None
        # instances = [[Login(), True], [Signup(), False]]

        self.signup = Signup()
        self.login = Login()

        self.clock = pygame.time.Clock()
        self.isRunning = True

    def run(self):
        while self.isRunning:
            time_delta = self.clock.tick(60)/1000.0

            if self.uiManager is None:
                self.uiManager = self.login.getManager()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.isRunning = False

                if self.login.getView(event, self.signup) != self.login:
                    self.uiManager = self.login.getView(event, self.signup).getManager()

                elif self.signup.getView(event, self.login) != self.signup:
                    self.uiManager = self.signup.getView(event, self.login).getManager()

                # for instance in instances:
                #     if instance[0].getView(event) == instance[0] and instance[1] != True:
                #         manager = instance[0].getView(event).getManager()

                #         for instance2 in instances:
                #             if instance2[1] == True and manager == instance2[0].getManager():
                #                 instance2[1] = False
                #                 instance[1] = True

                self.uiManager.process_events(event)

            # print(instances)

            self.uiManager.update(time_delta)

            self.screen.blit(self.background, (0, 0))
            self.uiManager.draw_ui(self.screen)

            pygame.display.update()
