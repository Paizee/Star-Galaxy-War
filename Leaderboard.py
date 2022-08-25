from this import d
from tkinter.tix import DisplayStyle
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

class Leaderboard():
    def __init__(self):
        self.image = AllSettings.leaderboardpng
        self.rect1 = self.image.get_rect()
        self.rect1.y = AllSettings.screen_height/2
        self.rect1.x = AllSettings.screen_width/2
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect1.x,self.rect1.y))
 
    def runit():
        leaddraw = Leaderboard()
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
            print("dsaf")
            AllSettings.DISPLAY.blit(AllSettings.background,(0,0))
            leaddraw.draw() 
    
    

