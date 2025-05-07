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
    def __init__(self, add_sprite, add_bullet):
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

        self.health = 3
        self.standard_health = 4
        self.add_sprite = add_sprite
        self.add_bullet = add_bullet

        self.bullet_cooldown = 1000
        self.last_bullet = random.randint(0, 700)
            
    def shootback(self):
        now = pygame.time.get_ticks()
        if now - self.last_bullet >= self.bullet_cooldown:
            bullet = Bullet_Red(self.rect.center) # sprite
            self.add_sprite(bullet)
            self.add_bullet(bullet)
            self.last_bullet = now

    def move(self):
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

    def update(self):
        self.move()
        self.DrawHealthBar()
        self.shootback()


    def DrawBar(pos, size, borderC, barC, progress):
        pygame.draw.rect(AllSettings.DISPLAY, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+3, pos[1]+3)
        innerSize = ((size[0]-6) * progress, size[1]-6)
        pygame.draw.rect(AllSettings.DISPLAY, barC, (*innerPos, *innerSize))

    def DrawHealthBar(self): 
        pygame.draw.rect(AllSettings.DISPLAY, AllSettings.Lightgrey, (self.rect.x,self.rect.y, 100, 10),8)
        pygame.draw.rect(AllSettings.DISPLAY, AllSettings.Green, (self.rect.x,self.rect.y, (self.health / self.standard_health) * 100, 10), 8)
        pygame.display.update()



class Bullet_Red(pygame.sprite.Sprite):

    def __init__(self,center):
        super().__init__()

        self.image = AllSettings.bulletred
        self.rect = self.image.get_rect(center=center)
        self.speedy = -5

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.y > AllSettings.screen_height:
            self.kill()