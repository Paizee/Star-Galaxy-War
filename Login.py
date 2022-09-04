import pygame.gfxdraw
import time
import pygame, pygame.mixer
from pygame.locals import *
import os
import sys
import random
import AllSettings
import Animations
import Enemy
import level1
import Settingwindow
from pymongo import cursor
from pymongo import MongoClient

class Login():
    def __init__(self):
        global collection,db,cluster
        self.image = AllSettings.Loginimagepng
        self.backimage = AllSettings.Back
        self.registerinputimage = AllSettings.registerimageinputpng
        self.submitimage = AllSettings.Submitpng
        self.rect = self.image.get_rect()
        self.rect2 = self.registerinputimage.get_rect()
        self.rect3 = self.registerinputimage.get_rect()
        self.rect5 = self.backimage.get_rect()
        self.rect6 = self.submitimage.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.rect2.x = 417
        self.rect2.y = 235
        self.rect3.x = 417
        self.rect3.y = 427
        self.rect5.x = 417
        self.rect5.y = 630
        self.rect6.x = 708
        self.rect6.y = 630
        cluster = MongoClient("DATABASE")
        db = cluster.get_database("DATABASE")
        collection= db.get_collection("DATABASE")
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(0,0))
        AllSettings.DISPLAY.blit(self.registerinputimage,(417,235))
        AllSettings.DISPLAY.blit(self.registerinputimage,(417,427))
        AllSettings.DISPLAY.blit(self.backimage,(417,630))
        AllSettings.DISPLAY.blit(self.submitimage,(770,630))
        if not self.rect2.collidepoint(pos):
            if not self.rect3.collidepoint(pos):
                if not self.rect5.collidepoint(pos):
                    if not self.rect6.collidepoint(pos):
                        pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
                      

        if self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.emailinput = True
                AllSettings.passwordinput = False

        if self.rect3.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.emailinput = False
                AllSettings.passwordinput = True
        if self.rect5.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                AllSettings.Emailsubmitcheck = False
                AllSettings.Passwordsubmitcheck = False
                AllSettings.log = True
        if self.rect6.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                AllSettings.Emailsubmitcheck = True
                AllSettings.Passwordsubmitcheck = True
    def runit():
        drawit = Login()
        email_text = ""
        password_text = ""
        passwordfail = ""
        emailfail = ""
        last = pygame.time.get_ticks()
        cooldown = 600
        while not AllSettings.log:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                if AllSettings.emailinput == True:
                    if event.type == pygame.KEYDOWN:
                        if len(email_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                AllSettings.Emailsubmitcheck = False
                                email_text = email_text[:-1]
                            else: email_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                AllSettings.emailinput = False
                if AllSettings.passwordinput == True:
                    if event.type == pygame.KEYDOWN:
                        if len(password_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                AllSettings.Passwordsubmitcheck = False
                                password_text = password_text[:-1]
                            else: password_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                AllSettings.passwordinput = False
                            
            if AllSettings.Passwordsubmitcheck == True:
                if collection.find_one({"Password":password_text,"Email":email_text}) == None:
                    passwordfail = "Password is incorrect!"
                else: 
                    passwordfail = ""
                    AllSettings.Passwordcheckfinish = True

            if AllSettings.Emailsubmitcheck == True:
                if collection.find_one({"Email":email_text}) == None:
                    emailfail = "Email is incorrect!"
                else: 
                    emailfail = ""
                    AllSettings.Emailcheckfinish = True
            if AllSettings.Passwordsubmitcheck == False:
                passwordfail = ""
            if AllSettings.Emailsubmitcheck == False:
                emailfail = ""

            if AllSettings.Emailcheckfinish == True:
                if AllSettings.Passwordcheckfinish == True:
                    now = pygame.time.get_ticks()
                    if now - last >= cooldown:
                        last = now
                        AllSettings.Emailcheckfinish = False
                        AllSettings.Passwordcheckfinish = False
                        AllSettings.Namecheckfinish = False
                        AllSettings.login = True
                        

                
            drawit.draw()
             
            font_obj = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 32)
            font_obj2 = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 16)
            email_showtext = font_obj.render(email_text, True, AllSettings.Yellow)
            password_showtext = font_obj.render(password_text, True, AllSettings.Yellow)
            passwordfail_showtext = font_obj2.render(passwordfail, True, (255,0,0))
            emailfail_showtext = font_obj2.render(emailfail, True, (255,0,0))
            login_showtext = font_obj2.render("Login sucessfully!",True,(18,164,47))
            AllSettings.DISPLAY.blit(email_showtext,(430,240))
            AllSettings.DISPLAY.blit(password_showtext,(430,432))
            AllSettings.DISPLAY.blit(passwordfail_showtext,(430,482))
            AllSettings.DISPLAY.blit(emailfail_showtext,(430,290))
            if AllSettings.login == True:
                AllSettings.DISPLAY.blit(login_showtext,(580,650))
                AllSettings.log = True
                
        
            
            pygame.display.update()
