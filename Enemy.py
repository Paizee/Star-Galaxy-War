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


class Enemie(pygame.sprite.Sprite):
    id: int
    image: pygame.Surface
    rect: pygame.Rect

    numsx: list[int]
    speedx: int
    numsy = list[int]
    speedy: int

    x_limit_right: int
    x_limit_left: int
    y_limit_down: int
    y_limit_up: int

    health: int
    standard_health: int

    add_sprite = Callable
    add_bullet = Callable

    bullet_cooldown: int
    last_bullet: int

    target: Player.Player 
    def __init__(self, add_sprite, add_bullet,player: Player.Player):
        super().__init__()
        self.id = random.randint(0,100)
        self.image = AllSettings.enemieimage
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(AllSettings.screen_width)
        self.rect.y = random.randrange(round(AllSettings.screen_height/1.5))
        numsx = [1,-1]
        self.speedx = random.choice(numsx)
        numsy = [1,-1]
        self.speedy = random.choice(numsy)
        
        self.x_limit_right = random.randint(100, AllSettings.screen_width - 100)
        self.x_limit_left = 0
        self.y_limit_down = random.randint(50, round(AllSettings.screen_height / 5))
        self.y_limit_up = 5

        self.health = 4
        self.standard_health = 4
        self.add_sprite = add_sprite
        self.add_bullet = add_bullet

        self.bullet_cooldown = 1000
        self.last_bullet = random.randint(0, 1000)

        self.health_bar = Health_Bar(x=self.rect.x,y=self.rect.y,percentage=100)
        add_sprite(self.health_bar)

        self.target = player 
            
    def shootback(self):
        now = pygame.time.get_ticks()
        if now - self.last_bullet >= self.bullet_cooldown:
            bullet = Bullet_Red(center=self.rect.center,target=self.target) # sprite
            self.add_sprite(bullet)
            self.add_bullet(bullet)
            self.last_bullet = now

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x > self.x_limit_right or self.rect.x < self.x_limit_left:
            self.speedx *= -1
            self.x_limit_right = random.randint(100, AllSettings.screen_width - 100)

        if self.rect.y > self.y_limit_down or self.rect.y < self.y_limit_up:
            self.speedy *= -1
            self.y_limit_down = random.randint(50, round(AllSettings.screen_height / 5))
            
    def update(self):
        self.move()
        self.UpdateHealthBar()
        self.shootback()

    def UpdateHealthBar(self): 
        self.health_bar.x = self.rect.x
        self.health_bar.y = self.rect.y
        self.health_bar.percentage = round((self.health / self.standard_health) * 100)

    def kill_healthbar(self):
        self.health_bar.kill()

class Bullet_Red(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect
    speed: int
    target_x: float
    target_y: float
    
    target : Player.Player
    def __init__(self,center,target):
        super().__init__()

        self.image = AllSettings.bulletred
        self.rect = self.image.get_rect(center=center)
        self.speed = 6
        self.target_x = target.rect.centerx
        self.target_y = target.rect.centery

    def update(self):
        self.rect.y += self.speed 

        # Extreme mode bullets fliegen zum Spieler
        
        #dx = self.target_x - self.rect.centerx
        #dy = self.target_y - self.rect.centery
        #distance = max(abs(dx), abs(dy))
        #if distance != 0:
        #    self.rect.x += (dx / distance) * self.speed
        #    self.rect.y += (dy / distance) * self.speed

        if self.rect.y > AllSettings.screen_height:
            self.kill()



        
class Health_Bar(pygame.sprite.Sprite):
    
    image: pygame.Surface
    rect: pygame.Rect

    x: int
    y: int
    percentage: int

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