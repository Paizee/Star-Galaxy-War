

import pygame.gfxdraw
import time
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
from enum import Enum

class Window(Enum):
    Sound = "Sound"
    Video = "Video"
    Control = "Control"

class Menu():
    def __init__(self,player: Player.Player):
        super().__init__()
        self.is_running = True
        self.selected_window = Window.Sound,
        self.settings_menu_selected = True
        self.back = False
        self.start_input = False
        self.player = player

    def Menu(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
            pos = pygame.mouse.get_pos()
            if not Menusbutton.rect.collidepoint(pos):
                if not Settingsbutton.rect.collidepoint(pos):
                    if not Continuebutton.rect.collidepoint(pos):
                        pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)

            Menusbutton.draw()
            Settingsbutton.draw()
            Continuebutton.draw()
            pygame.display.update()  
        
    def SettingsMenu(self):
        while (not self.back) and self.settings_menu_selected: 
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                    
            pos = pygame.mouse.get_pos()
            if not SettingsSound.rect.collidepoint(pos):
                if not SettingsVideo.rect.collidepoint(pos):
                    if not SettingsControls.rect.collidepoint(pos):
                        if not SettingsBack.rect.collidepoint(pos):
                            pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
                            
            Settingmenu.draw()
            SettingsSound.draw(menu=self)
            SettingsVideo.draw(menu=self)
            SettingsControls.draw(menu=self)
            SettingsBack.draw(menu=self)
            pygame.display.update()
                
    def Soundmenu(self):
        volume_bars = []
        Settingmenu.draw() 
        for i in range(round(self.player.volume / 10)):
            volume_bars.append(pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(620 + (35 * i),211,20,40),border_radius=10))

        music_bars = []
        for i in range(round(self.player.music_volume / 10)):
            music_bars.append(pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(620 + (35 * i),295,20,40),border_radius=10))
             
        def update_volume():
            AllSettings.shot.set_volume(self.player.volume/100)
            AllSettings.click.set_volume(self.player.volume/100)
            AllSettings.explosound.set_volume(self.player.volume/100)

        def update_music_volume():
            AllSettings.music.set_volume(self.player.music_volume/100)


        def volume_plus(): 
            if self.player.volume < 100:
                self.player.volume += 10
                volume_bars.append(pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(620 + (35 * len(volume_bars) - 1),211,20,40),border_radius=10))
                update_volume()

        volume_plus_button = Volume_Plus(function=volume_plus,x=975,y=211)


        def volume_minus(): 
            if self.player.volume > 0:
                self.player.volume -= 10
                print(self.player.volume)
                AllSettings.DISPLAY.fill(AllSettings.Black,rect=volume_bars[len(volume_bars) - 1])
                volume_bars.remove(volume_bars[len(volume_bars) - 1])
                update_volume()
        
        volume_minus_button = Volume_Minus(function=volume_minus,x=550,y=211)


        def music_volume_plus(): 
            if self.player.music_volume < 100:
                self.player.music_volume += 10
                music_bars.append(pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(620 + (35 * len(music_bars) - 1),295,20,40),border_radius=10))
                update_music_volume()

        music_volume_plus_button = Volume_Plus(function=music_volume_plus,x=975,y=295)
        

        def music_volume_minus(): 
            if self.player.music_volume > 0:
                self.player.music_volume -= 10
                AllSettings.DISPLAY.fill(AllSettings.Black,rect=music_bars[len(music_bars) - 1])
                music_bars.remove(music_bars[len(music_bars) - 1])
                update_music_volume()

        music_volume_minus_button = Volume_Minus(function=music_volume_minus,x=550,y=295)


        volume_icon = Volume()
        music_icon = Music_Volume()
        
        volume_icon.draw()
        music_icon.draw()
        
        old_volume_rect = None
        old_music_volume_rect = None
        
        while (not self.back) and (self.selected_window == Window.Sound):
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()

            pos = pygame.mouse.get_pos()
            if not SettingsSound.rect.collidepoint(pos):
                if not SettingsVideo.rect.collidepoint(pos):
                    if not SettingsControls.rect.collidepoint(pos):
                        if not SettingsBack.rect.collidepoint(pos):
                            if not volume_plus_button.rect.collidepoint(pos):
                                if not volume_minus_button.rect.collidepoint(pos):
                                    if not music_volume_plus_button.rect.collidepoint(pos):
                                        if not music_volume_minus_button.rect.collidepoint(pos):
                                            pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
            
            volume_plus_button.draw() 
            volume_minus_button.draw()
                                        
            music_volume_plus_button.draw()
            music_volume_minus_button.draw()

            SettingsSound.draw(menu=self)
            SettingsVideo.draw(menu=self)
            SettingsControls.draw(menu=self)
            SettingsBack.draw(menu=self)
            
            font = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)

            if (old_volume_rect != None):
                AllSettings.DISPLAY.fill(AllSettings.Black,rect=old_volume_rect)

            volume_text = font.render(str(self.player.volume) + "%" , True, AllSettings.WHITE)
            old_volume_rect = AllSettings.DISPLAY.blit(volume_text,(795,260))
            
            
            if (old_music_volume_rect != None):
                AllSettings.DISPLAY.fill(AllSettings.Black,rect=old_music_volume_rect)
                
            music_volume_text = font.render(str(self.player.music_volume) + "%" , True, AllSettings.WHITE)
            old_music_volume_rect = AllSettings.DISPLAY.blit(music_volume_text,(795,340))
                        
                                    
            pygame.display.update()  

    def VideoSettings(self):
        while (not self.back) and (self.selected_window == Window.Video):
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
            pos = pygame.mouse.get_pos()
            if not SettingsSound.rect.collidepoint(pos):
                if not SettingsVideo.rect.collidepoint(pos):
                    if not SettingsControls.rect.collidepoint(pos):
                        if not SettingsBack.rect.collidepoint(pos):
                            if not Fullcheckbox.rect.collidepoint(pos):
                                if not resolution.rect.collidepoint(pos):
                                    if not dropdownmenu.rect.collidepoint(pos):
                                        if not re1680x1050.rect.collidepoint(pos):
                                            if not re1280x1024.rect.collidepoint(pos):
                                                if not re720x1280.rect.collidepoint(pos):
                                                    if not re640x480.rect.collidepoint(pos):
                                                        pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
            Settingmenu.draw()
            SettingsVideo.draw(menu=self)
            SettingsSound.draw(menu=self)
            SettingsControls.draw(menu=self)
            SettingsBack.draw(menu=self)
            
            Fullcheckbox.draw()
            Fullscreenmodepng.draw()
            resolution.draw()
            dropdownmenu.draw()
            re1920x1080.draw()

            if AllSettings.toggofull == True:
                AllSettings.DISPLAY.blit(AllSettings.xohnekasten,(805,200))
            if AllSettings.toggofull2 == 2: 
                AllSettings.toggofull2 = 0
            if AllSettings.toggofull2 == 0:
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(809,203,40,33))

            if AllSettings.rahmenmenu == True:
                Dropdownrahmen.draw()
                re1680x1050.draw()
                re1280x1024.draw()
                re720x1280.draw()
                re640x480.draw()
            if AllSettings.closerahmen == 2: 
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(775,335,300,202))
                AllSettings.closerahmen = 0
            if AllSettings. screen_height == 1920:
                AllSettings.reso1 = "1680 x 1050"
                AllSettings.reso2 = "1280 x 1024"
                AllSettings.reso3 = "1281 x  720"
                AllSettings.reso4 = "640  x  480 "
            if AllSettings.screen_height == 1680:
                AllSettings.reso1 = "1920 x 1080"
                AllSettings.reso2 = "1280 x 1024"
                AllSettings.reso3 = "1281 x  720"
                AllSettings.reso4 = "640  x  480 "
            if AllSettings.screen_height == 1281:
                AllSettings.reso1 = "1920 x 1080"
                AllSettings.reso2 = "1680 x 1050"
                AllSettings.reso3 = "1281 x  720"
                AllSettings.reso4 = "640  x  480 "
            if AllSettings.screen_height == 1280:
                AllSettings.reso1 = "1920 x 1080"
                AllSettings.reso2 = "1680 x 1050"
                AllSettings.reso3 = "1280 x 1024"
                AllSettings.reso4 = "640  x  480 "
            if AllSettings.screen_height == 640:
                AllSettings.reso1 = "1920 x 1080"
                AllSettings.reso2 = "1680 x 1050"
                AllSettings.reso3 = "1280 x 1024"
                AllSettings.reso4 = "1281 x  720"



            if AllSettings.Apply == True:
                Settingmenu.draw()
                SettingsVideo.draw()
                SettingsBack.draw()
                SettingsSound.draw()
                SettingsControls.draw()
                Fullcheckbox.draw()
                Fullscreenmodepng.draw()
                resolution.draw()
                dropdownmenu.draw()
                re1920x1080.draw()

            if AllSettings.rahmenmenu == True:
                Dropdownrahmen.draw()
                re1680x1050.draw()
                re1280x1024.draw()
                re720x1280.draw()
                re640x480.draw()
            if AllSettings.closerahmen == 2: 
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(775,335,300,202))
                AllSettings.closerahmen = 0
            if AllSettings.screen_height == 1920:
                AllSettings.reso1 = "1680 x 1050"
                AllSettings.reso2 = "1280 x 1024"
                AllSettings.reso3 = "1281 x  720"
                AllSettings.reso4 = "640  x  480 "
            if AllSettings.screen_height == 1680:
                AllSettings.reso1 = "1920 x 1080"
                AllSettings.reso2 = "1280 x 1024"
                AllSettings.reso3 = "1281 x  720"
                AllSettings.reso4 = "640  x  480 "
            if AllSettings.screen_height == 1281:
                AllSettings.reso1 = "1920 x 1080"
                AllSettings.reso2 = "1680 x 1050"
                AllSettings.reso3 = "1281 x  720"
                AllSettings.reso4 = "640  x  480 "
            if AllSettings.screen_height == 1280:
                AllSettings.reso1 = "1920 x 1080"
                AllSettings.reso2 = "1680 x 1050"
                AllSettings.reso3 = "1280 x 1024"
                AllSettings.reso4 = "640  x  480 "
            if AllSettings.screen_height == 640:
                AllSettings.reso1 = "1920 x 1080"
                AllSettings.reso2 = "1680 x 1050"
                AllSettings.reso3 = "1280 x 1024"
                AllSettings.reso4 = "1281 x  720"



            pygame.display.update() 

    def Controlmenu(self):
        controldraw = controlesettings()
        controlkeydraw = keys()
        controlkeyinputdraw = keyinputs()
        
        

        while (not self.back) and (self.selected_window == Window.Control):
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                    
            pos = pygame.mouse.get_pos()
            if not SettingsControls.rect.collidepoint(pos):
                if not SettingsVideo.rect.collidepoint(pos):
                    if not SettingsSound.rect.collidepoint(pos):
                        if not SettingsBack.rect.collidepoint(pos):
                            if not controlkeyinputdraw.rect.collidepoint(pos):
                                pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
                                
            Settingmenu.draw()
            SettingsControls.draw(menu=self)
            SettingsVideo.draw(menu=self)
            SettingsSound.draw(menu=self)
            SettingsBack.draw(menu=self)
            
            controlkeydraw.draw()
            controldraw.draw()
            controlkeyinputdraw.draw(player=self.player)

            
            if (old_textinput_shoot_rect != None):
                AllSettings.DISPLAY.fill(AllSettings.Black,rect=old_textinput_shoot_rect)
            elif (old_textinput_move_right_rect != None):
                AllSettings.DISPLAY.fill(AllSettings.Black,rect=old_textinput_move_right_rect)
            elif (old_textinput_move_left_rect != None):
                AllSettings.DISPLAY.fill(AllSettings.Black,rect=old_textinput_move_left_rect)
            elif (old_textinput_settings_rect != None):
                AllSettings.DISPLAY.fill(AllSettings.Black,rect=old_textinput_settings_rect)

            font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
            
            #shoot key
            textinput_shoot = font.render(pygame.key.name(Player.Player.shoot_key), True, AllSettings.Yellow)
            old_textinput_shoot_rect = AllSettings.DISPLAY.blit(textinput_shoot,(910,170))

            #move right key
            textinput_move_right = font.render(pygame.key.name(Player.Player.move_right_key), True, AllSettings.Yellow)
            old_textinput_move_right_rect = AllSettings.DISPLAY.blit(textinput_move_right,(910,270))

            #move left key
            textinput_move_left = font.render(pygame.key.name(Player.Player.move_left_key), True, AllSettings.Yellow)
            old_textinput_move_left_rect = AllSettings.DISPLAY.blit(textinput_move_left,(910,370))
        
            #shoot key
            textinput_settings = font.render(pygame.key.name(Player.Player.settings_key), True, AllSettings.Yellow)
            old_textinput_settings_rect = AllSettings.DISPLAY.blit(textinput_settings,(910,470))

            pygame.display.update() 

class ButtonMenu():

    def __init__(self):
        self.image = AllSettings.butMenu
        self.rect = self.image.get_rect()
        self.rect.x = AllSettings.screen_width/3
        self.rect.y = AllSettings.screen_height/4.5

    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                #AllSettings.zeit = 10 time left
                AllSettings.kill = True
                AllSettings.level1run = True
                
class ButtonwinMenu():

    def __init__(self):
        self.image = AllSettings.butMenu1
        self.rect = self.image.get_rect()
        self.rect.x = AllSettings.screen_width/3.5
        self.rect.y = AllSettings.screen_height/1.5

    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                #AllSettings.zeit = 10
                AllSettings.kill = True
                AllSettings.level1run = True
            
class ButtonSettings():

    def __init__(self):
        self.image = AllSettings.butsettings
        self.rect = self.image.get_rect()
        self.rect.x = AllSettings.screen_width/3
        self.rect.y = AllSettings.screen_height/2.5

    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                menu =  Menu()
                menu.settings_menu_selected = True
                menu.SettingsMenu()

class ButtonContinue():

    def __init__(self):
        self.image = AllSettings.butContinue
        self.rect = self.image.get_rect()
        self.rect.x = AllSettings.screen_width/3
        self.rect.y = AllSettings.screen_height/1.7

    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                AllSettings.run = True
                AllSettings.kill = False
                thread_timer = Thread(target=level1.rungame.timer)
                thread_timer.start()

class SettingsMenuBackground():
    def __init__(self):
        self.image = AllSettings.Settingsmenu_bg
        self.rect = self.image.get_rect()
        self.rect.x = 140
        self.rect.y = 60
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

class SoundSettings():
    def __init__(self):
        self.image = AllSettings.Sound
        self.rect = self.image.get_rect()
        self.rect.x = 188
        self.rect.y = 134
    def draw(self,menu: Menu):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                menu.selected_window = Window.Sound
                menu.Soundmenu()

class VideoSettings():
    def __init__(self):
        self.image = AllSettings.Video
        self.rect = self.image.get_rect()
        self.rect.x = 517
        self.rect.y = 134
    def draw(self,menu: Menu):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                menu.selected_window = Window.Video
                menu.VideoSettings()

class ControlsSettings():
    def __init__(self):
        self.image = AllSettings.Controls
        self.rect = self.image.get_rect()
        self.rect.x = 823
        self.rect.y = 134
    def draw(self,menu: Menu):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                menu.selected_window = Window.Control
                menu.Controlmenu()

class backSettingsMenu():
    def __init__(self):
        self.image = AllSettings.Back
        self.rect = self.image.get_rect()
        self.rect.x = 967
        self.rect.y = 566 
    def draw(self,menu: Menu):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                menu.back = True      

class Volume():
    def __init__(self):
        self.image = AllSettings.volumepng
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 204
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

class Volume_Plus():
    def __init__(self,function,x,y):
        self.image = AllSettings.plus
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
        self.function = function

    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    self.function()

class Volume_Minus():
    def __init__(self,function,x,y):
        self.image = AllSettings.minus
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cooldown = 300 
        self.last = pygame.time.get_ticks()
        self.function = function

    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    self.function()

class Music_Volume():
    def __init__(self):
        self.image = AllSettings.musicpng
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 295

    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

class Resolution():
    def __init__(self):
        self.image = AllSettings.reso
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 295
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
        
class dropdown():
    def __init__(self):
        self.image = AllSettings.zeile
        self.rect = self.image.get_rect()
        self.rect.x = 775
        self.rect.y = 286
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    AllSettings.rahmenmenu = True
                    AllSettings.closerahmen += 1
class dropdownrahmen():
    def __init__(self):
        self.image = AllSettings.rahmen
        self.rect = self.image.get_rect()
        self.rect.x = 775
        self.rect.y = 335
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x,self.rect.y))
        
class currentResolution():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(str(AllSettings.screen_height) +  " x " + str(AllSettings.screen_width), True, AllSettings.Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 785
        self.rect.y = 282

    def draw(self):
        AllSettings.DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

class r1680x1050():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(AllSettings.reso1, True, AllSettings.Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 785
        self.rect.y = 332
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    AllSettings.screen_height = int(AllSettings.reso1[7:11])
                    AllSettings.screen_width = int(AllSettings.reso1[0:4])
                    AllSettings.Apply = True
        return AllSettings.Apply
class r1280x1024():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(AllSettings.reso2, True, AllSettings.Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 785
        self.rect.y = 372
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    AllSettings.screen_height = int(AllSettings.reso2[7:11])
                    AllSettings.screen_width = int(AllSettings.reso2[0:4])
                    AllSettings.Apply = True
        return AllSettings.Apply
        
class r720x1280():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(AllSettings.reso3, True, AllSettings.Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 805
        self.rect.y = 412
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    AllSettings.screen_height = int(AllSettings.reso3[7:12])
                    AllSettings.screen_width = int(AllSettings.reso3[0:4])
                    AllSettings.Apply = True
        return AllSettings.Apply
class r640x480():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(AllSettings.reso4, True, AllSettings.Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 800
        self.rect.y = 452
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    AllSettings.screen_height = int(AllSettings.reso4[7:12])
                    AllSettings.screen_width = int(AllSettings.reso4[0:4])
                    AllSettings.Apply = True
        return AllSettings.Apply
class Fullscreenmode():
    def __init__(self):
        self.image = AllSettings.Fullscreenpng
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 200
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

class Fullscreencheckbox():
    def __init__(self):
        self.image = AllSettings.xkasten
        self.rect = self.image.get_rect()
        self.rect.x = 805
        self.rect.y = 200
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    AllSettings.toggofull = True
                    AllSettings.toggofull2 += 1
                    pygame.display.toggle_fullscreen()
        return AllSettings.toggofull

class controlesettings():
    def __init__(self):
        self.image = AllSettings.keyspng
        self.rect = self.image.get_rect()       
        self.rect.x = 181
        self.rect.y = 204
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

class keys():
    def __init__(self):
        self.shootimage = AllSettings.shootpng
        self.moverightimage = AllSettings.moverightpng
        self.moveleftimage = AllSettings.moveleftpng
        self.settingspng = AllSettings.settingspng
        self.rect = self.shootimage.get_rect() 
        self.rect1 = self.moverightimage.get_rect() 
        self.rect2 = self.moveleftimage.get_rect()
        self.rect3 = self.settingspng.get_rect()
        self.rect.x = 500
        self.rect.y = 204
        self.rect1.x = 500
        self.rect1.y = 304
        self.rect2.x = 500
        self.rect2.y = 404
        self.rect3.x = 500
        self.rect3.y = 504  
    def draw(self):
        AllSettings.DISPLAY.blit(self.shootimage,(self.rect.x,self.rect.y))
        AllSettings.DISPLAY.blit(self.moverightimage,(self.rect1.x,self.rect1.y))
        AllSettings.DISPLAY.blit(self.moveleftimage,(self.rect2.x,self.rect2.y))
        AllSettings.DISPLAY.blit(self.settingspng,(self.rect3.x,self.rect3.y))

class keyinputs():
    def __init__(self):
        self.keyinput = AllSettings.keyinputpng
        self.keyinput1 = AllSettings.keyinputpng
        self.keyinput2 = AllSettings.keyinputpng
        self.keyinput3 = AllSettings.keyinputpng
        self.rect = self.keyinput.get_rect()
        self.rect1 = self.keyinput1.get_rect()
        self.rect2 = self.keyinput2.get_rect()
        self.rect3 = self.keyinput3.get_rect()
        self.rect.x = 900
        self.rect.y = 184
        self.rect1.x = 900
        self.rect1.y = 284
        self.rect2.x = 900
        self.rect2.y = 384
        self.rect3.x = 900
        self.rect3.y = 484
        self.start_time = time.time()
        self.seconds = int(10)
        
    def draw(self,player: Player.Player):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.keyinput,(self.rect.x,self.rect.y))
        AllSettings.DISPLAY.blit(self.keyinput1,(self.rect1.x,self.rect1.y))
        AllSettings.DISPLAY.blit(self.keyinput2,(self.rect2.x,self.rect2.y))
        AllSettings.DISPLAY.blit(self.keyinput3,(self.rect3.x,self.rect3.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                player.shoot_key = pygame.key.get_pressed().first()
                
        elif self.rect1.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                player.move_right_key = pygame.key.get_pressed().first()

        elif self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                player.move_left_key = pygame.key.get_pressed().first()
                
        elif self.rect3.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                player.settings_key = pygame.key.get_pressed().first()

cooldown0 = 1200
last0 = pygame.time.get_ticks()

Fullcheckbox = Fullscreencheckbox()
Fullscreenmodepng = Fullscreenmode()

SettingsSound = SoundSettings()
SettingsVideo = VideoSettings()
SettingsControls = ControlsSettings()
SettingsBack = backSettingsMenu()

resolution = Resolution()
dropdownmenu = dropdown()
Dropdownrahmen = dropdownrahmen()

re1920x1080 = currentResolution()
re1680x1050 = r1680x1050()
re1280x1024 = r1280x1024()
re720x1280 = r720x1280()
re640x480 = r640x480()

Settingsbutton = ButtonSettings()
Menusbutton = ButtonMenu()
Continuebutton = ButtonContinue()
Settingmenu = SettingsMenuBackground()
