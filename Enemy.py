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

        self.health = 4
        self.standard_health = 4
        self.add_sprite = add_sprite
        self.add_bullet = add_bullet

        self.bullet_cooldown = 1000
        self.last_bullet = random.randint(0, 1000)

        self.health_bar = Health_Bar(x=self.rect.x,y=self.rect.y,percentage=100)
        add_sprite(self.health_bar)
            
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
        
        if self.rect.x > random.randint(0,round(AllSettings.screen_width - 90)):
            self.speedx = -2
        if self.rect.x < 0:
            self.speedx = +2
        if self.rect.y > random.randint(0,round(AllSettings.screen_height/5)):
            self.speedy = -1
        if self.rect.y < 5:
            self.speedy = +1

    def update(self):
        self.move()
        self.UpdateHealthBar()
        self.shootback()

    def UpdateHealthBar(self): 
        self.health_bar.x = self.rect.x
        self.health_bar.y = self.rect.y
        self.health_bar.percentage = (self.health / self.standard_health) * 100



class Bullet_Red(pygame.sprite.Sprite):

    def __init__(self,center):
        super().__init__()

        self.image = AllSettings.bulletred
        self.rect = self.image.get_rect(center=center)
        self.speedy = 6

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > AllSettings.screen_height:
            self.kill()


        
class Health_Bar(pygame.sprite.Sprite):

    def __init__(self,x,y,percentage):
        super().__init__()

        self.image = pygame.Surface([100, 8])
        self.image.fill(AllSettings.Green)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.percentage = percentage

    def update(self):
        self.image = pygame.Surface([100 * (self.percentage / 100), 8])
        self.image.fill(AllSettings.Green)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y