from views.login import Login
from views.signup import Signup
from views.home import Home
from views.loading import Loading
from views.game import Game
from views.createParty import CreateParty
from controllers.auth import Auth
from controllers.part import Part
import pygame
from pygame.locals import *


class Route():
    def __init__(self, route):
        self.signup = Signup()
        self.login = Login()
        self.home = Home()
        # self.loading = Loading()

        self.createParty = CreateParty()

        self.session = None
        self.party = None

        self.route = route
        self.uiManager = self.login.getManager()

    def getRoute(self):
        return self.route

    def setRoute(self, route):
        self.route = route

    def homeRoute(self, event):
        if self.home.getView(event) != self.home:
            if self.home.getView(event) == 'signup':
                self.uiManager = self.signup.getManager()
                self.setRoute('signup')
            elif self.home.getView(event) == 'creating':
                self.uiManager = self.createParty.getManager()
                self.setRoute('creating')

    def loginRoute(self, event):
        # if self.getRoute() == 'login':
        if self.login.getView(event) != self.login:
            if self.login.getView(event) == 'home':
                pseudo = self.login.getPseudo().get_text()
                password = self.login.getPassword().get_text()
                self.session = Auth().login(pseudo, password)

                if self.session:
                    self.uiManager = self.home.getManager()
                    self.setRoute('home')

            elif self.login.getView(event) == 'signup':
                self.uiManager = self.signup.getManager()
                self.setRoute('signup')

    def signupRoute(self, event):
        # if self.getRoute() == 'signup':
        if self.signup.getView(event) != self.signup:
            if self.signup.getView(event) == 'home':
                pseudo = self.signup.getPseudo().get_text()
                password = self.signup.getPassword().get_text()
                self.session = Auth().register(pseudo, password)

                if self.session:
                    self.uiManager = self.home.getManager()
                    self.setRoute('home')

            elif self.signup.getView(event) == 'login':
                self.uiManager = self.login.getManager()
                self.setRoute('login')

    # def loadingRoute(self, event):
    #     # if self.getRoute() == 'loading':
    #     if self.loading.getView(event) != self.loading:
    #         if self.loading.getView(event) == 'signup':
    #             self.uiManager = self.signup.getManager()
    #             self.setRoute('signup')

    #         elif self.home.getView(event) == 'creating':
    #             self.uiManager = self.createParty.getManager()
    #             self.setRoute('creating')

    def CreatePartyRoute(self, event):
        if self.getRoute() == 'creating':
            if self.createParty.getView(event) != self.createParty:
                if self.createParty.getView(event) == 'game':
                    name = self.createParty.getParty().get_text()

                    self.party = Part().createParty(name)

                    if self.party:
                        self.game = Game()
                        self.uiManager = self.game.getManager()
                        self.setRoute('game')

    def gameRoute(self, event):
        self.game.getEvent(event)
        print(self.game.pressed)

        self.pressed()

    def pressed(self):
        if self.game.pressed.get(pygame.K_RIGHT):
            print(self.game.pressed)
            self.game.player.move("right")

        elif self.game.pressed.get(pygame.K_LEFT):
            self.game.player.move("left")

        self.game.updatePosPlayer()
