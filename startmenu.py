
import pygame, pygame.mixer
from pygame.locals import *
import os
import AllSettings
import Animations
import Enemy
import level1
import Player
import Settingwindow
from threading import Thread

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
        
        self.player = Player.Player(add_bullet=None,add_sprite=None,stop_game=None)

    def drawcoinsunlogged(self):
        textcoin = AllSettings.font_objcoins.render(str(self.player.coins)+"💰", True, AllSettings.Yellow)
        infonotlogged = AllSettings.font_objnotlogged.render("You're not logged in, the coins are not save!",True,(255,0,0))
        AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/1.2,AllSettings.screen_height/1.2))
        AllSettings.DISPLAY.blit(infonotlogged,(AllSettings.screen_width/1.5,AllSettings.screen_height/1.05))
        
    def drawcoinsloggedin(self):
        textcoin = AllSettings.font_objcoins.render(str(self.player.coins)+"💰", True, AllSettings.Yellow)
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

                
        
        if self.rect1.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                game = level1.game()
                thread_lev1 = Thread(target=game.runit())
                thread_lev1.start()
                
        if self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                pygame.quit()
                
        if self.rect3.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                menu = Settingwindow.Menu(player=self.player)
                thread_menu = Thread(target=menu.SettingsMenu())
                thread_menu.start()
                
        if self.rect4.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                import Leaderboard
                thread_lead = Thread(target=Leaderboard.Leaderboard.runit(self))
                AllSettings.Leader = False
                thread_lead.start()
                
        if self.rect5.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    AllSettings.Usershow = True
                    AllSettings.Userclicked +=1
                    if AllSettings.Userclicked > 1:
                        AllSettings.Usershow = False
                        AllSettings.Userclicked = 0
                        
        if self.rect7.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    import Register
                    AllSettings.Emailsubmitcheck = False
                    AllSettings.Passwordsubmitcheck = False
                    AllSettings.Namesubmitcheck = False
                    thread_reg = Thread(target=Register.Register.runit())
                    AllSettings.reg = False
                    thread_reg.start()
                    
        if self.rect6.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    import Login
                    AllSettings.Emailsubmitcheck = False
                    AllSettings.Passwordsubmitcheck = False
                    AllSettings.Namesubmitcheck = False
                    thread_log = Thread(target=Login.Login.runit())
                    AllSettings.log = False
                    thread_log.start()
    
        if self.rect8.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                AllSettings.login = False
                
    def run(self):   
        menu = Menu()
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit() 
                    
            if AllSettings.login == True:

                if AllSettings.Usershow == True:
                    menu.draw()
                    menu.drawUserloggedin()
                    menu.drawcoinsloggedin()
                else:
                    menu.draw()
                    menu.drawcoinsloggedin()
            if AllSettings.login == False:
                if AllSettings.Usershow == True:
                    menu.draw()
                    menu.drawUserunlogged()
                    menu.drawcoinsunlogged()

                else: 
                    menu.draw()
                    menu.drawcoinsunlogged()
     
            pygame.display.update()
