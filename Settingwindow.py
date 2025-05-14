

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
    def __init__(self):
        super().__init__()
        self.is_running = True
        self.selected_window = Window.Sound,
        self.settings_menu_selected = False
        self.back = False
        self.start_input = False

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
            pygame.display.flip()  
        
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
            SettingsSound.draw()
            SettingsVideo.draw()
            SettingsControls.draw()
            SettingsBack.draw()
            pygame.display.flip()
                
    def Soundmenu(self):
        while (not self.back) and (self.selected_window == Window.Sound):
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
            pos = pygame.mouse.get_pos()
            if not SettingsSound.rect.collidepoint(pos):
                if not SettingsVideo.rect.collidepoint(pos):
                    if not SettingsControls.rect.collidepoint(pos):
                        if not plus2.rect.collidepoint(pos):
                            if not minus2.rect.collidepoint(pos):
                                if not minus3.rect.collidepoint(pos):
                                    pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
            Settingmenu.draw()
            SettingsSound.draw()
            SettingsVideo.draw()
            SettingsControls.draw()
            plus2.draw()
            minus2.draw()
            plus3.draw()
            minus3.draw()
            Volumepng.draw()
            Musicpng.draw()

            s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(620,211,20,40),border_radius=10)
            s2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(655,211,20,40),border_radius=10)
            s3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(690,211,20,40),border_radius=10)
            s4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(725,211,20,40),border_radius=10)
            s5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(760,211,20,40),border_radius=10)
            s6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(795,211,20,40),border_radius=10)
            s7 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(830,211,20,40),border_radius=10)
            s8 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(865,211,20,40),border_radius=10)
            s9 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(900,211,20,40),border_radius=10)
            s10 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(935,211,20,40),border_radius=10)

            m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(620,295,20,40),border_radius=10)
            m2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(655,295,20,40),border_radius=10)
            m3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(690,295,20,40),border_radius=10)
            m4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(725,295,20,40),border_radius=10)
            m5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(760,295,20,40),border_radius=10)
            m6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(795,295,20,40),border_radius=10)
            m7 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(830,295,20,40),border_radius=10)
            m8 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(865,295,20,40),border_radius=10)
            m9 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(900,295,20,40),border_radius=10)
            m10 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.WHITE,pygame.Rect(935,295,20,40),border_radius=10)

            if AllSettings.volume == 0:
                s10 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(620,211,20,40),border_radius=10)
                s9 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(655,211,20,40),border_radius=10)
                s8 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(690,211,20,40),border_radius=10)
                s7 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(725,211,20,40),border_radius=10)
                s6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(760,211,20,40),border_radius=10)
                s5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,211,20,40),border_radius=10)
                s4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,211,20,40),border_radius=10)
                s3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,211,20,40),border_radius=10)
                s2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,211,20,40),border_radius=10)
                s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,211,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25)) 
            if AllSettings.volume == 10:
                s9 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(655,211,20,40),border_radius=10)
                s8 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(690,211,20,40),border_radius=10)
                s7 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(725,211,20,40),border_radius=10)
                s6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(760,211,20,40),border_radius=10)
                s5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,211,20,40),border_radius=10)
                s4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,211,20,40),border_radius=10)
                s3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,211,20,40),border_radius=10)
                s2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,211,20,40),border_radius=10)
                s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,211,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25))                  
            if AllSettings.volume == 20:
                s8 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(690,211,20,40),border_radius=10)
                s7 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(725,211,20,40),border_radius=10)
                s6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(760,211,20,40),border_radius=10)
                s5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,211,20,40),border_radius=10)
                s4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,211,20,40),border_radius=10)
                s3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,211,20,40),border_radius=10)
                s2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,211,20,40),border_radius=10)
                s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,211,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25))  
            if AllSettings.volume == 30:
                s7 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(725,211,20,40),border_radius=10)
                s6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(760,211,20,40),border_radius=10)
                s5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,211,20,40),border_radius=10)
                s4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,211,20,40),border_radius=10)
                s3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,211,20,40),border_radius=10)
                s2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,211,20,40),border_radius=10)
                s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,211,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25))     
            if AllSettings.volume == 40:
                s6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(760,211,20,40),border_radius=10)
                s5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,211,20,40),border_radius=10)
                s4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,211,20,40),border_radius=10)
                s3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,211,20,40),border_radius=10)
                s2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,211,20,40),border_radius=10)
                s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,211,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25))
            if AllSettings.volume == 50:
                s5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,211,20,40),border_radius=10)
                s4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,211,20,40),border_radius=10)
                s3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,211,20,40),border_radius=10)
                s2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,211,20,40),border_radius=10)
                s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,211,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25))
            if AllSettings.volume == 60:
                s4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,211,20,40),border_radius=10)
                s3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,211,20,40),border_radius=10)
                s2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,211,20,40),border_radius=10)
                s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,211,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25)) 
            if AllSettings.volume == 70:
                s3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,211,20,40),border_radius=10)
                s2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,211,20,40),border_radius=10)
                s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,211,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25))    
            if AllSettings.volume == 80:
                s2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,211,20,40),border_radius=10)
                s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,211,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25))
            if AllSettings.volume == 90:
                s1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,211,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25))
            if AllSettings.volume == 100:
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,260,60,25))


            AllSettings.shot.set_volume(AllSettings.volume/100)
            AllSettings.click.set_volume(AllSettings.volume/100)
            AllSettings.explosound.set_volume(AllSettings.volume/100)
            AllSettings.music.set_volume(AllSettings.musicvolume/100)

            if AllSettings.musicvolume == 0:
                m10 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(620,295,20,40),border_radius=10)
                m9 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(655,295,20,40),border_radius=10)
                m8 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(690,295,20,40),border_radius=10)
                m7 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(725,295,20,40),border_radius=10)
                m6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(760,295,20,40),border_radius=10)
                m5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,295,20,40),border_radius=10)
                m4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,295,20,40),border_radius=10)
                m3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,295,20,40),border_radius=10)
                m2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,295,20,40),border_radius=10)
                m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,295,20,40),border_radius=10)
                AllSettings.music.stop()
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25)) 
            if AllSettings.musicvolume == 10:
                m9 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(655,295,20,40),border_radius=10)
                m8 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(690,295,20,40),border_radius=10)
                m7 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(725,295,20,40),border_radius=10)
                m6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(760,295,20,40),border_radius=10)
                m5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,295,20,40),border_radius=10)
                m4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,295,20,40),border_radius=10)
                m3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,295,20,40),border_radius=10)
                m2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,295,20,40),border_radius=10)
                m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,295,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25))                  
            if AllSettings.musicvolume == 20:
                m8 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(690,295,20,40),border_radius=10)
                m7 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(725,295,20,40),border_radius=10)
                m6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(760,295,20,40),border_radius=10)
                m5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,295,20,40),border_radius=10)
                m4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,295,20,40),border_radius=10)
                m3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,295,20,40),border_radius=10)
                m2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,295,20,40),border_radius=10)
                m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,295,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25))  
            if AllSettings.musicvolume == 30:
                m7 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(725,295,20,40),border_radius=10)
                m6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(760,295,20,40),border_radius=10)
                m5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,295,20,40),border_radius=10)
                m4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,295,20,40),border_radius=10)
                m3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,295,20,40),border_radius=10)
                m2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,295,20,40),border_radius=10)
                m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,295,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25))     
            if AllSettings.musicvolume == 40:
                m6 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(760,295,20,40),border_radius=10)
                m5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,295,20,40),border_radius=10)
                m4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,295,20,40),border_radius=10)
                m3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,295,20,40),border_radius=10)
                m2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,295,20,40),border_radius=10)
                m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,295,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25))
            if AllSettings.musicvolume == 50:
                m5 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,295,20,40),border_radius=10)
                m4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,295,20,40),border_radius=10)
                m3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,295,20,40),border_radius=10)
                m2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,295,20,40),border_radius=10)
                m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,295,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25))
            if AllSettings.musicvolume == 60:
                m4 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(830,295,20,40),border_radius=10)
                m3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,295,20,40),border_radius=10)
                m2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,295,20,40),border_radius=10)
                m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,295,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25)) 
            if AllSettings.musicvolume == 70:
                m3 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(865,295,20,40),border_radius=10)
                m2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,295,20,40),border_radius=10)
                m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,295,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25))    
            if AllSettings.musicvolume == 80:
                m2 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(900,295,20,40),border_radius=10)
                m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,295,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25))
            if AllSettings.musicvolume == 90:
                m1 = pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(935,295,20,40),border_radius=10)
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25))
            if AllSettings.musicvolume == 100:
                pygame.draw.rect(AllSettings.DISPLAY,AllSettings.Black,pygame.Rect(795,340,60,25))


            font_obj2 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
            Volume2 = font_obj2.render(str(AllSettings.volume) + "%" , True, AllSettings.WHITE)
            AllSettings.DISPLAY.blit(Volume2,(795,260))

            font_obj3 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
            Volume3 = font_obj3.render(str(AllSettings.musicvolume) + "%" , True, AllSettings.WHITE)
            AllSettings.DISPLAY.blit(Volume3,(795,340))
                        
                                    
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
            SettingsVideo.draw()
            SettingsSound.draw()
            SettingsControls.draw()
            SettingsBack.draw()
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
            SettingsControls.draw()
            SettingsVideo.draw()
            SettingsSound.draw()
            SettingsBack.draw()
            controlkeydraw.draw()
            controldraw.draw()
            controlkeyinputdraw.draw()

            # shoot    
            if self.start_input:
                pygame.key.get_pressed().first()

            font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
            textinput = font.render(pygame.key.name(AllSettings.keywaspressed), True, AllSettings.Yellow)
            AllSettings.DISPLAY.blit(textinput,(910,170))

            # move right
            if AllSettings.startinput == True:
                pygame.key.get_pressed()
            font1 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
            textinput1 = font1.render(pygame.key.name(AllSettings.keywaspressed1), True, AllSettings.Yellow)
            AllSettings.DISPLAY.blit(textinput1,(910,270))

            # move left
            font2 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
            textinput2 = font2.render(pygame.key.name(AllSettings.keywaspressed2), True, AllSettings.Yellow)
            AllSettings.DISPLAY.blit(textinput2,(910,370))
        
            # Settings
            
            font3 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
            textinput3 = font3.render(pygame.key.name(AllSettings.keywaspressed3), True, AllSettings.Yellow)
            AllSettings.DISPLAY.blit(textinput3,(910,470))

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

class SettingsMenu():
    def __init__(self):
        self.image = AllSettings.Settingsmenu
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
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                menu = Menu()
                menu.selected_window = Window.Sound
                menu.Soundmenu()

class VideoSettings():
    def __init__(self):
        self.image = AllSettings.Video
        self.rect = self.image.get_rect()
        self.rect.x = 517
        self.rect.y = 134
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                menu = Menu()
                menu.selected_window = Window.Video
                menu.VideoSettings()

class ControlsSettings():
    def __init__(self):
        self.image = AllSettings.Controls
        self.rect = self.image.get_rect()
        self.rect.x = 823
        self.rect.y = 134
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                menu = Menu()
                menu.selected_window = Window.Control
                menu.Controlmenu()

class backSettingsMenu():
    def __init__(self):
        self.image = AllSettings.Back
        self.rect = self.image.get_rect()
        self.rect.x = 967
        self.rect.y = 566 
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                menu = Menu()
                menu.back = True



class Volume():
    def __init__(self):
        self.image = AllSettings.volumepng
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 204
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
class Plus():
    def __init__(self):
        self.image = AllSettings.plus
        self.rect = self.image.get_rect()
        self.rect.x = 975
        self.rect.y = 211
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
                    AllSettings.volume += 10
                    if AllSettings.volume > 100:
                        AllSettings.volume = 100
class Minus():
    def __init__(self):
        self.image = AllSettings.minus
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 211
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:#
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    AllSettings.volume -= 10
                    if AllSettings.volume < 0:
                        AllSettings.volume = 0
class Volume1():
    def __init__(self):
        self.image = AllSettings.musicpng
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 295
    def draw(self):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
class Plus1():
    def __init__(self):
        self.image = AllSettings.plus
        self.rect = self.image.get_rect()
        self.rect.x = 975
        self.rect.y = 295
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
                    AllSettings.musicvolume += 10
                    if AllSettings.musicvolume > 100:
                        AllSettings.musicvolume = 100
class Minus1():
    def __init__(self):
        self.image = AllSettings.minus
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 295
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        pos = pygame.mouse.get_pos()
        pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    AllSettings.click.play()
                    AllSettings.musicvolume -= 10
                    if AllSettings.musicvolume < 0:
                        AllSettings.musicvolume = 0
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
    def draw(self):
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.keyinput,(self.rect.x,self.rect.y))
        AllSettings.DISPLAY.blit(self.keyinput1,(self.rect1.x,self.rect1.y))
        AllSettings.DISPLAY.blit(self.keyinput2,(self.rect2.x,self.rect2.y))
        AllSettings.DISPLAY.blit(self.keyinput3,(self.rect3.x,self.rect3.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.startinput = True
        if self.rect1.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.startinput1 = True
        if self.rect2.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.startinput2 = True
        if self.rect3.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.startinput3 = True

cooldown0 = 1200
last0 = pygame.time.get_ticks()
controldraw = controlesettings()
controlkeydraw = keys()
controlkeyinputdraw = keyinputs()
Fullcheckbox = Fullscreencheckbox()
Fullscreenmodepng = Fullscreenmode()
SettingsSound = SoundSettings()
SettingsVideo = VideoSettings()
SettingsControls = ControlsSettings()
SettingsBack = backSettingsMenu()
Volumepng = Volume()
Musicpng = Volume1()
minus2 = Minus()
plus2 = Plus()
minus3 = Minus1()
plus3 = Plus1()
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
Settingmenu = SettingsMenu()
