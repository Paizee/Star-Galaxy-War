
import pygame, pygame.mixer
from pygame.locals import *
import os
import AllSettings


class Play():
    
    def __init__(self):
        self.height = 25
        self.gravity = 1
        self.speed = 1
        self.Playimage = AllSettings.Playtostart
        self.shipimage = AllSettings.shiptostart
        self.tiefighter = AllSettings.enemieimage
        self.rect1 = self.Playimage.get_rect()
        self.rect2 = self.shipimage.get_rect()
        self.rect3 = self.tiefighter.get_rect()
        self.rect1.x = 480
        self.rect1.y = -50
        self.rect2.x = 2000
        self.rect2.y = 450
        self.rect3.x = 50
        self.rect3.y = 450
        self.speedy = 5

        self.ship = False


    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(AllSettings.Playtostart,(self.rect1.x,self.rect1.y))

        

        self.rect1.y += self.gravity 
        if self.rect1.y == 340:
            self.gravity = 0
            if self.rect1.collidepoint(pos):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
                if pygame.mouse.get_pressed()[0] == 1:
                    AllSettings.click.play()
                    self.gravity = -1.25
                    self.ship = True
        if self.ship == True:
            AllSettings.DISPLAY.blit(AllSettings.shiptostart,(self.rect2.x,self.rect2.y))
            AllSettings.DISPLAY.blit(AllSettings.enemieimage,(self.rect2.x - 350,self.rect2.y))
            if self.rect1.y < -100:
                self.gravity = 0
                self.rect2.x -= self.speed *2
            if self.rect2.x < -500:
                import startmenu
                menu = startmenu.Menu()
                menu.run()
            




        
play = Play()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    AllSettings.DISPLAY.blit(AllSettings.background,(0,0))
    play.draw()
    pygame.display.update()