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
    def __init__(self,add_bullet,add_sprite,stop_game):
        super().__init__()

        self.image = AllSettings.playerimage
        self.rect = self.image.get_rect()
        self.rect.y = AllSettings.screen_height - 150
        self.speedx = 0
        self.rect.x = AllSettings.screen_width/2
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
        self.add_bullet = add_bullet
        self.add_sprite = add_sprite
        self.stop_game = stop_game
        self.health = 15
        self.standart_health = 15

    def update(self):
        self.movement()

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[K_a]: # a key => move left
            self.rect.x  -=7
        elif keys[K_d]: # d key => move right
            self.rect.x  +=7
        if keys[K_SPACE]: # spacebar => shoot if cooldown allows
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown:
                self.last = now
                Player.shoot(self)
                AllSettings.shot.play()
        if keys[K_ESCAPE]: # escape => stop game and show menu
            AllSettings.run = False
            self.stop_game()
            menu = Settingwindow.Menu()
            menu.Menu()
            
        #move player finally
        if self.rect.x > AllSettings.screen_width - 125:
            self.rect.x = AllSettings.screen_width - 125
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet_Laser(start_x=self.rect.x, start_y=self.rect.y)
        self.add_sprite(bullet)
        self.add_bullet(bullet)
    
    def DrawHealthBar(self):
        pygame.draw.rect(AllSettings.DISPLAY, (AllSettings.Lightgrey), (AllSettings.screen_width/15, AllSettings.screen_height/1.15, 100, 15), 1)
        pygame.draw.rect(AllSettings.DISPLAY, (AllSettings.Green), (AllSettings.screen_width/15, AllSettings.screen_height/1.15, (self.health / self.standart_health) * 100  ,12.5))
        pygame.display.update()


class Bullet_Laser(pygame.sprite.Sprite):

    def __init__(self,start_x,start_y):
        super().__init__()
        self.image = AllSettings.laserbullet
        self.rect = self.image.get_rect()
        self.speedy = 10
        self.rect.x = start_x + 40
        self.rect.y = start_y - 25

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.top < 5:
            self.kill()