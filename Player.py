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


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global PlayerHealth

        self.image = AllSettings.playerimage
        self.rect = self.image.get_rect()
        self.rect.y = AllSettings.screen_height - 150
        self.speedx = 0
        self.rect.x = AllSettings.screen_width/2
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
        PlayerHealth = 15

    def update(self):
        global playerx,playery
        keys = pygame.key.get_pressed()
        if keys[AllSettings.keywaspressed1]:
            self.rect.x  -=7
        elif keys[AllSettings.keywaspressed2]:
            self.rect.x  +=7
        if keys[AllSettings.keywaspressed]:
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown:
                self.last = now
                Player.shoot(self)
                AllSettings.shot.play()
        if keys[AllSettings.keywaspressed3]:
            AllSettings.run = False
            AllSettings.kill = True
            Settingwindow.Menu.Menu(self)

            
        
        playerx = self.rect.x
        playery = self.rect.y
        if self.rect.x > AllSettings.screen_width - 125:
            self.rect.x = AllSettings.screen_width - 125
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet()
        AllSettings.all_sprites_list.add(bullet)
        AllSettings.bullet_list.add(bullet)
    
    def DrawBar(pos2, size2, borderC2, barC2, progress2):
        pygame.draw.rect(AllSettings.DISPLAY, borderC2, (*pos2, *size2), 1)
        innerPos  = (pos2[0]+3, pos2[1]+3)
        innerSize = ((size2[0]-6) * progress2, size2[1]-6)
        pygame.draw.rect(AllSettings.DISPLAY, barC2, (*innerPos, *innerSize))

class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = AllSettings.laserbullet
        self.rect = self.image.get_rect()
        self.speedy = 5
        self.rect.x = playerx + 40
        self.rect.y = playery - 25

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.top < 5:
            self.kill()