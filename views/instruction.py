
import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UILabel, UITextBox


class Instruction:
    def __init__(self):

        self.manager = UIManager((800, 600), 'themes/home.json')

        self.title = UILabel(relative_rect=pygame.Rect(400 - 100, 20, 200, 50),
                             text='Instruction',
                             manager=self.manager, object_id='#title')

        self.text = UITextBox(
            relative_rect=pygame.Rect(100, 100, 800 - 200, 600 - 100),
            html_text="<body><b>Touche</b><br>Espace -> Tirer<br>Entrer -> Magasin<br>Echap -> Menu de sauvegarde<br>Flèche droite et gauche -> Se déplacer<br><br><b>Système de Niveau</b><br>Niveau 1 -> 0 à 5000 points<br>Niveau 2 -> 5000 à 10000 points<br>Niveau 3 -> 10000 à 15000 points<br>Niveau 4 -> plus de 15000 points<br><br><b>Système du jeu</b><br>Le Joueur commence avec 3 vies, lorsque un monstre touche le joueur celui-ci perd une vie et le monstre meurt.<br>Un monstre rapporte 100 points et 1 credit lorsque le joueur le tue et retire 50 points lorsque le monstre touche le sol<br>Le Joueur a un pourcentage de chance d'obtenir un bonus lorsqu'il tue un monstre<br><br><b>Les Bonus</b><br>Double attaque -> Double les dégats du missile du joueur<br>3 missiles -> Tire 3 missiles au lieu de 1<br>Double score -> Double le score du joueur<br>Temps d'apparition -> Le temps d'apparition est augmenté de 2s</body>",
            manager=self.manager)

        self.buttonReturn = UIButton(relative_rect=pygame.Rect(20, 20, 200, 50),
                                     text='Retour',
                                     manager=self.manager)

        self.buttonLogout = UIButton(relative_rect=pygame.Rect(800 - 220, 20, 200, 50),
                                     text='Déconnexion',
                                     manager=self.manager, object_id='#button-logout')

    def getManager(self):
        return self.manager

    def getView(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.buttonReturn:
                    return "home"
                elif event.ui_element == self.buttonLogout:
                    return "login"

        return self
