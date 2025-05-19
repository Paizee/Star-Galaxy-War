import pygame
from pygame.locals import *
import os
import AllSettings
from verify_email import verify_email
import Database

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
    Emailsubmitcheck: bool 
    Passwordsubmitcheck: bool 
    Namesubmitcheck: bool 
    reg: bool   
    
    def __init__(self):
        self.image = AllSettings.registerimagepng
        self.backimage = AllSettings.Back
        self.registerinputimage = AllSettings.registerimageinputpng
        self.submitimage = AllSettings.Submitpng
        self.rect = self.image.get_rect()
        self.rect1 = self.registerinputimage.get_rect()
        self.rect2 = self.registerinputimage.get_rect()
        self.rect3 = self.registerinputimage.get_rect()
        self.rect4 = self.registerinputimage.get_rect()
        self.rect5 = self.backimage.get_rect()
        self.rect6 = self.submitimage.get_rect()
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
        self.Emailsubmitcheck = False
        self.Passwordsubmitcheck = False
        self.Namesubmitcheck = False   
        self.reg = False    

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
                self.Emailsubmitcheck = False
                self.Passwordsubmitcheck = False
                self.Namesubmitcheck = False   
                self.reg = True
        if self.rect6.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                self.Emailsubmitcheck = True
                self.Passwordsubmitcheck = True
                self.Namesubmitcheck = True
    def runit(self):
        drawit = Register()
        name_text = ""
        email_text = ""
        password_text = ""
        password2_text = ""
        passwordfail = ""
        emailfail = ""
        namefail = ""
        last = pygame.time.get_ticks()
        cooldown = 600
        while not self.reg:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                if self.nameinput == True:
                    if event.type == pygame.KEYDOWN:
                        if len(name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                self.Namesubmitcheck = False
                                name_text = name_text[:-1]
                            else: name_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                self.nameinput = False
                if self.emailinput == True:
                    if event.type == pygame.KEYDOWN:
                        if len(name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                self.Emailsubmitcheck = False
                                email_text = email_text[:-1]
                            else: email_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                self.emailinput = False
                if self.passwordinput == True:
                    if event.type == pygame.KEYDOWN:
                        if len(name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                self.Passwordsubmitcheck = False
                                password_text = password_text[:-1]
                            else: password_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                self.passwordinput = False
                                
                if self.password2input == True:
                    if event.type == pygame.KEYDOWN:
                        if len(name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                self.Passwordsubmitcheck = False
                                password2_text = password2_text[:-1]
                            else: password2_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                self.password2input = False
                            
            if self.Passwordsubmitcheck == True:
                if not password_text == password2_text:
                    passwordfail = "Password must be the same!"
                else: 
                    passwordfail = ""
                    AllSettings.Passwordcheckfinish = True
            
            if self.Namesubmitcheck == True:
                if self.db.check_username_given(username=name_text):
                    namefail = ""
                    AllSettings.Namecheckfinish = True
                else:
                    namefail = "Name is already given!" 

            if self.Emailsubmitcheck == True:
                if verify_email(email_text):
                    emailfail = ""
                    AllSettings.Emailcheckfinish = True
                else: emailfail = "Email is not valid!"
            if self.Passwordsubmitcheck == False:
                passwordfail = ""
            if self.Emailsubmitcheck == False:
                emailfail = ""
            if self.Namesubmitcheck == False:
                namefail = ""

            if AllSettings.Emailcheckfinish == True:
                if AllSettings.Namecheckfinish == True:
                    if AllSettings.Passwordcheckfinish == True:
                        now = pygame.time.get_ticks()
                        if now - last >= cooldown:
                            last = now
                            self.db.create_user(email=email_text,password=password2_text,username=name_text)
                            
                            

                
            drawit.draw()
             
            font_obj = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 32)
            font_obj2 = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 16)
            name_showtext = font_obj.render(name_text, True, AllSettings.Yellow)
            email_showtext = font_obj.render(email_text, True, AllSettings.Yellow)
            password_showtext = font_obj.render(password_text, True, AllSettings.Yellow)
            password2_showtext = font_obj.render(password2_text, True, AllSettings.Yellow)
            passwordfail_showtext = font_obj2.render(passwordfail, True, (255,0,0))
            emailfail_showtext = font_obj2.render(emailfail, True, (255,0,0))
            namefail_showtext = font_obj2.render(namefail, True, (255,0,0))
            login_showtext = font_obj2.render("Register sucessfully!",True,(18,164,47))
            AllSettings.DISPLAY.blit(name_showtext,(430,190))
            AllSettings.DISPLAY.blit(email_showtext,(430,310))
            AllSettings.DISPLAY.blit(password_showtext,(430,432))
            AllSettings.DISPLAY.blit(password2_showtext,(430,554))
            AllSettings.DISPLAY.blit(passwordfail_showtext,(430,600))
            AllSettings.DISPLAY.blit(emailfail_showtext,(430,360))
            AllSettings.DISPLAY.blit(namefail_showtext,(430,240))
            if AllSettings.login == True:
                AllSettings.DISPLAY.blit(login_showtext,(580,650))
                self.reg = True
            
            pygame.display.update()
                
