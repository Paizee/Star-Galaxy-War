import pygame
from pygame.locals import *
import os
import AllSettings
import Database
import Player

class Login():
    login_label: pygame.Surface
    backimage: pygame.Surface
    registerinputimage: pygame.Surface
    submitimage: pygame.Surface
    rect: pygame.Rect
    rect2: pygame.Rect
    rect3: pygame.Rect
    rect4: pygame.Rect
    rect5: pygame.Rect
    emailinput: bool
    passwordinput: bool
    Emailsubmitcheck: bool
    Passwordsubmitcheck: bool
    
    is_running: bool
    login : bool
    
    email_text: str
    password_text: str
    passwordfail: str
    emailfail: str
    last: int
    cooldown: int
    player: Player.Player
    
    def __init__(self,player: Player.Player):
        self.login_label = AllSettings.Loginimagepng
        self.backimage = AllSettings.Back
        self.registerinputimage = AllSettings.registerimageinputpng
        self.submitimage = AllSettings.Submitpng
        self.rect = self.login_label.get_rect() # login label
        self.rect2 = self.registerinputimage.get_rect() # email rect2
        self.rect3 = self.registerinputimage.get_rect() # password rect3
        self.rect4 = self.backimage.get_rect() # back rect4
        self.rect5 = self.submitimage.get_rect() # submit rect5
        self.rect.x = 0
        self.rect.y = 0
        self.rect2.x = 417
        self.rect2.y = 235
        self.rect3.x = 417
        self.rect3.y = 427
        self.rect4.x = 417
        self.rect4.y = 630
        self.rect5.x = 708
        self.rect5.y = 630
        self.db = Database.Database()
        
        self.emailinput = False
        self.passwordinput = False
        self.Emailsubmitcheck = False
        self.Passwordsubmitcheck = False
        
        self.is_running = True
        self.login = False
        
        self.email_text = ""
        self.password_text = ""
        self.passwordfail = ""
        self.emailfail = ""
        self.last = pygame.time.get_ticks()
        self.cooldown = 600
        
        self.player = player
        

    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.login_label,(0,0))
        AllSettings.DISPLAY.blit(self.registerinputimage,(417,235))
        AllSettings.DISPLAY.blit(self.registerinputimage,(417,427))
        AllSettings.DISPLAY.blit(self.backimage,(417,630))
        AllSettings.DISPLAY.blit(self.submitimage,(770,630))
        
        if not self.rect2.collidepoint(pos):
            if not self.rect3.collidepoint(pos):
                if not self.rect4.collidepoint(pos):
                    if not self.rect5.collidepoint(pos):
                        pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)

        # email input
        if self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                self.emailinput = True
                self.passwordinput = False
                
        # password input
        if self.rect3.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                self.emailinput = False
                self.passwordinput = True
                
        if self.rect4.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                self.is_running = False

        if self.rect5.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                
                    if not self.db.check_email_given(email= self.email_text):
                        self.emailfail = "Email is incorrect!"
                    else: 
                        self.emailfail = ""
                                                
                        if not self.db.check_password_correct(password= self.password_text,email= self.email_text):
                            self.passwordfail = "Password is incorrect!"
                        else: 
                            self.emailfail = ""
                            
                            self.db.login_user(email=self.email_text,password=self.password_text,player=self.player)
                            self.login = True
                                    
                                    


                    
                        


    def runit(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                    
                #email input    
                if self.emailinput == True:
                    if event.type == pygame.KEYDOWN:
                        if len(self.email_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                self.Emailsubmitcheck = False
                                self.email_text = self.email_text[:-1]
                            else: self.email_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                self.emailinput = False
                #password input
                if self.passwordinput == True:
                    if event.type == pygame.KEYDOWN:
                        if len(self.password_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                self.Passwordsubmitcheck = False
                                self.password_text = self.password_text[:-1]
                            else: self.password_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                self.passwordinput = False
                            
                        

                
            self.draw()
             
            font_obj = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 32)
            font_obj2 = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 16)
            
            email_showtext = font_obj.render(self.email_text, True, AllSettings.Yellow)
            password_showtext = font_obj.render(self.password_text, True, AllSettings.Yellow)
            passwordfail_showtext = font_obj2.render(self.passwordfail, True, (255,0,0))
            emailfail_showtext = font_obj2.render(self.emailfail, True, (255,0,0))
            login_showtext = font_obj2.render("Login sucessfully!",True,(18,164,47))
            
            AllSettings.DISPLAY.blit(email_showtext,(430,240))
            AllSettings.DISPLAY.blit(password_showtext,(430,432))
            AllSettings.DISPLAY.blit(passwordfail_showtext,(430,482))
            AllSettings.DISPLAY.blit(emailfail_showtext,(430,290))
            
            if self.login:
                AllSettings.DISPLAY.blit(login_showtext,(580,650))
                self.is_running = False
                
        
            
            pygame.display.update()
