
import pygame, pygame.mixer
from pygame.locals import *
import os
import AllSettings
import Animations
import Enemy
import level1
import Player
import Settingwindow


DISPLAY=pygame.display.set_mode((AllSettings.screen_width,AllSettings.screen_height),0,64)
pygame.display.set_caption("Pilot Galaxy War")
pygame.display.set_icon(AllSettings.logoiconpng)

background = pygame.image.load(os.path.join("data/images","background.png")).convert()
Play_ = pygame.image.load(os.path.join("data/images","Play_.png"))
Play_ = pygame.transform.smoothscale(Play_,(350,100))
quit = pygame.image.load(os.path.join("data/images","quit.png"))
quit = pygame.transform.smoothscale(quit,(350,100))
Settingstext = pygame.image.load(os.path.join("data/images","Settings.png"))
Settingstext = pygame.transform.smoothscale(Settingstext,(350,100))
Leaderboard = pygame.image.load(os.path.join("data/images","Leaderboard.png"))
Leaderboard = pygame.transform.smoothscale(Leaderboard,(350,100))


class Menu():
    def __init__(self):
        self.Play_image = Play_
        self.quit_image = quit
        self.Settingstext_image = Settingstext
        self.Leaderboard_image = Leaderboard
        self.rect1 = self.Play_image.get_rect()
        self.rect2 = self.quit_image.get_rect()
        self.rect3 = self.Settingstext_image.get_rect()
        self.rect4 = self.Leaderboard_image.get_rect()
        self.rect1.x = AllSettings.screen_width/2.8
        self.rect1.y = AllSettings.screen_height/5
        self.rect2.x = AllSettings.screen_width/2.8
        self.rect2.y = AllSettings.screen_height/1.4
        self.rect3.x = AllSettings.screen_width/2.8
        self.rect3.y = AllSettings.screen_height/1.85
        self.rect4.x = AllSettings.screen_width/2.8
        self.rect4.y = AllSettings.screen_height/2.7


    def draw(self):
        DISPLAY.blit(background, (0, 0))
        DISPLAY.blit(self.Play_image,(self.rect1.x,self.rect1.y))
        DISPLAY.blit(self.quit_image,(self.rect2.x,self.rect2.y))
        DISPLAY.blit(self.Settingstext_image,(self.rect3.x,self.rect3.y))
        DISPLAY.blit(self.Leaderboard_image,(self.rect4.x,self.rect4.y))

        pos = pygame.mouse.get_pos()
        if self.rect3.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                Settingwindow.Menu.SettingsMenu(self)
        if self.rect2.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                pygame.quit()
        if self.rect1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                level1.rungame.runit()

    def run():
        
        menu = Menu()
        while True:
            print(AllSettings.hjah)
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()       
            menu.draw()


            pygame.display.update()

if AllSettings.start == True:
    pygame.init()
    Menu.run()