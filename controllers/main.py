import pygame
from pygame.locals import *
import pygame_gui
from controllers.route import Route


class App:
    def __init__(self):

        pygame.init()

        pygame.display.set_caption('Quick Start')

        self.screen = pygame.display.set_mode((800, 600))

        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(pygame.Color('#4D4D4D'))

        self.route = Route('login')

        self.clock = pygame.time.Clock()
        self.isRunning = True

    def run(self):
        while self.isRunning:
            timeDelta = self.clock.tick(60)/1000.0

            if self.route.getRoute() == 'game':

                if self.route.game.getPause():
                    if not self.route.game.player.isDead():
                        self.route.pressed()

                        self.route.game.run()

                        for missile in self.route.game.player.allMissile:
                            missile.move()

                        self.route.getAllEnemy().draw(self.screen)
                        for enemy in self.route.game.allEnemy:
                            enemy.down()
                    else:
                        self.route.game.menuGameOver()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

                if self.route.getRoute() == 'home':
                    self.route.homeRoute(event)
                if self.route.getRoute() == 'login':
                    self.route.loginRoute(event)
                if self.route.getRoute() == 'signup':
                    self.route.signupRoute(event)
                if self.route.getRoute() == 'creating':
                    self.route.CreatePartyRoute(event)
                if self.route.getRoute() == 'game':
                    self.route.gameRoute(event)

                self.route.uiManager.process_events(event)

            self.route.uiManager.update(timeDelta)

            self.screen.blit(self.background, (0, 0))

            self.route.uiManager.draw_ui(self.screen)
            # pygame.display.flip()
            pygame.display.update()
