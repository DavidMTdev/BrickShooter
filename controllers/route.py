from views.login import Login
from views.signup import Signup
from views.home import Home
from controllers.auth import Auth


class Route():
    def __init__(self, route):
        self.signup = Signup()
        self.login = Login()
        self.home = Home()

        self.route = route
        self.uiManager = self.login.getManager()

    def getRoute(self):
        return self.route

    def setRoute(self, route):
        self.route = route

    def homeRoute(self, event):
        if self.getRoute() == 'home':
            if self.home.getView(event) != self.home:
                if self.home.getView(event) == 'signup':
                    self.uiManager = self.signup.getManager()
                    self.setRoute('signup')

                elif self.home.getView(event) == 'login':
                    self.uiManager = self.login.getManager()
                    self.setRoute('login')


    def loginRoute(self, event):
        if self.getRoute() == 'login':
            if self.login.getView(event) != self.login:
                if self.login.getView(event) == 'home':

                    pseudo = self.login.getPseudo().get_text()
                    password = self.login.getPassword().get_text()

                    success = Auth().login(pseudo, password)

                    if success is True:
                        self.uiManager = self.home.getManager()
                        self.setRoute('home')
                        
                elif self.login.getView(event) == 'signup':
                     self.uiManager = self.signup.getManager()
                     self.setRoute('signup')


    def signupRoute(self, event):
        if self.getRoute() == 'signup':
            if self.signup.getView(event) != self.signup:
                if self.signup.getView(event) == 'home':
                    self.uiManager = self.home.getManager()

                    pseudo = self.signup.getPseudo().get_text()
                    password = self.signup.getPassword().get_text()

                    Auth().register(pseudo, password)

                    self.setRoute('home')
