import pygame
from pygame.locals import *
import os
import AllSettings
from verify_email import verify_email
import Database
import Player

class Register():
    image: pygame.Surface
    backimage: pygame.Surface
    registerinputimage: pygame.Surface
    submitimage: pygame.Surface
    rect: pygame.Rect
    rect1: pygame.Rect
    rect2: pygame.Rect
    rect3: pygame.Rect
    rect4: pygame.Rect
    rect5: pygame.Rect
    rect6: pygame.Rect
    db = Database.Database()
    nameinput: bool 
    emailinput: bool 
    passwordinput: bool 
    password2input: bool  
    
    is_running: bool
    
    name_text: str
    email_text: str
    password_text: str
    password2_text: str
    passwordfail: str
    emailfail: str
    namefail: str
    last: int
    cooldown: int
    player: Player.Player
    
    def __init__(self,player: Player.Player):
        self.image = AllSettings.registerimagepng
        self.backimage = AllSettings.Back
        self.registerinputimage = AllSettings.registerimageinputpng
        self.submitimage = AllSettings.Submitpng
        self.rect = self.image.get_rect()
        self.rect1 = self.registerinputimage.get_rect() #name
        self.rect2 = self.registerinputimage.get_rect() #email
        self.rect3 = self.registerinputimage.get_rect() #password 1
        self.rect4 = self.registerinputimage.get_rect() #password 2
        self.rect5 = self.backimage.get_rect() #back
        self.rect6 = self.submitimage.get_rect() #submit
        self.rect.x = 0
        self.rect.y = 0
        self.rect1.x = 417
        self.rect1.y = 185
        self.rect2.x = 417
        self.rect2.y = 305
        self.rect3.x = 417
        self.rect3.y = 427
        self.rect4.x = 417
        self.rect4.y = 549
        self.rect5.x = 417
        self.rect5.y = 630
        self.rect6.x = 708
        self.rect6.y = 630
        self.db = Database.Database()
        self.nameinput = False
        self.emailinput = False
        self.passwordinput = False
        self.password2input = False
        self.is_running = True    
        
        self.name_text = ""
        self.email_text = ""
        self.password_text = ""
        self.password2_text = ""
        self.passwordfail = ""
        self.emailfail = ""
        self.namefail = ""
        self.last = pygame.time.get_ticks()
        self.cooldown = 600
        
        self.player = player

    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(0,0))
        AllSettings.DISPLAY.blit(self.registerinputimage,(417,185))
        AllSettings.DISPLAY.blit(self.registerinputimage,(417,305))
        AllSettings.DISPLAY.blit(self.registerinputimage,(417,427))
        AllSettings.DISPLAY.blit(self.registerinputimage,(417,549))
        AllSettings.DISPLAY.blit(self.backimage,(417,630))
        AllSettings.DISPLAY.blit(self.submitimage,(770,630))
        
        if not self.rect1.collidepoint(pos):
            if not self.rect2.collidepoint(pos):
                if not self.rect3.collidepoint(pos):
                    if not self.rect4.collidepoint(pos):
                        if not self.rect5.collidepoint(pos):
                            if not self.rect6.collidepoint(pos):
                                pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
        
        if self.rect1.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                self.nameinput = True
                self.emailinput = False
                self.passwordinput = False
                self.password2input = False                   

        if self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                self.nameinput = False
                self.emailinput = True
                self.passwordinput = False
                self.password2input = False

        if self.rect3.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                self.emailinput = False
                self.nameinput = False
                self.passwordinput = True
                self.password2input = False
                
        if self.rect4.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                self.emailinput = False
                self.nameinput = False
                self.passwordinput = False
                self.password2input = True
        if self.rect5.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()  
                self.is_running = False 
                
        if self.rect6.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    
                    
                if self.db.check_username_given(username=self.name_text):
                    self.namefail = "Name is already given!"
                else:
                    self.namefail = ""

                    if not verify_email(self.email_text):
                        self.emailfail = "Email is not valid!"
                    else:
                        self.emailfail = ""
        
                        if len(self.password_text) < 6:
                            self.passwordfail = "Password must be 6 figures long!"
                            
                        else: 
                            if self.password_text != self.password2_text:
                                self.passwordfail = "Password must be the same!"
                            else: 
                                self.passwordfail = ""
                                                   
                                self.db.create_user(email=self.email_text,password=self.password2_text,username=self.name_text,player=self.player)
                                self.is_running = False

                
    def runit(self):

        while self.is_running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                    
                # username input
                if self.nameinput:
                    if event.type == pygame.KEYDOWN:
                        if len(self.name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                self.name_text = self.name_text[:-1]
                            else: self.name_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                self.nameinput = False
                
                # email input            
                elif self.emailinput:
                    if event.type == pygame.KEYDOWN:
                        if len(self.name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                self.email_text = self.email_text[:-1]
                            else: self.email_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                self.emailinput = False
                    
                # password input                
                elif self.passwordinput:
                    if event.type == pygame.KEYDOWN:
                        if len(self.name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                self.password_text = self.password_text[:-1]
                            else: self.password_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                self.passwordinput = False
                
                # password 2 input                
                elif self.password2input:
                    if event.type == pygame.KEYDOWN:
                        if len(self.name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]: 
                                self.password2_text = self.password2_text[:-1]
                            else: self.password2_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                self.password2input = False
                                   
            self.draw()
             
            font_obj = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 32)
            font_obj2 = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 16)
            
            name_showtext = font_obj.render(self.name_text, True, AllSettings.Yellow)
            email_showtext = font_obj.render(self.email_text, True, AllSettings.Yellow)
            password_showtext = font_obj.render(self.password_text, True, AllSettings.Yellow)
            password2_showtext = font_obj.render(self.password2_text, True, AllSettings.Yellow)
            passwordfail_showtext = font_obj2.render(self.passwordfail, True, (255,0,0))
            emailfail_showtext = font_obj2.render(self.emailfail, True, (255,0,0))
            namefail_showtext = font_obj2.render(self.namefail, True, (255,0,0))
            login_showtext = font_obj2.render("Register sucessfully!",True,(18,164,47))
            
            AllSettings.DISPLAY.blit(name_showtext,(430,190))
            AllSettings.DISPLAY.blit(email_showtext,(430,310))
            AllSettings.DISPLAY.blit(password_showtext,(430,432))
            AllSettings.DISPLAY.blit(password2_showtext,(430,554))
            AllSettings.DISPLAY.blit(passwordfail_showtext,(430,600))
            AllSettings.DISPLAY.blit(emailfail_showtext,(430,360))
            AllSettings.DISPLAY.blit(namefail_showtext,(430,240))
            
            
            pygame.display.update()
                
