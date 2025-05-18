

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
        self.player = player
        #video
        self.res_frame_open = False

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
            if not SettingsSound_Label.rect.collidepoint(pos):
                if not SettingsVideo_Label.rect.collidepoint(pos):
                    if not SettingsControls_Label.rect.collidepoint(pos):
                        if not SettingsBack_Button.rect.collidepoint(pos):
                            pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
                            
            Settingmenu.draw()
            SettingsSound_Label.draw(menu=self)
            SettingsVideo_Label.draw(menu=self)
            SettingsControls_Label.draw(menu=self)
            SettingsBack_Button.draw(menu=self)
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


        volume_label = Volume_Label()
        music_label = Music_Label()
        
        volume_label.draw()
        music_label.draw()
        
        old_volume_rect = None
        old_music_volume_rect = None
        
        while (not self.back) and (self.selected_window == Window.Sound):
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()

            pos = pygame.mouse.get_pos()
            if not SettingsSound_Label.rect.collidepoint(pos):
                if not SettingsVideo_Label.rect.collidepoint(pos):
                    if not SettingsControls_Label.rect.collidepoint(pos):
                        if not SettingsBack_Button.rect.collidepoint(pos):
                            if not volume_plus_button.rect.collidepoint(pos):
                                if not volume_minus_button.rect.collidepoint(pos):
                                    if not music_volume_plus_button.rect.collidepoint(pos):
                                        if not music_volume_minus_button.rect.collidepoint(pos):
                                            pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
            
            volume_plus_button.draw() 
            volume_minus_button.draw()
                                        
            music_volume_plus_button.draw()
            music_volume_minus_button.draw()

            SettingsSound_Label.draw(menu=self)
            SettingsVideo_Label.draw(menu=self)
            SettingsControls_Label.draw(menu=self)
            SettingsBack_Button.draw(menu=self)
            
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
        Fullcheckbox = Fullscreencheckbox()
        Fullscreen_label = Fullscreen_Label()
        
        resolution_label = Resolution_Label()
        dropdownmenu = Dropdown_Menu()
        dropdown_frame = Dropdown_Frame()

        current_res = currentResolution_Label()
        re1920x1080= res_dropdown_button(x=785,y=332,width=1920,height=1080)
        re1680x1050 = res_dropdown_button(x=785,y=372,width=1680,height=1050)
        re1280x1024 = res_dropdown_button(x=805,y=412,width=1280,height=1024)
        re1280x720 = res_dropdown_button(x=800,y=452,width=1280,height=720)
        
        old_fullscreen_rect = None
        old_res_frame_rect = None
    
        def toggle_res_frame():
            self.res_frame_open = not self.res_frame_open
            current_res = currentResolution_Label()
            
        while (not self.back) and (self.selected_window == Window.Video):
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
            pos = pygame.mouse.get_pos()
            if not SettingsSound_Label.rect.collidepoint(pos):
                if not SettingsVideo_Label.rect.collidepoint(pos):
                    if not SettingsControls_Label.rect.collidepoint(pos):
                        if not SettingsBack_Button.rect.collidepoint(pos):
                            if not Fullcheckbox.rect.collidepoint(pos):
                                if not resolution_label.rect.collidepoint(pos):
                                    if not dropdownmenu.rect.collidepoint(pos):
                                        if not re1680x1050.rect.collidepoint(pos):
                                            if not re1280x1024.rect.collidepoint(pos):
                                                if not re1280x720.rect.collidepoint(pos):
                                                    if not re1920x1080.rect.collidepoint(pos):
                                                        pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
                                                        

            
            Settingmenu.draw()
            SettingsVideo_Label.draw(menu=self)
            SettingsSound_Label.draw(menu=self)
            SettingsControls_Label.draw(menu=self)
            SettingsBack_Button.draw(menu=self)
            
            Fullcheckbox.draw(player=self.player)
            Fullscreen_label.draw()
            
            resolution_label.draw()
            dropdownmenu.draw(toggle_res_frame=toggle_res_frame)
            current_res.draw()

            if self.player.fullscreen:
                old_fullscreen_rect = AllSettings.DISPLAY.blit(AllSettings.xohnekasten,(815,210))
            else:
                if (old_fullscreen_rect != None):
                    AllSettings.DISPLAY.fill(AllSettings.Black, old_fullscreen_rect)
              

            
            if self.res_frame_open:
                old_res_frame_rect = dropdown_frame.draw()
                re1920x1080.draw(toggle_res_frame=toggle_res_frame)
                re1680x1050.draw(toggle_res_frame=toggle_res_frame)
                re1280x1024.draw(toggle_res_frame=toggle_res_frame)
                re1280x720.draw(toggle_res_frame=toggle_res_frame)
            else:
                if old_res_frame_rect != None:
                    AllSettings.DISPLAY.fill(AllSettings.Black, old_res_frame_rect)
            
            pygame.display.update() 

    def Controlmenu(self):
        controldraw = controlesettings()
        key_labels = Key_Labels()
        key_input_boxes = Key_Input_Boxes()
        
        
        old_textinput_shoot_rect = None
        old_textinput_move_right_rect = None
        old_textinput_move_left_rect = None
        old_textinput_settings_rect = None
        while (not self.back) and (self.selected_window == Window.Control):
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                    
            pos = pygame.mouse.get_pos()
            if not SettingsControls_Label.rect.collidepoint(pos):
                if not SettingsVideo_Label.rect.collidepoint(pos):
                    if not SettingsSound_Label.rect.collidepoint(pos):
                        if not SettingsBack_Button.rect.collidepoint(pos):
                            if not key_input_boxes.rect.collidepoint(pos):
                                pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
                                
            Settingmenu.draw()
            SettingsControls_Label.draw(menu=self)
            SettingsVideo_Label.draw(menu=self)
            SettingsSound_Label.draw(menu=self)
            SettingsBack_Button.draw(menu=self)
            
            key_labels.draw()
            controldraw.draw()
            key_input_boxes.draw(player=self.player)

            
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
            textinput_shoot = font.render(pygame.key.name(self.player.shoot_key), True, AllSettings.Yellow)
            old_textinput_shoot_rect = AllSettings.DISPLAY.blit(textinput_shoot,(910,170))

            #move right key
            textinput_move_right = font.render(pygame.key.name(self.player.move_right_key), True, AllSettings.Yellow)
            old_textinput_move_right_rect = AllSettings.DISPLAY.blit(textinput_move_right,(910,270))

            #move left key
            textinput_move_left = font.render(pygame.key.name(self.player.move_left_key), True, AllSettings.Yellow)
            old_textinput_move_left_rect = AllSettings.DISPLAY.blit(textinput_move_left,(910,370))
        
            #shoot key
            textinput_settings = font.render(pygame.key.name(self.player.settings_key), True, AllSettings.Yellow)
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

class Volume_Label():
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

class Music_Label():
    def __init__(self):
        self.image = AllSettings.musicpng
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 295

    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

class Resolution_Label():
    def __init__(self):
        self.image = AllSettings.reso
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 295
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
        
class Dropdown_Menu():
    def __init__(self):
        self.image = AllSettings.zeile
        self.rect = self.image.get_rect()
        self.rect.x = 775
        self.rect.y = 286
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
        
    def draw(self,toggle_res_frame):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    toggle_res_frame()
class Dropdown_Frame():
    def __init__(self):
        self.image = AllSettings.rahmen
        self.rect = self.image.get_rect()
        self.rect.x = 775
        self.rect.y = 335
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x,self.rect.y))
        
class currentResolution_Label():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(f"{AllSettings.screen_width} x {AllSettings.screen_height}", True, AllSettings.Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 785
        self.rect.y = 282

    def draw(self):
        AllSettings.DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

class res_dropdown_button():
    def __init__(self,x,y,width,height):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(f"{width} x {height}", True, AllSettings.Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
        
    def draw(self,toggle_res_frame):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    AllSettings.screen_height = self.height
                    AllSettings.screen_width = self.width
                    AllSettings.DISPLAY= pygame.display.set_mode((self.width,self.height),0,64)
                    toggle_res_frame()
                    

class Fullscreen_Label():
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
    def draw(self,player: Player.Player):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    player.fullscreen = False 
                    pygame.display.toggle_fullscreen()
                    
class controlesettings():
    def __init__(self):
        self.image = AllSettings.keyspng
        self.rect = self.image.get_rect()       
        self.rect.x = 181
        self.rect.y = 204
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

class Key_Labels():
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

class Key_Input_Boxes():
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
        self.start_input_shoot = False
        self.start_input_move_left = False
        self.start_input_move_right = False
        self.start_input_settings = False
        
    def return_key(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                print(event.key)
                return event.key
                
        
    def draw(self,player: Player.Player):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.keyinput,(self.rect.x,self.rect.y))
        AllSettings.DISPLAY.blit(self.keyinput1,(self.rect1.x,self.rect1.y))
        AllSettings.DISPLAY.blit(self.keyinput2,(self.rect2.x,self.rect2.y))
        AllSettings.DISPLAY.blit(self.keyinput3,(self.rect3.x,self.rect3.y))
        
        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                self.start_input_shoot = True
                
        elif self.rect1.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                self.start_input_move_right = True

        elif self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                self.start_input_move_left = True
                
        elif self.rect3.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                self.start_input_settings = True

        if self.start_input_shoot:
            key = self.return_key()
            if key != None:
                self.start_input_shoot = False
                player.shoot_key = key

        elif self.start_input_move_right:
            key = self.return_key()
            if key != None:
                self.start_input_move_right = False
                player.move_right_key = key
                
        elif self.start_input_move_left:
            key = self.return_key()
            if key != None:
                self.start_input_move_left = False
                player.move_left_key = key
                
        elif self.start_input_settings:
            key = self.return_key()
            if key != None:
                self.start_input_settings = False
                player.settings_key = key
                   
                
                
cooldown0 = 1200

last0 = pygame.time.get_ticks()


SettingsSound_Label = SoundSettings()
SettingsVideo_Label = VideoSettings()
SettingsControls_Label = ControlsSettings()
SettingsBack_Button = backSettingsMenu()


Settingsbutton = ButtonSettings()
Menusbutton = ButtonMenu()
Continuebutton = ButtonContinue()
Settingmenu = SettingsMenuBackground()
