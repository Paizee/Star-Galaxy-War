
import pygame
from pygame.locals import *
import os
import AllSettings

class Leaderboard():
    image: pygame.Surface
    backimage: pygame.Surface
    rect1: pygame.Rect
    rect2: pygame.Rect
    def __init__(self):
        self.image = AllSettings.leaderboardpng
        self.backimage = AllSettings.Back
        self.rect1 = self.image.get_rect()
        self.rect1.y = 0
        self.rect1.x = 0
        self.rect2 = self.backimage.get_rect()
        self.rect2.x = 1150
        self.rect2.y = 660

    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect1.x,self.rect1.y)) 
        AllSettings.DISPLAY.blit(self.backimage,(self.rect2.x,self.rect2.y))
        if not self.rect2.collidepoint(pos):
            pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
        if self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                AllSettings.Leader = True
        font_obj = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 32)
        font_objcoins = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.TTF"), 32)
        #
        textplace1name= font_obj.render(str("place1name"),True,AllSettings.Yellow)
        textplace1coins = font_objcoins.render(str(0)+"💰",True,AllSettings.Yellow)
        #
        textplace2name= font_obj.render(str("place2name"),True,AllSettings.Yellow)
        textplace2coins = font_objcoins.render(str(0)+"💰",True,AllSettings.Yellow)
        #
        textplace3name= font_obj.render(str("place3name"),True,AllSettings.Yellow)
        textplace3coins = font_objcoins.render(str(0)+"💰",True,AllSettings.Yellow)
        #
        textplace4name= font_obj.render(str("place4name"),True,AllSettings.Yellow)
        textplace4coins = font_objcoins.render(str(0)+"💰",True,AllSettings.Yellow)
        #
        textplace5name= font_obj.render(str("place5name"),True,AllSettings.Yellow)
        textplace5coins = font_objcoins.render(str(0)+"💰",True,AllSettings.Yellow)
        
        AllSettings.DISPLAY.blit(textplace1coins,(500,152))
        AllSettings.DISPLAY.blit(textplace1name,(650,152))
        #
        AllSettings.DISPLAY.blit(textplace2coins,(500,261))
        AllSettings.DISPLAY.blit(textplace2name,(650,261))
        #
        AllSettings.DISPLAY.blit(textplace3coins,(500,370))
        AllSettings.DISPLAY.blit(textplace3name,(650,370))
        #
        AllSettings.DISPLAY.blit(textplace4coins,(500,480))
        AllSettings.DISPLAY.blit(textplace4name,(650,480))
        #
        AllSettings.DISPLAY.blit(textplace5coins,(500,600))
        AllSettings.DISPLAY.blit(textplace5name,(650,600))
    def runit(self):
        leaddraw = Leaderboard()
        while not AllSettings.Leader:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
            
            leaddraw.draw()
            pygame.display.update()
    
    

