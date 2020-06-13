import pygame
from pygame.locals import *
import random



class Niveau:

    def __init__(self, game, score):
        self.game = game
        self.score = score
        self.level = 1
        self.reload = 100

        # pourcentage d'apparition du niveau de l'ennemy (total doit être égal à 100)
        self.enemyLevel1 = 100
        self.enemyLevel2 = 0
        self.enemyLevel3 = 0

        # pourcentage d'apparition d'un enemy normal ou surprise
        self.enemy = 95
        self.enemySurprise = 5
        self.probaEnemy = []

        
    def generate(self, reload):
        print(reload)
        if reload:
            reload -= 1
            print(-1)
        else:
            for i in range(0, 11):
                self.generateEnemy(i)
            reload = self.reload
            print(reload)
    

    def generateEnemy(self, i):
        proba = 0
        if self.getLevel() == 1:
            self.setProbaEnemy()
            proba = random.randint(0,99)

            if self.probaEnemy[proba] == 'enemy':
                self.game.spawnEnemy(1, 75 * i, False)
                # print('enemy')

            elif self.probaEnemy[proba] == 'enemySurprise':
                self.game.spawnEnemy(1, 75 * i, 'enemySurprise')
                # print('surprise')




    def setProbaEnemy(self):
        for enemyLevel1 in range(0, self.enemy):
            self.probaEnemy.append("enemy")
        for enemySurprise in range(0, self.enemySurprise):
            self.probaEnemy.append("enemySurprise") 


    def setLevel(self, level):
        self.level = level
    
    def getLevel(self):
        return self.level
    
