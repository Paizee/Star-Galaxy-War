

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

class Menu():
    def __init__(self):
        super().__init__()
        self.is_running = True


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
        if AllSettings.Settings == True:
            while True: 
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
                if back == True:
                    AllSettings.DISPLAY.blit(AllSettings.background, (0, 0))
                    
                    break
                
    def Soundmenu(self):
        global soundm,breaksound
        if soundm == True:
            while True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        exit()
                pos = pygame.mouse.get_pos()
                if not SettingsSound.rect.collidepoint(pos):
                    if not SettingsVideo.rect.collidepoint(pos):
                        if not SettingsControls.rect.collidepoint(pos):
                            if not SoundBack.rect.collidepoint(pos):
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
                SoundBack.draw()
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
                if back == True:
                    break

                if breaksound == True:
                    break

    def VideoSettings(self):
        if vidsettings == True: 
            while True:
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
                SettingsVideo1.draw()
                SettingsSound1.draw()
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

                if back == True:               
                    break

                if breakvideo == True:
                    break
    def Conntrolmenu(self):
        if control == True: 
            while True:
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
                if AllSettings.startinput == True:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                AllSettings.keywaspressed = K_BACKSPACE
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_TAB]:
                                AllSettings.keywaspressed = K_TAB
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_CLEAR]:
                                AllSettings.keywaspressed = K_CLEAR
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_RETURN]:
                                AllSettings.keywaspressed = K_RETURN
                                AllSettings.startinput = False  
                            if pygame.key.get_pressed()[K_PAUSE]:
                                AllSettings.keywaspressed = K_PAUSE
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_ESCAPE]:
                                AllSettings.keywaspressed = K_ESCAPE
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_SPACE]:
                                AllSettings.keywaspressed = K_SPACE
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_EXCLAIM]:
                                AllSettings.keywaspressed = K_EXCLAIM
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_QUOTEDBL]:
                                AllSettings.keywaspressed = K_QUOTEDBL
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_HASH]:
                                AllSettings.keywaspressed = K_HASH
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_DOLLAR]:
                                AllSettings.keywaspressed = K_DOLLAR
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_AMPERSAND]:
                                AllSettings.keywaspressed = K_AMPERSAND
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_QUOTE]:
                                AllSettings.keywaspressed = K_QUOTE
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_LEFTPAREN]:
                                AllSettings.keywaspressed = K_LEFTPAREN
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_RIGHTPAREN]:
                                AllSettings.keywaspressed = K_RIGHTPAREN
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_ASTERISK]:
                                AllSettings.keywaspressed = K_ASTERISK
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_PLUS]:
                                AllSettings.keywaspressed = K_PLUS
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_COMMA]:
                                AllSettings.keywaspressed = K_COMMA
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_MINUS]:
                                AllSettings.keywaspressed = K_MINUS
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_PERIOD]:
                                AllSettings.keywaspressed = K_PERIOD
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_SLASH]:
                                AllSettings.keywaspressed = K_SLASH
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_0]:
                                AllSettings.keywaspressed = K_0
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_1]:
                                AllSettings.keywaspressed = K_1
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_2]:
                                AllSettings.keywaspressed = K_2
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_3]:
                                AllSettings.keywaspressed = K_3
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_4]:
                                AllSettings.keywaspressed = K_4
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_5]:
                                AllSettings.keywaspressed = K_5
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_6]:
                                AllSettings.keywaspressed = K_6
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_7]:
                                AllSettings.keywaspressed = K_7
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_8]:
                                AllSettings.keywaspressed = K_8
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_9]:
                                AllSettings.keywaspressed = K_9
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_COLON]:
                                AllSettings.keywaspressed = K_COLON
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_SEMICOLON]:
                                AllSettings.keywaspressed = K_SEMICOLON
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_LESS]:
                                AllSettings.keywaspressed = K_LESS
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_EQUALS]:
                                AllSettings.keywaspressed = K_EQUALS
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_GREATER]:
                                AllSettings.keywaspressed = K_GREATER
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_QUESTION]:
                                AllSettings.keywaspressed = K_QUESTION
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_AT]:
                                AllSettings.keywaspressed = K_AT
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_LEFTBRACKET]:
                                AllSettings.keywaspressed = K_LEFTBRACKET
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_BACKSLASH]:
                                AllSettings.keywaspressed = K_BACKSLASH
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_RIGHTBRACKET]:
                                AllSettings.keywaspressed = K_RIGHTBRACKET
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_CARET]:
                                AllSettings.keywaspressed = K_CARET
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_UNDERSCORE]:
                                AllSettings.keywaspressed = K_UNDERSCORE
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_BACKQUOTE]:
                                AllSettings.keywaspressed = K_BACKQUOTE
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_a]:
                                AllSettings.keywaspressed = K_a
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_b]:
                                AllSettings.keywaspressed = K_b
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_c]:
                                AllSettings.keywaspressed = K_c
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_d]:
                                AllSettings.keywaspressed = K_d
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_e]:
                                AllSettings.keywaspressed = K_e
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_f]:
                                AllSettings.keywaspressed = K_f
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_g]:
                                AllSettings.keywaspressed = K_g
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_h]:
                                AllSettings.keywaspressed = K_h
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_i]:
                                AllSettings.keywaspressed = K_i
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_j]:
                                AllSettings.keywaspressed = K_j
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_k]:
                                AllSettings.keywaspressed = K_k
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_l]:
                                AllSettings.keywaspressed = K_l
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_m]:
                                AllSettings.keywaspressed = K_m
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_o]:
                                AllSettings.keywaspressed = K_o
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_p]:
                                AllSettings.keywaspressed = K_p
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_q]:
                                AllSettings.keywaspressed = K_q
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_r]:
                                AllSettings.keywaspressed = K_r
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_s]:
                                AllSettings.keywaspressed = K_s
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_t]:
                                AllSettings.keywaspressed = K_t
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_u]:
                                AllSettings.keywaspressed = K_u
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_v]:
                                AllSettings.keywaspressed = K_v
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_w]:
                                AllSettings.keywaspressed = K_w
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_x]:
                                AllSettings.keywaspressed = K_x
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_y]:
                                AllSettings.keywaspressed = K_y
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_z]:
                                AllSettings.keywaspressed = K_z
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_DELETE]:
                                AllSettings.keywaspressed = K_DELETE
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP0]:
                                AllSettings.keywaspressed = K_KP0
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP1]:
                                AllSettings.keywaspressed = K_KP1
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP2]:
                                AllSettings.keywaspressed = K_KP2
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP3]:
                                AllSettings.keywaspressed = K_KP3
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP4]:
                                AllSettings.keywaspressed = K_KP4
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP5]:
                                AllSettings.keywaspressed = K_KP5
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP6]:
                                AllSettings.keywaspressed = K_KP6
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP7]:
                                AllSettings.keywaspressed = K_KP7
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP8]:
                                AllSettings.keywaspressed = K_KP8
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP9]:
                                AllSettings.keywaspressed = K_KP9
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP_PERIOD]:
                                AllSettings.keywaspressed = K_BACKSPACE
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP_DIVIDE]:
                                AllSettings.keywaspressed = K_KP_DIVIDE
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP_MULTIPLY]:
                                AllSettings.keywaspressed = K_KP_MULTIPLY
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP_MINUS]:
                                AllSettings.keywaspressed = K_KP_MINUS
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP_PLUS]:
                                AllSettings.keywaspressed = K_KP_PLUS
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP_ENTER]:
                                AllSettings.keywaspressed = K_KP_ENTER
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_KP_EQUALS]:
                                AllSettings.keywaspressed = K_KP_EQUALS
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_UP]:
                                AllSettings.keywaspressed = K_UP
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_DOWN]:
                                AllSettings.keywaspressed = K_DOWN
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_RIGHT]:
                                AllSettings.keywaspressed = K_RIGHT
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_LEFT]:
                                AllSettings.keywaspressed = K_LEFT
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_INSERT]:
                                AllSettings.keywaspressed = K_INSERT
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_HOME]:
                                AllSettings.keywaspressed = K_HOME
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_END]:
                                AllSettings.keywaspressed = K_END
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_PAGEUP]:
                                AllSettings.keywaspressed = K_PAGEUP
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_PAGEDOWN]:
                                AllSettings.keywaspressed = K_PAGEDOWN
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F1]:
                                AllSettings.keywaspressed = K_F1
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F2]:
                                AllSettings.keywaspressed = K_F2
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F3]:
                                AllSettings.keywaspressed = K_F3
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F4]:
                                AllSettings.keywaspressed = K_F4
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F5]:
                                AllSettings.keywaspressed = K_F5
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F6]:
                                AllSettings.keywaspressed = K_F6
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F7]:
                                AllSettings.keywaspressed = K_F7
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F8]:
                                AllSettings.keywaspressed = K_F8
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F9]:
                                AllSettings.keywaspressed = K_F9
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F10]:
                                AllSettings.keywaspressed = K_F10
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F11]:
                                AllSettings.keywaspressed = K_F11
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F12]:
                                AllSettings.keywaspressed = K_F12
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F13]:
                                AllSettings.keywaspressed = K_F13
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F14]:
                                AllSettings.keywaspressed = K_F14
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_F15]:
                                AllSettings.keywaspressed = K_F15
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_NUMLOCK]:
                                AllSettings.keywaspressed = K_NUMLOCK
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_CAPSLOCK]:
                                AllSettings.keywaspressed = K_CAPSLOCK
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_SCROLLOCK]:
                                AllSettings.keywaspressed = K_SCROLLOCK
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_RSHIFT]:
                                AllSettings.keywaspressed = K_RSHIFT
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_LSHIFT]:
                                AllSettings.keywaspressed = K_LSHIFT
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_RCTRL]:
                                AllSettings.keywaspressed = K_RCTRL
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_LCTRL]:
                                AllSettings.keywaspressed = K_LCTRL
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_RALT]:
                                AllSettings.keywaspressed = K_RALT
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_LALT]:
                                AllSettings.keywaspressed = K_LALT
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_RMETA]:
                                AllSettings.keywaspressed = K_RMETA
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_LMETA]:
                                AllSettings.keywaspressed = K_LMETA
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_LSUPER]:
                                AllSettings.keywaspressed = K_LSUPER
                                AllSettings.startinput = False
                            if pygame.key.get_pressed()[K_RSUPER]:
                                AllSettings.keywaspressed = K_RSUPER
                                AllSettings.startinput = False
                font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
                textinput = font.render(pygame.key.name(AllSettings.keywaspressed), True, AllSettings.Yellow)
                AllSettings.DISPLAY.blit(textinput,(910,170))
                if AllSettings.startinput1 == True:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                AllSettings.keywaspressed1 = K_BACKSPACE
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_TAB]:
                                AllSettings.keywaspressed1 = K_TAB
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_CLEAR]:
                                AllSettings.keywaspressed1 = K_CLEAR
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_RETURN]:
                                AllSettings.keywaspressed1 = K_RETURN
                                AllSettings.startinput1 = False  
                            if pygame.key.get_pressed()[K_PAUSE]:
                                AllSettings.keywaspressed1 = K_PAUSE
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_ESCAPE]:
                                AllSettings.keywaspressed1 = K_ESCAPE
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_SPACE]:
                                AllSettings.keywaspressed1 = K_SPACE
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_EXCLAIM]:
                                AllSettings.keywaspressed1 = K_EXCLAIM
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_QUOTEDBL]:
                                AllSettings.keywaspressed1 = K_QUOTEDBL
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_HASH]:
                                AllSettings.keywaspressed1 = K_HASH
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_DOLLAR]:
                                AllSettings.keywaspressed1 = K_DOLLAR
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_AMPERSAND]:
                                AllSettings.keywaspressed1 = K_AMPERSAND
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_QUOTE]:
                                AllSettings.keywaspressed1 = K_QUOTE
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_LEFTPAREN]:
                                AllSettings.keywaspressed1 = K_LEFTPAREN
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_RIGHTPAREN]:
                                AllSettings.keywaspressed1 = K_RIGHTPAREN
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_ASTERISK]:
                                AllSettings.keywaspressed1 = K_ASTERISK
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_PLUS]:
                                AllSettings.keywaspressed1 = K_PLUS
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_COMMA]:
                                AllSettings.keywaspressed1 = K_COMMA
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_MINUS]:
                                AllSettings.keywaspressed1 = K_MINUS
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_PERIOD]:
                                AllSettings.keywaspressed1 = K_PERIOD
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_SLASH]:
                                AllSettings.keywaspressed1 = K_SLASH
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_0]:
                                AllSettings.keywaspressed1 = K_0
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_1]:
                                AllSettings.keywaspressed1 = K_1
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_2]:
                                AllSettings.keywaspressed1 = K_2
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_3]:
                                AllSettings.keywaspressed1 = K_3
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_4]:
                                AllSettings.keywaspressed1 = K_4
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_5]:
                                AllSettings.keywaspressed1 = K_5
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_6]:
                                AllSettings.keywaspressed1 = K_6
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_7]:
                                AllSettings.keywaspressed1 = K_7
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_8]:
                                AllSettings.keywaspressed1 = K_8
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_9]:
                                AllSettings.keywaspressed1 = K_9
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_COLON]:
                                AllSettings.keywaspressed1 = K_COLON
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_SEMICOLON]:
                                AllSettings.keywaspressed1 = K_SEMICOLON
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_LESS]:
                                AllSettings.keywaspressed1 = K_LESS
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_EQUALS]:
                                AllSettings.keywaspressed1 = K_EQUALS
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_GREATER]:
                                AllSettings.keywaspressed1 = K_GREATER
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_QUESTION]:
                                AllSettings.keywaspressed1 = K_QUESTION
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_AT]:
                                AllSettings.keywaspressed1 = K_AT
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_LEFTBRACKET]:
                                AllSettings.keywaspressed1 = K_LEFTBRACKET
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_BACKSLASH]:
                                AllSettings.keywaspressed1 = K_BACKSLASH
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_RIGHTBRACKET]:
                                AllSettings.keywaspressed1 = K_RIGHTBRACKET
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_CARET]:
                                AllSettings.keywaspressed1 = K_CARET
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_UNDERSCORE]:
                                AllSettings.keywaspressed1 = K_UNDERSCORE
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_BACKQUOTE]:
                                AllSettings.keywaspressed1 = K_BACKQUOTE
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_a]:
                                AllSettings.keywaspressed1 = K_a
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_b]:
                                AllSettings.keywaspressed1 = K_b
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_c]:
                                AllSettings.keywaspressed1 = K_c
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_d]:
                                AllSettings.keywaspressed1 = K_d
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_e]:
                                AllSettings.keywaspressed1 = K_e
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_f]:
                                AllSettings.keywaspressed1 = K_f
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_g]:
                                AllSettings.keywaspressed1 = K_g
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_h]:
                                AllSettings.keywaspressed1 = K_h
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_i]:
                                AllSettings.keywaspressed1 = K_i
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_j]:
                                AllSettings.keywaspressed1 = K_j
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_k]:
                                AllSettings.keywaspressed1 = K_k
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_l]:
                                AllSettings.keywaspressed1 = K_l
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_m]:
                                AllSettings.keywaspressed1 = K_m
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_o]:
                                AllSettings.keywaspressed1 = K_o
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_p]:
                                AllSettings.keywaspressed1 = K_p
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_q]:
                                AllSettings.keywaspressed1 = K_q
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_r]:
                                AllSettings.keywaspressed1 = K_r
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_s]:
                                AllSettings.keywaspressed1 = K_s
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_t]:
                                AllSettings.keywaspressed1 = K_t
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_u]:
                                AllSettings.keywaspressed1 = K_u
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_v]:
                                AllSettings.keywaspressed1 = K_v
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_w]:
                                AllSettings.keywaspressed1 = K_w
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_x]:
                                AllSettings.keywaspressed1 = K_x
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_y]:
                                AllSettings.keywaspressed1 = K_y
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_z]:
                                AllSettings.keywaspressed1 = K_z
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_DELETE]:
                                AllSettings.keywaspressed1 = K_DELETE
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP0]:
                                AllSettings.keywaspressed1 = K_KP0
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP1]:
                                AllSettings.keywaspressed1 = K_KP1
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP2]:
                                AllSettings.keywaspressed1 = K_KP2
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP3]:
                                AllSettings.keywaspressed1 = K_KP3
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP4]:
                                AllSettings.keywaspressed1 = K_KP4
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP5]:
                                AllSettings.keywaspressed1 = K_KP5
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP6]:
                                AllSettings.keywaspressed1 = K_KP6
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP7]:
                                AllSettings.keywaspressed1 = K_KP7
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP8]:
                                AllSettings.keywaspressed1 = K_KP8
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP9]:
                                AllSettings.keywaspressed1 = K_KP9
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP_PERIOD]:
                                AllSettings.keywaspressed1 = K_BACKSPACE
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP_DIVIDE]:
                                AllSettings.keywaspressed1 = K_KP_DIVIDE
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP_MULTIPLY]:
                                AllSettings.keywaspressed1 = K_KP_MULTIPLY
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP_MINUS]:
                                AllSettings.keywaspressed1 = K_KP_MINUS
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP_PLUS]:
                                AllSettings.keywaspressed1 = K_KP_PLUS
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP_ENTER]:
                                AllSettings.keywaspressed1 = K_KP_ENTER
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_KP_EQUALS]:
                                AllSettings.keywaspressed1 = K_KP_EQUALS
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_UP]:
                                AllSettings.keywaspressed1 = K_UP
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_DOWN]:
                                AllSettings.keywaspressed1 = K_DOWN
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_RIGHT]:
                                AllSettings.keywaspressed1 = K_RIGHT
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_LEFT]:
                                AllSettings.keywaspressed1 = K_LEFT
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_INSERT]:
                                AllSettings.keywaspressed1 = K_INSERT
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_HOME]:
                                AllSettings.keywaspressed1 = K_HOME
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_END]:
                                AllSettings.keywaspressed1 = K_END
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_PAGEUP]:
                                AllSettings.keywaspressed1 = K_PAGEUP
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_PAGEDOWN]:
                                AllSettings.keywaspressed1 = K_PAGEDOWN
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F1]:
                                AllSettings.keywaspressed1 = K_F1
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F2]:
                                AllSettings.keywaspressed1 = K_F2
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F3]:
                                AllSettings.keywaspressed1 = K_F3
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F4]:
                                AllSettings.keywaspressed1 = K_F4
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F5]:
                                AllSettings.keywaspressed1 = K_F5
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F6]:
                                AllSettings.keywaspressed1 = K_F6
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F7]:
                                AllSettings.keywaspressed1 = K_F7
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F8]:
                                AllSettings.keywaspressed1 = K_F8
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F9]:
                                AllSettings.keywaspressed1 = K_F9
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F10]:
                                AllSettings.keywaspressed1 = K_F10
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F11]:
                                AllSettings.keywaspressed1 = K_F11
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F12]:
                                AllSettings.keywaspressed1 = K_F12
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F13]:
                                AllSettings.keywaspressed1 = K_F13
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F14]:
                                AllSettings.keywaspressed1 = K_F14
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_F15]:
                                AllSettings.keywaspressed1 = K_F15
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_NUMLOCK]:
                                AllSettings.keywaspressed1 = K_NUMLOCK
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_CAPSLOCK]:
                                AllSettings.keywaspressed1 = K_CAPSLOCK
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_SCROLLOCK]:
                                AllSettings.keywaspressed1 = K_SCROLLOCK
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_RSHIFT]:
                                AllSettings.keywaspressed1 = K_RSHIFT
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_LSHIFT]:
                                AllSettings.keywaspressed1 = K_LSHIFT
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_RCTRL]:
                                AllSettings.keywaspressed1 = K_RCTRL
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_LCTRL]:
                                AllSettings.keywaspressed1 = K_LCTRL
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_RALT]:
                                AllSettings.keywaspressed1 = K_RALT
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_LALT]:
                                AllSettings.keywaspressed1 = K_LALT
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_RMETA]:
                                AllSettings.keywaspressed1 = K_RMETA
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_LMETA]:
                                AllSettings.keywaspressed1 = K_LMETA
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_LSUPER]:
                                AllSettings.keywaspressed1 = K_LSUPER
                                AllSettings.startinput1 = False
                            if pygame.key.get_pressed()[K_RSUPER]:
                                AllSettings.keywaspressed1 = K_RSUPER
                                AllSettings.startinput1 = False
                font1 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
                textinput1 = font1.render(pygame.key.name(AllSettings.keywaspressed1), True, AllSettings.Yellow)
                AllSettings.DISPLAY.blit(textinput1,(910,270))

                if AllSettings.startinput2 == True:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                AllSettings.keywaspressed2 = K_BACKSPACE
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_TAB]:
                                AllSettings.keywaspressed2 = K_TAB
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_CLEAR]:
                                AllSettings.keywaspressed2 = K_CLEAR
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_RETURN]:
                                AllSettings.keywaspressed2 = K_RETURN
                                AllSettings.startinput2 = False  
                            if pygame.key.get_pressed()[K_PAUSE]:
                                AllSettings.keywaspressed2 = K_PAUSE
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_ESCAPE]:
                                AllSettings.keywaspressed2 = K_ESCAPE
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_SPACE]:
                                AllSettings.keywaspressed2 = K_SPACE
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_EXCLAIM]:
                                AllSettings.keywaspressed2 = K_EXCLAIM
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_QUOTEDBL]:
                                AllSettings.keywaspressed2 = K_QUOTEDBL
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_HASH]:
                                AllSettings.keywaspressed2 = K_HASH
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_DOLLAR]:
                                AllSettings.keywaspressed2 = K_DOLLAR
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_AMPERSAND]:
                                AllSettings.keywaspressed2 = K_AMPERSAND
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_QUOTE]:
                                AllSettings.keywaspressed2 = K_QUOTE
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_LEFTPAREN]:
                                AllSettings.keywaspressed2 = K_LEFTPAREN
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_RIGHTPAREN]:
                                AllSettings.keywaspressed2 = K_RIGHTPAREN
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_ASTERISK]:
                                AllSettings.keywaspressed2 = K_ASTERISK
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_PLUS]:
                                AllSettings.keywaspressed2 = K_PLUS
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_COMMA]:
                                AllSettings.keywaspressed2 = K_COMMA
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_MINUS]:
                                AllSettings.keywaspressed2 = K_MINUS
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_PERIOD]:
                                AllSettings.keywaspressed2 = K_PERIOD
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_SLASH]:
                                AllSettings.keywaspressed2 = K_SLASH
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_0]:
                                AllSettings.keywaspressed2 = K_0
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_1]:
                                AllSettings.keywaspressed2 = K_1
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_2]:
                                AllSettings.keywaspressed2 = K_2
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_3]:
                                AllSettings.keywaspressed2 = K_3
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_4]:
                                AllSettings.keywaspressed2 = K_4
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_5]:
                                AllSettings.keywaspressed2 = K_5
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_6]:
                                AllSettings.keywaspressed2 = K_6
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_7]:
                                AllSettings.keywaspressed2 = K_7
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_8]:
                                AllSettings.keywaspressed2 = K_8
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_9]:
                                AllSettings.keywaspressed2 = K_9
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_COLON]:
                                AllSettings.keywaspressed2 = K_COLON
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_SEMICOLON]:
                                AllSettings.keywaspressed2 = K_SEMICOLON
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_LESS]:
                                AllSettings.keywaspressed2 = K_LESS
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_EQUALS]:
                                AllSettings.keywaspressed2 = K_EQUALS
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_GREATER]:
                                AllSettings.keywaspressed2 = K_GREATER
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_QUESTION]:
                                AllSettings.keywaspressed2 = K_QUESTION
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_AT]:
                                AllSettings.keywaspressed2 = K_AT
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_LEFTBRACKET]:
                                AllSettings.keywaspressed2 = K_LEFTBRACKET
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_BACKSLASH]:
                                AllSettings.keywaspressed2 = K_BACKSLASH
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_RIGHTBRACKET]:
                                AllSettings.keywaspressed2 = K_RIGHTBRACKET
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_CARET]:
                                AllSettings.keywaspressed2 = K_CARET
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_UNDERSCORE]:
                                AllSettings.keywaspressed2 = K_UNDERSCORE
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_BACKQUOTE]:
                                AllSettings.keywaspressed2 = K_BACKQUOTE
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_a]:
                                AllSettings.keywaspressed2 = K_a
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_b]:
                                AllSettings.keywaspressed2 = K_b
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_c]:
                                AllSettings.keywaspressed2 = K_c
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_d]:
                                AllSettings.keywaspressed2 = K_d
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_e]:
                                AllSettings.keywaspressed2 = K_e
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_f]:
                                AllSettings.keywaspressed2 = K_f
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_g]:
                                AllSettings.keywaspressed2 = K_g
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_h]:
                                AllSettings.keywaspressed2 = K_h
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_i]:
                                AllSettings.keywaspressed2 = K_i
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_j]:
                                AllSettings.keywaspressed2 = K_j
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_k]:
                                AllSettings.keywaspressed2 = K_k
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_l]:
                                AllSettings.keywaspressed2 = K_l
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_m]:
                                AllSettings.keywaspressed2 = K_m
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_o]:
                                AllSettings.keywaspressed2 = K_o
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_p]:
                                AllSettings.keywaspressed2 = K_p
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_q]:
                                AllSettings.keywaspressed2 = K_q
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_r]:
                                AllSettings.keywaspressed2 = K_r
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_s]:
                                AllSettings.keywaspressed2 = K_s
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_t]:
                                AllSettings.keywaspressed2 = K_t
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_u]:
                                AllSettings.keywaspressed2 = K_u
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_v]:
                                AllSettings.keywaspressed2 = K_v
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_w]:
                                AllSettings.keywaspressed2 = K_w
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_x]:
                                AllSettings.keywaspressed2 = K_x
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_y]:
                                AllSettings.keywaspressed2 = K_y
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_z]:
                                AllSettings.keywaspressed2 = K_z
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_DELETE]:
                                AllSettings.keywaspressed2 = K_DELETE
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP0]:
                                AllSettings.keywaspressed2 = K_KP0
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP1]:
                                AllSettings.keywaspressed2 = K_KP1
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP2]:
                                AllSettings.keywaspressed2 = K_KP2
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP3]:
                                AllSettings.keywaspressed2 = K_KP3
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP4]:
                                AllSettings.keywaspressed2 = K_KP4
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP5]:
                                AllSettings.keywaspressed2 = K_KP5
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP6]:
                                AllSettings.keywaspressed2 = K_KP6
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP7]:
                                AllSettings.keywaspressed2 = K_KP7
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP8]:
                                AllSettings.keywaspressed2 = K_KP8
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP9]:
                                AllSettings.keywaspressed2 = K_KP9
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP_PERIOD]:
                                AllSettings.keywaspressed2 = K_BACKSPACE
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP_DIVIDE]:
                                AllSettings.keywaspressed2 = K_KP_DIVIDE
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP_MULTIPLY]:
                                AllSettings.keywaspressed2 = K_KP_MULTIPLY
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP_MINUS]:
                                AllSettings.keywaspressed2 = K_KP_MINUS
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP_PLUS]:
                                AllSettings.keywaspressed2 = K_KP_PLUS
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP_ENTER]:
                                AllSettings.keywaspressed2 = K_KP_ENTER
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_KP_EQUALS]:
                                AllSettings.keywaspressed2 = K_KP_EQUALS
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_UP]:
                                AllSettings.keywaspressed2 = K_UP
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_DOWN]:
                                AllSettings.keywaspressed2 = K_DOWN
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_RIGHT]:
                                AllSettings.keywaspressed2 = K_RIGHT
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_LEFT]:
                                AllSettings.keywaspressed2 = K_LEFT
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_INSERT]:
                                AllSettings.keywaspressed2 = K_INSERT
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_HOME]:
                                AllSettings.keywaspressed2 = K_HOME
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_END]:
                                AllSettings.keywaspressed2 = K_END
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_PAGEUP]:
                                AllSettings.keywaspressed2 = K_PAGEUP
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_PAGEDOWN]:
                                AllSettings.keywaspressed2 = K_PAGEDOWN
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F1]:
                                AllSettings.keywaspressed2 = K_F1
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F2]:
                                AllSettings.keywaspressed2 = K_F2
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F3]:
                                AllSettings.keywaspressed2 = K_F3
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F4]:
                                AllSettings.keywaspressed2 = K_F4
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F5]:
                                AllSettings.keywaspressed2 = K_F5
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F6]:
                                AllSettings.keywaspressed2 = K_F6
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F7]:
                                AllSettings.keywaspressed2 = K_F7
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F8]:
                                AllSettings.keywaspressed2 = K_F8
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F9]:
                                AllSettings.keywaspressed2 = K_F9
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F10]:
                                AllSettings.keywaspressed2 = K_F10
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F11]:
                                AllSettings.keywaspressed2 = K_F11
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F12]:
                                AllSettings.keywaspressed2 = K_F12
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F13]:
                                AllSettings.keywaspressed2 = K_F13
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F14]:
                                AllSettings.keywaspressed2 = K_F14
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_F15]:
                                AllSettings.keywaspressed2 = K_F15
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_NUMLOCK]:
                                AllSettings.keywaspressed2 = K_NUMLOCK
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_CAPSLOCK]:
                                AllSettings.keywaspressed2 = K_CAPSLOCK
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_SCROLLOCK]:
                                AllSettings.keywaspressed2 = K_SCROLLOCK
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_RSHIFT]:
                                AllSettings.keywaspressed2 = K_RSHIFT
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_LSHIFT]:
                                AllSettings.keywaspressed2 = K_LSHIFT
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_RCTRL]:
                                AllSettings.keywaspressed2 = K_RCTRL
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_LCTRL]:
                                AllSettings.keywaspressed2 = K_LCTRL
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_RALT]:
                                AllSettings.keywaspressed2 = K_RALT
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_LALT]:
                                AllSettings.keywaspressed2 = K_LALT
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_RMETA]:
                                AllSettings.keywaspressed2 = K_RMETA
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_LMETA]:
                                AllSettings.keywaspressed2 = K_LMETA
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_LSUPER]:
                                AllSettings.keywaspressed2 = K_LSUPER
                                AllSettings.startinput2 = False
                            if pygame.key.get_pressed()[K_RSUPER]:
                                AllSettings.keywaspressed2 = K_RSUPER
                                AllSettings.startinput2 = False
                font2 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
                textinput2 = font2.render(pygame.key.name(AllSettings.keywaspressed2), True, AllSettings.Yellow)
                AllSettings.DISPLAY.blit(textinput2,(910,370))

            
                if AllSettings.startinput3 == True:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                AllSettings.keywaspressed3 = K_BACKSPACE
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_TAB]:
                                AllSettings.keywaspressed3 = K_TAB
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_CLEAR]:
                                AllSettings.keywaspressed3 = K_CLEAR
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_RETURN]:
                                AllSettings.keywaspressed3 = K_RETURN
                                AllSettings.startinput3 = False  
                            if pygame.key.get_pressed()[K_PAUSE]:
                                AllSettings.keywaspressed3 = K_PAUSE
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_ESCAPE]:
                                AllSettings.keywaspressed3 = K_ESCAPE
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_SPACE]:
                                AllSettings.keywaspressed3 = K_SPACE
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_EXCLAIM]:
                                AllSettings.keywaspressed3 = K_EXCLAIM
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_QUOTEDBL]:
                                AllSettings.keywaspressed3 = K_QUOTEDBL
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_HASH]:
                                AllSettings.keywaspressed3 = K_HASH
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_DOLLAR]:
                                AllSettings.keywaspressed3 = K_DOLLAR
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_AMPERSAND]:
                                AllSettings.keywaspressed3 = K_AMPERSAND
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_QUOTE]:
                                AllSettings.keywaspressed3 = K_QUOTE
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_LEFTPAREN]:
                                AllSettings.keywaspressed3 = K_LEFTPAREN
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_RIGHTPAREN]:
                                AllSettings.keywaspressed3 = K_RIGHTPAREN
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_ASTERISK]:
                                AllSettings.keywaspressed3 = K_ASTERISK
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_PLUS]:
                                AllSettings.keywaspressed3 = K_PLUS
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_COMMA]:
                                AllSettings.keywaspressed3 = K_COMMA
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_MINUS]:
                                AllSettings.keywaspressed3 = K_MINUS
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_PERIOD]:
                                AllSettings.keywaspressed3 = K_PERIOD
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_SLASH]:
                                AllSettings.keywaspressed3 = K_SLASH
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_0]:
                                AllSettings.keywaspressed3 = K_0
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_1]:
                                AllSettings.keywaspressed3 = K_1
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_2]:
                                AllSettings.keywaspressed3 = K_2
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_3]:
                                AllSettings.keywaspressed3 = K_3
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_4]:
                                AllSettings.keywaspressed3 = K_4
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_5]:
                                AllSettings.keywaspressed3 = K_5
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_6]:
                                AllSettings.keywaspressed3 = K_6
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_7]:
                                AllSettings.keywaspressed3 = K_7
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_8]:
                                AllSettings.keywaspressed3 = K_8
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_9]:
                                AllSettings.keywaspressed3 = K_9
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_COLON]:
                                AllSettings.keywaspressed3 = K_COLON
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_SEMICOLON]:
                                AllSettings.keywaspressed3 = K_SEMICOLON
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_LESS]:
                                AllSettings.keywaspressed3 = K_LESS
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_EQUALS]:
                                AllSettings.keywaspressed3 = K_EQUALS
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_GREATER]:
                                AllSettings.keywaspressed3 = K_GREATER
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_QUESTION]:
                                AllSettings.keywaspressed3 = K_QUESTION
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_AT]:
                                AllSettings.keywaspressed3 = K_AT
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_LEFTBRACKET]:
                                AllSettings.keywaspressed3 = K_LEFTBRACKET
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_BACKSLASH]:
                                AllSettings.keywaspressed3 = K_BACKSLASH
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_RIGHTBRACKET]:
                                AllSettings.keywaspressed3 = K_RIGHTBRACKET
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_CARET]:
                                AllSettings.keywaspressed3 = K_CARET
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_UNDERSCORE]:
                                AllSettings.keywaspressed3 = K_UNDERSCORE
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_BACKQUOTE]:
                                AllSettings.keywaspressed3 = K_BACKQUOTE
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_a]:
                                AllSettings.keywaspressed3 = K_a
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_b]:
                                AllSettings.keywaspressed3 = K_b
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_c]:
                                AllSettings.keywaspressed3 = K_c
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_d]:
                                AllSettings.keywaspressed3 = K_d
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_e]:
                                AllSettings.keywaspressed3 = K_e
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_f]:
                                AllSettings.keywaspressed3 = K_f
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_g]:
                                AllSettings.keywaspressed3 = K_g
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_h]:
                                AllSettings.keywaspressed3 = K_h
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_i]:
                                AllSettings.keywaspressed3 = K_i
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_j]:
                                AllSettings.keywaspressed3 = K_j
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_k]:
                                AllSettings.keywaspressed3 = K_k
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_l]:
                                AllSettings.keywaspressed3 = K_l
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_m]:
                                AllSettings.keywaspressed3 = K_m
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_o]:
                                AllSettings.keywaspressed3 = K_o
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_p]:
                                AllSettings.keywaspressed3 = K_p
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_q]:
                                AllSettings.keywaspressed3 = K_q
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_r]:
                                AllSettings.keywaspressed3 = K_r
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_s]:
                                AllSettings.keywaspressed3 = K_s
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_t]:
                                AllSettings.keywaspressed3 = K_t
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_u]:
                                AllSettings.keywaspressed3 = K_u
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_v]:
                                AllSettings.keywaspressed3 = K_v
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_w]:
                                AllSettings.keywaspressed3 = K_w
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_x]:
                                AllSettings.keywaspressed3 = K_x
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_y]:
                                AllSettings.keywaspressed3 = K_y
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_z]:
                                AllSettings.keywaspressed3 = K_z
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_DELETE]:
                                AllSettings.keywaspressed3 = K_DELETE
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP0]:
                                AllSettings.keywaspressed3 = K_KP0
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP1]:
                                AllSettings.keywaspressed3 = K_KP1
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP2]:
                                AllSettings.keywaspressed3 = K_KP2
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP3]:
                                AllSettings.keywaspressed3 = K_KP3
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP4]:
                                AllSettings.keywaspressed3 = K_KP4
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP5]:
                                AllSettings.keywaspressed3 = K_KP5
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP6]:
                                AllSettings.keywaspressed3 = K_KP6
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP7]:
                                AllSettings.keywaspressed3 = K_KP7
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP8]:
                                AllSettings.keywaspressed3 = K_KP8
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP9]:
                                AllSettings.keywaspressed3 = K_KP9
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP_PERIOD]:
                                AllSettings.keywaspressed3 = K_BACKSPACE
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP_DIVIDE]:
                                AllSettings.keywaspressed3 = K_KP_DIVIDE
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP_MULTIPLY]:
                                AllSettings.keywaspressed3 = K_KP_MULTIPLY
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP_MINUS]:
                                AllSettings.keywaspressed3 = K_KP_MINUS
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP_PLUS]:
                                AllSettings.keywaspressed3 = K_KP_PLUS
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP_ENTER]:
                                AllSettings.keywaspressed3 = K_KP_ENTER
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_KP_EQUALS]:
                                AllSettings.keywaspressed3 = K_KP_EQUALS
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_UP]:
                                AllSettings.keywaspressed3 = K_UP
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_DOWN]:
                                AllSettings.keywaspressed3 = K_DOWN
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_RIGHT]:
                                AllSettings.keywaspressed3 = K_RIGHT
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_LEFT]:
                                AllSettings.keywaspressed3 = K_LEFT
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_INSERT]:
                                AllSettings.keywaspressed3 = K_INSERT
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_HOME]:
                                AllSettings.keywaspressed3 = K_HOME
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_END]:
                                AllSettings.keywaspressed3 = K_END
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_PAGEUP]:
                                AllSettings.keywaspressed3 = K_PAGEUP
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_PAGEDOWN]:
                                AllSettings.keywaspressed3 = K_PAGEDOWN
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F1]:
                                AllSettings.keywaspressed3 = K_F1
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F2]:
                                AllSettings.keywaspressed3 = K_F2
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F3]:
                                AllSettings.keywaspressed3 = K_F3
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F4]:
                                AllSettings.keywaspressed3 = K_F4
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F5]:
                                AllSettings.keywaspressed3 = K_F5
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F6]:
                                AllSettings.keywaspressed3 = K_F6
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F7]:
                                AllSettings.keywaspressed3 = K_F7
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F8]:
                                AllSettings.keywaspressed3 = K_F8
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F9]:
                                AllSettings.keywaspressed3 = K_F9
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F10]:
                                AllSettings.keywaspressed3 = K_F10
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F11]:
                                AllSettings.keywaspressed3 = K_F11
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F12]:
                                AllSettings.keywaspressed3 = K_F12
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F13]:
                                AllSettings.keywaspressed3 = K_F13
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F14]:
                                AllSettings.keywaspressed3 = K_F14
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_F15]:
                                AllSettings.keywaspressed3 = K_F15
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_NUMLOCK]:
                                AllSettings.keywaspressed3 = K_NUMLOCK
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_CAPSLOCK]:
                                AllSettings.keywaspressed3 = K_CAPSLOCK
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_SCROLLOCK]:
                                AllSettings.keywaspressed3 = K_SCROLLOCK
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_RSHIFT]:
                                AllSettings.keywaspressed3 = K_RSHIFT
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_LSHIFT]:
                                AllSettings.keywaspressed3 = K_LSHIFT
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_RCTRL]:
                                AllSettings.keywaspressed3 = K_RCTRL
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_LCTRL]:
                                AllSettings.keywaspressed3 = K_LCTRL
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_RALT]:
                                AllSettings.keywaspressed3 = K_RALT
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_LALT]:
                                AllSettings.keywaspressed3 = K_LALT
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_RMETA]:
                                AllSettings.keywaspressed3 = K_RMETA
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_LMETA]:
                                AllSettings.keywaspressed3 = K_LMETA
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_LSUPER]:
                                AllSettings.keywaspressed3 = K_LSUPER
                                AllSettings.startinput3 = False
                            if pygame.key.get_pressed()[K_RSUPER]:
                                AllSettings.keywaspressed3 = K_RSUPER
                                AllSettings.startinput3 = False
                font3 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
                textinput3 = font3.render(pygame.key.name(AllSettings.keywaspressed3), True, AllSettings.Yellow)
                AllSettings.DISPLAY.blit(textinput3,(910,470))

                pygame.display.update() 
                if back == True:
                    AllSettings.DISPLAY.blit(AllSettings.background, (0, 0))

                    break
                if AllSettings.breakcontrol == True:
                    AllSettings.DISPLAY.blit(AllSettings.background, (0, 0))

                    break
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
                Menu.SettingsMenu(self)

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
        global soundm
        soundm = False
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                soundm = True
                Menu.Soundmenu(self)

        return soundm

class SoundSettings1():
    def __init__(self):
        self.image = AllSettings.Sound
        self.rect = self.image.get_rect()
        self.rect.x = 188
        self.rect.y = 134
    def draw(self):
        global soundm,breakvideo,breakcontrol
        soundm = False
        breakvideo = False
        breakcontrol = False
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                soundm = True
                breakvideo = True
                breakcontrol = True

        return soundm,breakvideo,breakcontrol


class VideoSettings():
    def __init__(self):
        self.image = AllSettings.Video
        self.rect = self.image.get_rect()
        self.rect.x = 517
        self.rect.y = 134
    def draw(self):
        global vidsettings,breakcontrol
        vidsettings = False
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                vidsettings = True
                breakcontrol = True
                Menu.VideoSettings(self)

        return vidsettings

class VideoSettings1():
    def __init__(self):
        self.image = AllSettings.Video
        self.rect = self.image.get_rect()
        self.rect.x = 517
        self.rect.y = 134
    def draw(self):
        global vidsettings,breaksound
        breaksound = False
        vidsettings = False
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                vidsettings = True
                breaksound = True

        return vidsettings



class ControlsSettings():
    def __init__(self):
        self.image = AllSettings.Controls
        self.rect = self.image.get_rect()
        self.rect.x = 823
        self.rect.y = 134
    def draw(self):
        global control,breaksound
        pos = pygame.mouse.get_pos()
        control = False
        breaksound = False
        AllSettings.DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                control = True
                breaksound = True
                Menu.Conntrolmenu(self)

        return control,breaksound 

class backSettingsMenu():
    def __init__(self):
        self.image = AllSettings.Back
        self.rect = self.image.get_rect()
        self.rect.x = 967
        self.rect.y = 566 
    def draw(self):
        global back
        back = False
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                back = True

        return back

class Soundback():
    def __init__(self):
        self.image = AllSettings.Back
        self.rect = self.image.get_rect()
        self.rect.x = 967
        self.rect.y = 566 
    def draw(self):
        global back
        back = False
        pos = pygame.mouse.get_pos()
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                back = True

        return back


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
SettingsSound1 = SoundSettings1()
SettingsVideo = VideoSettings()
SettingsVideo1 = VideoSettings1()
SettingsControls = ControlsSettings()
SettingsBack = backSettingsMenu()
SoundBack = Soundback()
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
