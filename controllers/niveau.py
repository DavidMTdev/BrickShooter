import pygame
from pygame.locals import *
import random


class Niveau:

    def __init__(self, game, score):
        self.game = game
        self.score = score
        self.level = 1
        self.reload = 0
        self.maxReload = 100

        # pourcentage d'apparition d'un enemy normal ou surprise
        self.enemy = 95
        self.enemySurprise = 5
        self.probaEnemy = []
        self.assets = ["attack","reload"]

        self.attack = [False,0]

    def generate(self):
        # print(self.reload)
        # print(self.score)
        if self.reload:
            self.reload -= 1
            self.setSurprise()
        else:
            for i in range(0, 11):
                self.generateEnemy(i)
            self.reload = self.maxReload
            print(self.game.player.damage)

    def generateEnemy(self, i):
        proba = 0
        self.setProbaEnemy()
        proba = random.randint(0, 99)

        if self.probaEnemy[proba] == 'enemy':
            self.game.spawnEnemy(self.levelEnemy(), 75 * i, False)
        
        elif self.probaEnemy[proba] == 'enemySurprise':
            probaAsset = random.randint(0, (len(self.assets) - 1))
            self.game.spawnEnemy(1, 75 * i, self.assets[probaAsset])


    def levelEnemy(self):
        proba = random.randint(0, 100)
        if self.getLevel() == 1:
            if proba <= 90:
                enemy = 1
            else:
                enemy = 2
        if self.getLevel() == 2:
            if proba <= 70:
                enemy = 1
            elif proba > 70 and proba <= 90:
                enemy = 2
            else:
                enemy = 3
        if self.getLevel() == 3:
            if proba <= 50:
                enemy = 1
            elif proba > 50 and proba <= 80:
                enemy = 2
            else:
                enemy = 3

        if self.getLevel() == 4:
            if proba <= 30:
                enemy = 1
            elif proba > 30 and proba <= 60:
                enemy = 2
            else:
                enemy = 3

        return enemy

        # print('surprise')

    def setProbaEnemy(self):
        for enemyLevel1 in range(0, self.enemy):
            self.probaEnemy.append("enemy")
        for enemySurprise in range(0, self.enemySurprise):
            self.probaEnemy.append("enemySurprise")

    def setScore(self, score):
        self.score = score

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        if self.score > 15000:
            self.setLevel(4)
        elif self.score > 10000:
            self.setLevel(3)
        elif self.score > 5000:
            self.setLevel(2)

        return self.level

    def setSurprise(self):
        if(self.attack[1] > 0):
            self.attack[1] -= 1
        if self.attack[0] == True and self.attack[1] == 0:
            self.game.player.damage -= 1
            self.attack[0] = False
