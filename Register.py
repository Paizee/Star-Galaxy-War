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
from verify_email import verify_email

class Register():
    def __init__(self):
        global collection,db,cluster
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
        cluster = MongoClient("mongodb+srv://Leaderboard1:OCUXEVTl4W8Jy1Dg@mygame.b7uc4ln.mongodb.net/?retryWrites=true&w=majority")
        db = cluster.get_database("Accounts")
        collection= db.get_collection("Users")
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
                AllSettings.nameinput = True
                AllSettings.emailinput = False
                AllSettings.passwordinput = False
                AllSettings.password2input = False                   

        if self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.nameinput = False
                AllSettings.emailinput = True
                AllSettings.passwordinput = False
                AllSettings.password2input = False

        if self.rect3.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.emailinput = False
                AllSettings.nameinput = False
                AllSettings.passwordinput = True
                AllSettings.password2input = False
        if self.rect4.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.emailinput = False
                AllSettings.nameinput = False
                AllSettings.passwordinput = False
                AllSettings.password2input = True
        if self.rect5.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                AllSettings.Emailsubmitcheck = False
                AllSettings.Passwordsubmitcheck = False
                AllSettings.Namesubmitcheck = False   
                AllSettings.reg = True
        if self.rect6.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                AllSettings.Emailsubmitcheck = True
                AllSettings.Passwordsubmitcheck = True
                AllSettings.Namesubmitcheck = True
    def runit():
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
        while not AllSettings.reg:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                if AllSettings.nameinput == True:
                    if event.type == pygame.KEYDOWN:
                        if len(name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                AllSettings.Namesubmitcheck = False
                                name_text = name_text[:-1]
                            else: name_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                AllSettings.nameinput = False
                if AllSettings.emailinput == True:
                    if event.type == pygame.KEYDOWN:
                        if len(name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                AllSettings.Emailsubmitcheck = False
                                email_text = email_text[:-1]
                            else: email_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                AllSettings.emailinput = False
                if AllSettings.passwordinput == True:
                    if event.type == pygame.KEYDOWN:
                        if len(name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                AllSettings.Passwordsubmitcheck = False
                                password_text = password_text[:-1]
                            else: password_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                AllSettings.passwordinput = False
                                
                if AllSettings.password2input == True:
                    if event.type == pygame.KEYDOWN:
                        if len(name_text) < 25:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                AllSettings.Passwordsubmitcheck = False
                                password2_text = password2_text[:-1]
                            else: password2_text += event.unicode
                            if pygame.key.get_pressed()[K_RETURN]:
                                AllSettings.password2input = False
                            
            if AllSettings.Passwordsubmitcheck == True:
                if not password_text == password2_text:
                    passwordfail = "Password must be the same!"
                else: 
                    passwordfail = ""
                    AllSettings.Passwordcheckfinish = True
            
            if AllSettings.Namesubmitcheck == True:
                result = collection.find_one({"Name":name_text})
                if result == None:
                    namefail = ""
                    AllSettings.Namecheckfinish = True
                else:
                    namefail = "Name is already given!" 

            if AllSettings.Emailsubmitcheck == True:
                if verify_email(email_text):
                    emailfail = ""
                    AllSettings.Emailcheckfinish = True
                else: emailfail = "Email is not valid!"
            if AllSettings.Passwordsubmitcheck == False:
                passwordfail = ""
            if AllSettings.Emailsubmitcheck == False:
                emailfail = ""
            if AllSettings.Namesubmitcheck == False:
                namefail = ""

            if AllSettings.Emailcheckfinish == True:
                if AllSettings.Namecheckfinish == True:
                    if AllSettings.Passwordcheckfinish == True:
                        now = pygame.time.get_ticks()
                        if now - last >= cooldown:
                            last = now
                            post = {"Name":name_text,"Email":email_text,"Password":password2_text,"Coins": 0}
                            collection.insert_one(post)
                            if not collection.find_one({"Email":email_text,"Password":password2_text}) == None:
                                AllSettings.Emailcheckfinish = False
                                AllSettings.Passwordcheckfinish = False
                                AllSettings.Namecheckfinish = False
                                AllSettings.LoginName = name_text
                                AllSettings.login = True
                            

                
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
                AllSettings.reg = True
            
            pygame.display.update()
                