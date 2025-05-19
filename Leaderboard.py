
import pygame
from pygame.locals import *
import os
import AllSettings
import Database

class Leaderboard_Item():
    username: str
    coins: int
    
    def __init__(self,username,coins):
        self.username = username
        self.coins = coins
        
class Leaderboard():
    image: pygame.Surface
    backimage: pygame.Surface
    rect1: pygame.Rect
    rect2: pygame.Rect
    is_running: bool
    leaderboard_items: list[Leaderboard_Item]
    
    def __init__(self):
        self.image = AllSettings.leaderboardpng
        self.backimage = AllSettings.Back
        self.rect1 = self.image.get_rect()
        self.rect1.y = 0
        self.rect1.x = 0
        self.rect2 = self.backimage.get_rect()
        self.rect2.x = 1150
        self.rect2.y = 660
        self.is_running = True
        db = Database.Database()
        
        self.leaderboard_items = db.get_leaderboard()
        self.listed_items = False
 

    def draw(self):
        if not self.listed_items:
            AllSettings.DISPLAY.blit(self.image,(self.rect1.x,self.rect1.y)) 
            AllSettings.DISPLAY.blit(self.backimage,(self.rect2.x,self.rect2.y))
        
        pos = pygame.mouse.get_pos()
        if not self.rect2.collidepoint(pos):
            pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
            
        if self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                self.is_running = False
                
        font_obj = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 32)
        font_objcoins = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.TTF"), 32)
        
        if (self.leaderboard_items != None) and (not self.listed_items):
            for index, item in enumerate(self.leaderboard_items):
                textplacename= font_obj.render(str(item.username),True,AllSettings.Yellow)
                textplacecoins = font_objcoins.render(str(item.coins)+"💰",True,AllSettings.Yellow)
            
                AllSettings.DISPLAY.blit(textplacecoins,(500,150 + (index * 110)))
                AllSettings.DISPLAY.blit(textplacename,(650,150 + (index * 110)))
            pygame.display.update()
            self.listed_items = True
     
        
        
        
    def runit(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
            
            self.draw()
            pygame.display.update()
    
    
