
import pygame
from pygame.locals import *
import os
import AllSettings
import level1
import Player
import Settingwindow
from threading import Thread
import Register
import Login
import Database
import Leaderboard

background = pygame.image.load(os.path.join("data/images","background.png")).convert()
Play_ = pygame.image.load(os.path.join("data/images","Play_.png"))
Play_ = pygame.transform.smoothscale(Play_,(350,100))
quit = pygame.image.load(os.path.join("data/images","quit.png"))
quit = pygame.transform.smoothscale(quit,(350,100))
Settingstext = pygame.image.load(os.path.join("data/images","Settings.png"))
Settingstext = pygame.transform.smoothscale(Settingstext,(350,100))
Leaderboard_Label = pygame.image.load(os.path.join("data/images","Leaderboard.png"))
Leaderboard_Label = pygame.transform.smoothscale(Leaderboard_Label,(350,100))


class Menu():
    Play_image: pygame.Surface
    quit_image: pygame.Surface
    Settingstext_image: pygame.Surface
    Leaderboard_image: pygame.Surface
    user_image: pygame.Surface
    loginuserimagepng: pygame.Surface
    registeruserimagepng: pygame.Surface
    logoutimagepng: pygame.Surface
    rect1: pygame.Rect
    rect2: pygame.Rect
    rect3: pygame.Rect
    rect4: pygame.Rect
    rect5: pygame.Rect
    rect6: pygame.Rect
    rect7: pygame.Rect
    rect8: pygame.Rect
    
    last: int
    cooldown: int
    
    isrunning: bool
    Usershow: bool

    player: Player.Player
    
    def __init__(self):
        self.Play_image = Play_
        self.quit_image = quit
        self.Settingstext_image = Settingstext
        self.Leaderboard_image = Leaderboard_Label
        self.user_image = AllSettings.userimagepng
        self.loginuserimagepng = AllSettings.loginuserimagepng
        self.registeruserimagepng = AllSettings.registeruserimagepng
        self.logoutimagepng = AllSettings.logoutimagepng
        self.rect1 = self.Play_image.get_rect()
        self.rect2 = self.quit_image.get_rect()
        self.rect3 = self.Settingstext_image.get_rect()
        self.rect4 = self.Leaderboard_image.get_rect()
        self.rect5 = self.user_image.get_rect()
        self.rect6 = self.loginuserimagepng.get_rect()
        self.rect7 = self.registeruserimagepng.get_rect()
        self.rect8 = self.logoutimagepng.get_rect()
        self.rect1.x = AllSettings.screen_width/2.8
        self.rect1.y = AllSettings.screen_height/5
        self.rect2.x = AllSettings.screen_width/2.8
        self.rect2.y = AllSettings.screen_height/1.4
        self.rect3.x = AllSettings.screen_width/2.8
        self.rect3.y = AllSettings.screen_height/1.85
        self.rect4.x = AllSettings.screen_width/2.8
        self.rect4.y = AllSettings.screen_height/2.7
        self.rect5.x = AllSettings.screen_width/1.31
        self.rect5.y = AllSettings.screen_height/15
        self.rect6.x = AllSettings.screen_width/1.3
        self.rect6.y = AllSettings.screen_height/4.83
        self.rect7.x = AllSettings.screen_width/1.3
        self.rect7.y = AllSettings.screen_height/3.353
        self.rect8.x = AllSettings.screen_width/1.3
        self.rect8.y = AllSettings.screen_height/3.353
        
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
        
        self.isrunning = True
        self.Usershow = False
        
        self.player = Player.Player()

    def drawcoinsunlogged(self):
        try: 
            font_objcoins = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
            font_objnotlogged = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 16)
            textcoin = font_objcoins.render(str(self.player.coins)+"💰", True, AllSettings.Yellow)
            infonotlogged = font_objnotlogged.render("You're not logged in, the coins are not save!",True,(255,0,0))
            AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/1.2,AllSettings.screen_height/1.2))
            AllSettings.DISPLAY.blit(infonotlogged,(AllSettings.screen_width/1.5,AllSettings.screen_height/1.05))
        except: print("error loading coins")
            
    def drawcoinsloggedin(self):
        font_objcoins = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
        textcoin = font_objcoins.render(str(self.player.coins)+"💰", True, AllSettings.Yellow)
        AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/1.2,AllSettings.screen_height/1.2))

    def drawUserunlogged(self):
        AllSettings.DISPLAY.blit(self.loginuserimagepng,(self.rect6.x,self.rect6.y))
        AllSettings.DISPLAY.blit(self.registeruserimagepng,(self.rect7.x,self.rect7.y))

    def drawUserloggedin(self):
        AllSettings.DISPLAY.blit(self.logoutimagepng,(self.rect8.x,self.rect8.y))
        
    def draw(self):
        
        AllSettings.music.play()
        AllSettings.DISPLAY.blit(background, (0, 0))
        AllSettings.DISPLAY.blit(self.Play_image,(self.rect1.x,self.rect1.y))
        AllSettings.DISPLAY.blit(self.quit_image,(self.rect2.x,self.rect2.y))
        AllSettings.DISPLAY.blit(self.Settingstext_image,(self.rect3.x,self.rect3.y))
        AllSettings.DISPLAY.blit(self.Leaderboard_image,(self.rect4.x,self.rect4.y))
        AllSettings.DISPLAY.blit(self.user_image,(self.rect5.x,self.rect5.y))
        pos = pygame.mouse.get_pos()
        
        if not self.rect1.collidepoint(pos):
            if not self.rect2.collidepoint(pos):
                if not self.rect3.collidepoint(pos):
                    if not self.rect4.collidepoint(pos):
                        if not self.rect5.collidepoint(pos):
                            if not self.rect6.collidepoint(pos):
                                if not self.rect7.collidepoint(pos):
                                    if not self.rect8.collidepoint(pos):
                                        pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)

                    
        # start game
        if self.rect1.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                game = level1.game(player=self.player)
                thread_lev1 = Thread(target=game.runit())
                self.isrunning = False
                thread_lev1.start()
                self.isrunning = True
                game.reset()
        # quit        
        if self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                pygame.quit()
        # menu         
        if self.rect3.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                menu = Settingwindow.Menu(player=self.player)
                thread_menu = Thread(target=menu.SettingsMenu())
                thread_menu.start()
                
         #leaderboard       
        if self.rect4.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                leaderboard = Leaderboard.Leaderboard()
                thread_lead = Thread(target=leaderboard.runit())
                thread_lead.start()
                
        if self.rect5.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    self.Usershow = not self.Usershow
                        
        if self.rect7.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    reg = Register.Register(player=self.player)
                    thread_reg = Thread(target=reg.runit())
                    thread_reg.start()
                    self.Usershow = False
                    
        if self.rect6.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    log = Login.Login(player=self.player)
                    thread_log = Thread(target=log.runit())
                    thread_log.start()
                    self.Usershow = False
    
        if self.rect8.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                db = Database.Database()
                db.logout(player=self.player)
                
    def run(self):   
        while self.isrunning:
              
            if self.player.user_id != None: #logged in
                if self.Usershow:
                    self.draw()
                    self.drawUserloggedin()
                    self.drawcoinsloggedin()
                else:
                    self.draw()
                    self.drawcoinsloggedin()
                    
            else:
                if self.Usershow:
                    self.draw()
                    self.drawUserunlogged()
                    self.drawcoinsunlogged()

                else: 
                    self.draw()
                    self.drawcoinsunlogged()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit() 
            
            try: 
                pygame.display.update()
            except: print("error updating screen")
