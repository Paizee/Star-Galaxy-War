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

class Explosion(pygame.sprite.Sprite):

    def __init__(self,center):
        super().__init__()
        self.image = AllSettings.explosion
        self.rect = self.image.get_rect(center=center)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100


    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            AllSettings.explosound.play()
            self.last_update = now
            self.frame += 1
        if self.frame == 2:
            self.kill()
        else:
            self.image = AllSettings.explosion
            self.rect = self.image.get_rect(center=self.rect.center)
