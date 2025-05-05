import pygame.gfxdraw
import time
import pygame, pygame.mixer
from pygame.locals import *
import os
import random
import AllSettings
import Animations
import Enemy
import level1
import Player
import Settingwindow

class Enemie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global tfx,tfy
        
        self.id = random.randint(0,100)
        self.image = AllSettings.enemieimage
        self.rect = self.image.get_rect()
        tfx = random.randrange(AllSettings.screen_width)
        tfy = random.randrange(round(AllSettings.screen_height/1.5))
        self.rect.x = tfx
        self.rect.y = tfy
        numsx = [2,-2]
        self.speedx = random.choice(numsx)
        numsy = [-1,1]
        self.speedy = random.choice(numsy)
        self.health = 4
    
    def shootback():
        for enemies in AllSettings.enemie_list:
            bulletback = Bulletback(enemies.rect.center)
            AllSettings.all_sprites_list.add(bulletback)
            AllSettings.bulletback_list.add(bulletback)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x > AllSettings.screen_width - 90:
            self.speedx = -2
        if self.rect.x < 0:
            self.speedx = +2
        if self.rect.y > AllSettings.screen_height/5:
            self.speedy = -1
        if self.rect.y < 5:
            self.speedy = +1

    def DrawBar(pos, size, borderC, barC, progress):
        pygame.draw.rect(AllSettings.DISPLAY, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+3, pos[1]+3)
        innerSize = ((size[0]-6) * progress, size[1]-6)
        pygame.draw.rect(AllSettings.DISPLAY, barC, (*innerPos, *innerSize))

    def DrawHealthBar(self): 
        pygame.draw.rect(AllSettings.DISPLAY, AllSettings.Lightgrey, (self.rect.x,self.rect.y, 100, 10),8)
        pygame.draw.rect(AllSettings.DISPLAY, AllSettings.Green, (self.rect.x,self.rect.y, 100 / self.health,10), 8)

class Bulletback(pygame.sprite.Sprite):

    def __init__(self,center):
        super().__init__()

        self.image = AllSettings.bulletred
        self.rect = self.image.get_rect(center=center)
        self.speedy = -5

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.y > AllSettings.screen_height:
            self.kill()