import pygame
from pygame.locals import *
import pygame_gui
from controllers.route import Route


class App:
    def __init__(self):

        pygame.init()

        pygame.display.set_caption('Quick Start')

        self.screen = pygame.display.set_mode((800, 600), RESIZABLE)

        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(pygame.Color('#ffffff'))

        self.route = Route('login')

        self.clock = pygame.time.Clock()
        self.isRunning = True

    def run(self):
        while self.isRunning:
            timeDelta = self.clock.tick(60)/1000.0

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.isRunning = False

                self.route.homeRoute(event)
                self.route.loginRoute(event)
                self.route.signupRoute(event)

                self.route.uiManager.process_events(event)

            self.route.uiManager.update(timeDelta)

            self.screen.blit(self.background, (0, 0))
            self.route.uiManager.draw_ui(self.screen)

            pygame.display.update()
