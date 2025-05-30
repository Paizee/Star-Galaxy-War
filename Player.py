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
from typing import Callable


class Player(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect
    speedx: int
    last: int
    cooldown: int
    add_bullet: Callable
    add_sprite: Callable
    stop_game: Callable
    resume_game: Callable
    health: int
    standart_health: int
    coins: int
    name:str
    #keys
    move_left_key:int
    move_right_key:int
    shoot_key:int
    settings_key:int
    #sound
    volume: int
    music_volume: int
    #video
    fullscreen: bool
    def __init__(self):
        super().__init__()

        self.image = AllSettings.playerimage
        self.rect = self.image.get_rect()
        self.rect.y = AllSettings.screen_height - 150
        self.speedx = 0
        self.rect.x = AllSettings.screen_width/2
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
        self.add_bullet = None
        self.add_sprite = None
        self.stop_game = None
        self.resume_game = None
        self.health = 15
        self.standart_health = 15
        self.coins = 0
        self.name = "Player"
        #keys
        self.move_left_key = K_a
        self.move_right_key = K_d
        self.shoot_key = K_SPACE
        self.settings_key = K_ESCAPE
        #sound
        self.volume = 100
        self.music_volume = 100
        #video
        self.fullscreen = False
        #db
        self.user_id = None
    
    def add_coins(self,amount):
        self.coins += amount
    
    
    def update(self):
        self.movement()

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[self.move_left_key]: # a key => move left
            self.rect.x  -=7
        elif keys[self.move_right_key]: # d key => move right
            self.rect.x  +=7
        if keys[self.shoot_key]: # spacebar => shoot if cooldown allows
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown:
                self.last = now
                Player.shoot(self)
                AllSettings.shot.play()
        if keys[self.settings_key]: # escape => stop game and show menu
            self.stop_game()
            menu = Settingwindow.Menu(player=self)
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
        pygame.draw.rect(AllSettings.DISPLAY, (AllSettings.Green), (AllSettings.screen_width/14.78, AllSettings.screen_height/1.1478, (self.health / self.standart_health) * 100  ,13))
        pygame.display.update()


class Bullet_Laser(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect
    speedy: int

    def __init__(self,start_x,start_y):
        super().__init__()
        self.image = AllSettings.laserbullet
        self.rect = self.image.get_rect()
        self.speedy = 6
        self.rect.x = start_x + 40
        self.rect.y = start_y - 25

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.top < 5:
            self.kill()