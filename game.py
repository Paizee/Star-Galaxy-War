from ast import Starred
from cgitb import text
from glob import glob
import locale
from re import S, X
import re
from tkinter.tix import Tree
from turtle import textinput, width
from pygame_menu.widgets.core.widget import Widget
from pygame_menu.widgets.core.selection import Selection
import pygame.gfxdraw
import time
import pygame_menu
import sys, pygame, pygame.mixer
from pygame.locals import *
import os
import random
pygame.init()
screen_height = 720
screen_width = 1281
DISPLAY=pygame.display.set_mode((screen_width,screen_height),0,64)
pygame.display.set_caption("Pilot Galaxy2 War")
# settings
FPS  = 60
WHITE=(255,255,255)
BLUE=(0,0,255)
Yellow =(196,191,47)
Orange = (179,87,16)
Red = (149,12,12)
Lightgrey = (114,114,114)
Green = (7,149,26)
Black = (0,0,0)

background = pygame.image.load(os.path.join("data/images","background.png")).convert()
speedl = 5
speedr = 5
speedt = 5
speedb = 5
Bullets_vel = 6
xplayer = 350
yplayer = 500
playerimage = pygame.image.load(os.path.join("data/images", "x-wing.png"))
playerimage = pygame.transform.scale(playerimage,(128,128))
enemieimage = pygame.image.load(os.path.join("data/images", "tiefighter.png"))
enemieimage = pygame.transform.scale(enemieimage,(96,96))
laserbullet = pygame.image.load(os.path.join("data/images","bullet.png")).convert_alpha()
laserbullet = pygame.transform.smoothscale(laserbullet,(24,24))
laserbullet = pygame.transform.rotate(laserbullet, angle=90)
shot = pygame.mixer.Sound(os.path.join("data/sounds", "shot.wav"))
explosion = pygame.image.load(os.path.join("data/images", "explosion.png"))
explosion = pygame.transform.scale(explosion,(90,90))
explosound= pygame.mixer.Sound(os.path.join("data/sounds", "explosion.wav"))
bulletred = pygame.image.load(os.path.join("data/images","bulletback.png"))
bulletred = pygame.transform.smoothscale(bulletred,(24,24))
bulletred= pygame.transform.rotate(bulletred, angle=90)
butsettings = pygame.image.load(os.path.join("data/images", "Settings.png"))
butsettings = pygame.transform.smoothscale(butsettings,(350,100))
butContinue = pygame.image.load(os.path.join("data/images", "Continue.png"))
butContinue = pygame.transform.smoothscale(butContinue,(350,100))
butMenu = pygame.image.load(os.path.join("data/images", "Menu .png"))
butMenu = pygame.transform.smoothscale(butMenu,(350,100))
Settingsmenu = pygame.image.load(os.path.join("data/images", "Settingsmenu.png"))
Back = pygame.image.load(os.path.join("data/images", "Back.png"))
Sound = pygame.image.load(os.path.join("data/images", "Sound.png"))
Video = pygame.image.load(os.path.join("data/images", "Video.png"))
Controls = pygame.image.load(os.path.join("data/images", "Controls.png"))
lightswordsound = pygame.image.load(os.path.join("data/images","lightsword.png"))
lightswordsound = pygame.transform.rotate(lightswordsound,-90)
lightswordsound = pygame.transform.scale(lightswordsound,(300,250))
plus = pygame.image.load(os.path.join("data/images","plus.png"))
minus = pygame.image.load(os.path.join("data/images","minus.png"))
volumepng = pygame.image.load(os.path.join("data/images", "volume.png"))
music = pygame.mixer.Sound(os.path.join("data/sounds","music.wav"))
musicpng = pygame.image.load(os.path.join("data/images","music.png"))
plus1 = pygame.image.load(os.path.join("data/images","plus.png"))
minus1 = pygame.image.load(os.path.join("data/images","minus.png"))
reso = pygame.image.load(os.path.join("data/images", "Resolution.png"))
zeile = pygame.image.load(os.path.join("data/images", "zeile.png"))
rahmen = pygame.image.load(os.path.join("data/images","rahmen.png"))
xkasten = pygame.image.load(os.path.join("data/images", "xkasten.png"))
xohnekasten = pygame.image.load(os.path.join("data/images", "xohnekasten.png"))
Fullscreenpng = pygame.image.load(os.path.join("data/images", "Fullscreen.png"))
keyspng = pygame.image.load(os.path.join("data/images","Keys.png"))
shootpng = pygame.image.load(os.path.join("data/images","shoot.png"))
moverightpng = pygame.image.load(os.path.join("data/images","Moveright.png"))
moveleftpng = pygame.image.load(os.path.join("data/images","Moveleft.png"))
keyinputpng = pygame.image.load(os.path.join("data/images","keyinput.png"))
settingspng = pygame.image.load(os.path.join("data/images","settingstextpng.png"))





barPos      = (screen_width/1.16, screen_height/1.15)
barSize     = (100, 15)
borderColor = (Lightgrey)
barColor    = (Red)
max_a = 4


barPos2      = (screen_width/15, screen_height/1.15)
barSize2     = (100, 15)
borderColor2 = (Lightgrey)
barColor2    = (Green)
max_a2 = 15




Playername = "Player"
enemiename = "TieFighter"
all_sprites_list = pygame.sprite.Group()
explosion_list = pygame.sprite.Group()
enemie_list = pygame.sprite.Group()
enemie_list2 = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
bulletback_list = pygame.sprite.Group()
player_list = pygame.sprite.GroupSingle()
clock = pygame.time.Clock()
bol = False
Settings = True
rahmenmenu = False
Apply = False
coins = 0
toggofull = False
keywaspressed = K_SPACE
keywaspressed1 = K_a
keywaspressed2 = K_d
keywaspressed3 = K_ESCAPE
startinput = False
startinput1 = False
startinput2 = False
startinput3 = False
toggofull2 = 0
closerahmen = 0
rand = random.randrange(10,17)
dur = 60
volume = 100
musicvolume = 100
reso1 = "1680 x 1050"
reso2 = "1280 x 1024"
reso3 = "720  x  1280"
reso4 = "640  x  480"



class Enemie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global tfx,tfy,Health
 
        self.image = enemieimage
        self.rect = self.image.get_rect()
        tfx = random.randrange(screen_width)
        tfy = random.randrange(screen_height/1.5)
        self.rect.x = tfx
        self.rect.y = tfy
        numsx = [2,-2]
        self.speedx = random.choice(numsx)
        numsy = [-1,1]
        self.speedy = random.choice(numsy)
        Health = 4
    
    def shootback():
        for enemies in enemie_list:
            bulletback = Bulletback(enemies.rect.center)
            all_sprites_list.add(bulletback)
            bulletback_list.add(bulletback)

    def update(self):

        tfy = self.rect.y
        tfx = self.rect.x 
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x > screen_width - 90:
            self.speedx = -2
        if self.rect.x < 0:
            self.speedx = +2
        if self.rect.y > screen_height/5:
            self.speedy = -1
        if self.rect.y < 5:
            self.speedy = +1

    def DrawBar(pos, size, borderC, barC, progress):
        pygame.draw.rect(DISPLAY, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+3, pos[1]+3)
        innerSize = ((size[0]-6) * progress, size[1]-6)
        pygame.draw.rect(DISPLAY, barC, (*innerPos, *innerSize))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global PlayerHealth

        self.image = playerimage
        self.rect = self.image.get_rect()
        self.rect.y = screen_height - 150
        self.speedx = 0
        self.rect.x = screen_width/2
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
        PlayerHealth = 15

    def update(self):
        global playerx,playery,pauseon,run
        if keys[keywaspressed1]:
            self.rect.x  -=7
        elif keys[keywaspressed2]:
            self.rect.x  +=7
        if keys[keywaspressed]:
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown:
                self.last = now
                player.shoot()
                shot.play()
        if keys[keywaspressed3]:
            run = False
            Menu.Menu(self)

            
        
        playerx = self.rect.x
        playery = self.rect.y
        if self.rect.x > screen_width - 125:
            self.rect.x = screen_width - 125
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet()
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)
    
    def DrawBar(pos2, size2, borderC2, barC2, progress2):
        pygame.draw.rect(DISPLAY, borderC2, (*pos2, *size2), 1)
        innerPos  = (pos2[0]+3, pos2[1]+3)
        innerSize = ((size2[0]-6) * progress2, size2[1]-6)
        pygame.draw.rect(DISPLAY, barC2, (*innerPos, *innerSize))

class Menu():
    def Menu(self):
        if run == False:
            while True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        exit()

                Menusbutton.draw()
                Settingsbutton.draw()
                Continuebutton.draw()





                pygame.display.flip()
                if run == True:
                    break
        

    def SettingsMenu(self):
        if Settings == True:
            while True: 
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        exit()

                Settingmenu.draw()
                SettingsSound.draw()
                SettingsVideo.draw()
                SettingsControls.draw()
                SettingsBack.draw()
                pygame.display.flip()
                if back == True:
                    DISPLAY.blit(background, (0, 0))
                    DISPLAY.blit(textcoin,(screen_height/2.20,screen_width/2.5))
                    DISPLAY.blit(textenemie,(screen_width*1.6, screen_height/2.05))
                    DISPLAY.blit(Playerhealth,(screen_width/13, screen_height/2.05))

                    Enemie.DrawBar(barPos, barSize, borderColor, barColor, Health/max_a)
                    Player.DrawBar(barPos2, barSize2, borderColor2, barColor2, PlayerHealth/max_a2)







                    all_sprites_list.draw(DISPLAY)
                    
                    break
    def Soundmenu(self):
        global soundm,breaksound
        if soundm == True:
            while True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        exit()

                plus2.draw()
                minus2.draw()
                plus3.draw()
                minus3.draw()
                SettingsVideo1.draw()
                SettingsControls.draw()
                SoundBack.draw()
                Volumepng.draw()
                Musicpng.draw()
                if volume == 0:
                    s10 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(620,211,20,40),border_radius=10)
                    s9 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(655,211,20,40),border_radius=10)
                    s8 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(690,211,20,40),border_radius=10)
                    s7 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(725,211,20,40),border_radius=10)
                    s6 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(760,211,20,40),border_radius=10)
                    s5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,211,20,40),border_radius=10)
                    s4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,211,20,40),border_radius=10)
                    s3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,211,20,40),border_radius=10)
                    s2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,211,20,40),border_radius=10)
                    s1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,211,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25)) 
                if volume == 10:
                    s9 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(655,211,20,40),border_radius=10)
                    s8 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(690,211,20,40),border_radius=10)
                    s7 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(725,211,20,40),border_radius=10)
                    s6 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(760,211,20,40),border_radius=10)
                    s5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,211,20,40),border_radius=10)
                    s4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,211,20,40),border_radius=10)
                    s3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,211,20,40),border_radius=10)
                    s2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,211,20,40),border_radius=10)
                    s1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,211,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25))                  
                if volume == 20:
                    s8 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(690,211,20,40),border_radius=10)
                    s7 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(725,211,20,40),border_radius=10)
                    s6 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(760,211,20,40),border_radius=10)
                    s5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,211,20,40),border_radius=10)
                    s4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,211,20,40),border_radius=10)
                    s3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,211,20,40),border_radius=10)
                    s2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,211,20,40),border_radius=10)
                    s1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,211,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25))  
                if volume == 30:
                    s7 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(725,211,20,40),border_radius=10)
                    s6 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(760,211,20,40),border_radius=10)
                    s5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,211,20,40),border_radius=10)
                    s4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,211,20,40),border_radius=10)
                    s3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,211,20,40),border_radius=10)
                    s2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,211,20,40),border_radius=10)
                    s1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,211,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25))     
                if volume == 40:
                    s6 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(760,211,20,40),border_radius=10)
                    s5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,211,20,40),border_radius=10)
                    s4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,211,20,40),border_radius=10)
                    s3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,211,20,40),border_radius=10)
                    s2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,211,20,40),border_radius=10)
                    s1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,211,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25))
                if volume == 50:
                    s5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,211,20,40),border_radius=10)
                    s4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,211,20,40),border_radius=10)
                    s3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,211,20,40),border_radius=10)
                    s2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,211,20,40),border_radius=10)
                    s1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,211,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25))
                if volume == 60:
                    s4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,211,20,40),border_radius=10)
                    s3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,211,20,40),border_radius=10)
                    s2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,211,20,40),border_radius=10)
                    s1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,211,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25)) 
                if volume == 70:
                    s3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,211,20,40),border_radius=10)
                    s2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,211,20,40),border_radius=10)
                    s1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,211,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25))    
                if volume == 80:
                    s2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,211,20,40),border_radius=10)
                    s1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,211,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25))
                if volume == 90:
                    s1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,211,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25))
                if volume == 100:
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,260,60,25))


                shot.set_volume(volume/100)
                explosound.set_volume(volume/100)
                music.set_volume(musicvolume/100)

                if musicvolume == 0:
                    m10 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(620,295,20,40),border_radius=10)
                    m9 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(655,295,20,40),border_radius=10)
                    m8 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(690,295,20,40),border_radius=10)
                    m7 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(725,295,20,40),border_radius=10)
                    m6 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(760,295,20,40),border_radius=10)
                    m5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,295,20,40),border_radius=10)
                    m4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,295,20,40),border_radius=10)
                    m3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,295,20,40),border_radius=10)
                    m2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,295,20,40),border_radius=10)
                    m1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,295,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25)) 
                if musicvolume == 10:
                    m9 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(655,295,20,40),border_radius=10)
                    m8 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(690,295,20,40),border_radius=10)
                    m7 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(725,295,20,40),border_radius=10)
                    m6 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(760,295,20,40),border_radius=10)
                    m5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,295,20,40),border_radius=10)
                    m4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,295,20,40),border_radius=10)
                    m3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,295,20,40),border_radius=10)
                    m2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,295,20,40),border_radius=10)
                    m1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,295,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25))                  
                if musicvolume == 20:
                    m8 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(690,295,20,40),border_radius=10)
                    m7 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(725,295,20,40),border_radius=10)
                    m6 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(760,295,20,40),border_radius=10)
                    m5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,295,20,40),border_radius=10)
                    m4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,295,20,40),border_radius=10)
                    m3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,295,20,40),border_radius=10)
                    m2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,295,20,40),border_radius=10)
                    m1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,295,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25))  
                if musicvolume == 30:
                    m7 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(725,295,20,40),border_radius=10)
                    m6 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(760,295,20,40),border_radius=10)
                    m5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,295,20,40),border_radius=10)
                    m4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,295,20,40),border_radius=10)
                    m3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,295,20,40),border_radius=10)
                    m2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,295,20,40),border_radius=10)
                    m1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,295,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25))     
                if musicvolume == 40:
                    m6 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(760,295,20,40),border_radius=10)
                    m5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,295,20,40),border_radius=10)
                    m4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,295,20,40),border_radius=10)
                    m3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,295,20,40),border_radius=10)
                    m2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,295,20,40),border_radius=10)
                    m1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,295,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25))
                if musicvolume == 50:
                    m5 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,295,20,40),border_radius=10)
                    m4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,295,20,40),border_radius=10)
                    m3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,295,20,40),border_radius=10)
                    m2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,295,20,40),border_radius=10)
                    m1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,295,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25))
                if musicvolume == 60:
                    m4 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(830,295,20,40),border_radius=10)
                    m3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,295,20,40),border_radius=10)
                    m2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,295,20,40),border_radius=10)
                    m1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,295,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25)) 
                if musicvolume == 70:
                    m3 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(865,295,20,40),border_radius=10)
                    m2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,295,20,40),border_radius=10)
                    m1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,295,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25))    
                if musicvolume == 80:
                    m2 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(900,295,20,40),border_radius=10)
                    m1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,295,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25))
                if musicvolume == 90:
                    m1 = pygame.draw.rect(DISPLAY,Black,pygame.Rect(935,295,20,40),border_radius=10)
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25))
                if musicvolume == 100:
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(795,340,60,25))


                font_obj2 = pygame.font.Font('freesansbold.ttf', 20)
                Volume2 = font_obj2.render(str(volume) + "%" , True, WHITE)
                DISPLAY.blit(Volume2,(795,260))

                font_obj3 = pygame.font.Font('freesansbold.ttf', 20)
                Volume3 = font_obj3.render(str(musicvolume) + "%" , True, WHITE)
                DISPLAY.blit(Volume3,(795,340))

                          
                pygame.display.update()                        

                s1 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(620,211,20,40),border_radius=10)
                s2 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(655,211,20,40),border_radius=10)
                s3 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(690,211,20,40),border_radius=10)
                s4 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(725,211,20,40),border_radius=10)
                s5 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(760,211,20,40),border_radius=10)
                s6 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(795,211,20,40),border_radius=10)
                s7 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(830,211,20,40),border_radius=10)
                s8 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(865,211,20,40),border_radius=10)
                s9 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(900,211,20,40),border_radius=10)
                s10 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(935,211,20,40),border_radius=10)

                m1 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(620,295,20,40),border_radius=10)
                m2 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(655,295,20,40),border_radius=10)
                m3 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(690,295,20,40),border_radius=10)
                m4 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(725,295,20,40),border_radius=10)
                m5 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(760,295,20,40),border_radius=10)
                m6 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(795,295,20,40),border_radius=10)
                m7 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(830,295,20,40),border_radius=10)
                m8 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(865,295,20,40),border_radius=10)
                m9 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(900,295,20,40),border_radius=10)
                m10 = pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(935,295,20,40),border_radius=10)
                if back == True:
                    DISPLAY.blit(background, (0, 0))
                    DISPLAY.blit(textcoin,(screen_height/2.20,screen_width/2.5))
                    DISPLAY.blit(textenemie,(screen_width*1.6, screen_height/2.05))
                    DISPLAY.blit(Playerhealth,(screen_width/13, screen_height/2.05))

                    Enemie.DrawBar(barPos, barSize, borderColor, barColor, Health/max_a)
                    Player.DrawBar(barPos2, barSize2, borderColor2, barColor2, PlayerHealth/max_a2)

                    all_sprites_list.draw(DISPLAY)
                    
                    break

                if breaksound == True:
                    DISPLAY.blit(background, (0, 0))
                    DISPLAY.blit(textcoin,(screen_height/2.20,screen_width/2.5))
                    DISPLAY.blit(textenemie,(screen_width*1.6, screen_height/2.05))
                    DISPLAY.blit(Playerhealth,(screen_width/13, screen_height/2.05))

                    Enemie.DrawBar(barPos, barSize, borderColor, barColor, Health/max_a)
                    Player.DrawBar(barPos2, barSize2, borderColor2, barColor2, PlayerHealth/max_a2)

                    all_sprites_list.draw(DISPLAY)
                    break
    def VideoSettings(self):
        global reso1,reso2,reso3,reso4,Apply,DISPLAY,closerahmen,screen_height,screen_width,toggofull2,toggofull,soundm
        if vidsettings == True: 
            while True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        exit()
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

                if toggofull == True:
                    DISPLAY.blit(xohnekasten,(805,200))
                if toggofull2 == 2: 
                    toggofull2 = 0
                if toggofull2 == 0:
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(809,203,40,33))

                if rahmenmenu == True:
                    Dropdownrahmen.draw()
                    re1680x1050.draw()
                    re1280x1024.draw()
                    re720x1280.draw()
                    re640x480.draw()
                if closerahmen == 2: 
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(775,335,300,202))
                    closerahmen = 0
                if screen_height == 1920:
                    reso1 = "1680 x 1050"
                    reso2 = "1280 x 1024"
                    reso3 = "1281 x  720"
                    reso4 = "640  x  480 "
                if screen_height == 1680:
                    reso1 = "1920 x 1080"
                    reso2 = "1280 x 1024"
                    reso3 = "1281 x  720"
                    reso4 = "640  x  480 "
                if screen_height == 1281:
                    reso1 = "1920 x 1080"
                    reso2 = "1680 x 1050"
                    reso3 = "1281 x  720"
                    reso4 = "640  x  480 "
                if screen_height == 1280:
                    reso1 = "1920 x 1080"
                    reso2 = "1680 x 1050"
                    reso3 = "1280 x 1024"
                    reso4 = "640  x  480 "
                if screen_height == 640:
                    reso1 = "1920 x 1080"
                    reso2 = "1680 x 1050"
                    reso3 = "1280 x 1024"
                    reso4 = "1281 x  720"



                if Apply == True:
                    DISPLAY=pygame.display.set_mode((screen_width,screen_height),0,32)
                    DISPLAY.blit(background, (0, 0))
                    DISPLAY.blit(textcoin,(screen_height/2.20,screen_width/2.5))
                    DISPLAY.blit(textenemie,(screen_width*1.6, screen_height/2.05))
                    DISPLAY.blit(Playerhealth,(screen_width/13, screen_height/2.05))


                    Enemie.DrawBar(barPos, barSize, borderColor, barColor, Health/max_a)
                    Player.DrawBar(barPos2, barSize2, borderColor2, barColor2, PlayerHealth/max_a2)


                    all_sprites_list.draw(DISPLAY)

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

                if rahmenmenu == True:
                    Dropdownrahmen.draw()
                    re1680x1050.draw()
                    re1280x1024.draw()
                    re720x1280.draw()
                    re640x480.draw()
                if closerahmen == 2: 
                    pygame.draw.rect(DISPLAY,Black,pygame.Rect(775,335,300,202))
                    closerahmen = 0
                if screen_height == 1920:
                    reso1 = "1680 x 1050"
                    reso2 = "1280 x 1024"
                    reso3 = "1281 x  720"
                    reso4 = "640  x  480 "
                if screen_height == 1680:
                    reso1 = "1920 x 1080"
                    reso2 = "1280 x 1024"
                    reso3 = "1281 x  720"
                    reso4 = "640  x  480 "
                if screen_height == 1281:
                    reso1 = "1920 x 1080"
                    reso2 = "1680 x 1050"
                    reso3 = "1281 x  720"
                    reso4 = "640  x  480 "
                if screen_height == 1280:
                    reso1 = "1920 x 1080"
                    reso2 = "1680 x 1050"
                    reso3 = "1280 x 1024"
                    reso4 = "640  x  480 "
                if screen_height == 640:
                    reso1 = "1920 x 1080"
                    reso2 = "1680 x 1050"
                    reso3 = "1280 x 1024"
                    reso4 = "1281 x  720"



                pygame.display.update()  

                if back == True:

                    DISPLAY.blit(background, (0, 0))
                    DISPLAY.blit(textcoin,(screen_height/2.20,screen_width/2.5))
                    DISPLAY.blit(textenemie,(screen_width*1.6, screen_height/2.05))
                    DISPLAY.blit(Playerhealth,(screen_width/13, screen_height/2.05))

                    Enemie.DrawBar(barPos, barSize, borderColor, barColor, Health/max_a)
                    Player.DrawBar(barPos2, barSize2, borderColor2, barColor2, PlayerHealth/max_a2)

                    all_sprites_list.draw(DISPLAY)
                    
                    break

                if breakvideo == True:
                    print(breakvideo)
                    DISPLAY.blit(background, (0, 0))
                    DISPLAY.blit(textcoin,(screen_height/2.20,screen_width/2.5))
                    DISPLAY.blit(textenemie,(screen_width*1.6, screen_height/2.05))
                    DISPLAY.blit(Playerhealth,(screen_width/13, screen_height/2.05))


                    Enemie.DrawBar(barPos, barSize, borderColor, barColor, Health/max_a)
                    Player.DrawBar(barPos2, barSize2, borderColor2, barColor2, PlayerHealth/max_a2)







                    all_sprites_list.draw(DISPLAY)
                    break
    def Conntrolmenu(self):
        global startinput,keywaspressed,startinput1,keywaspressed1,startinput2,keywaspressed2,startinput3,keywaspressed3
        if control == True: 
            while True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        exit()
                
                SettingsBack.draw()
                controlkeydraw.draw()
                controldraw.draw()
                controlkeyinputdraw.draw()
                if startinput == True:
                            print(startinput)
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                keywaspressed = K_BACKSPACE
                                startinput = False
                            if pygame.key.get_pressed()[K_TAB]:
                                keywaspressed = K_TAB
                                startinput = False
                            if pygame.key.get_pressed()[K_CLEAR]:
                                keywaspressed = K_CLEAR
                                startinput = False
                            if pygame.key.get_pressed()[K_RETURN]:
                                keywaspressed = K_RETURN
                                startinput = False  
                            if pygame.key.get_pressed()[K_PAUSE]:
                                keywaspressed = K_PAUSE
                                startinput = False
                            if pygame.key.get_pressed()[K_ESCAPE]:
                                keywaspressed = K_ESCAPE
                                startinput = False
                            if pygame.key.get_pressed()[K_SPACE]:
                                keywaspressed = K_SPACE
                                startinput = False
                            if pygame.key.get_pressed()[K_EXCLAIM]:
                                keywaspressed = K_EXCLAIM
                                startinput = False
                            if pygame.key.get_pressed()[K_QUOTEDBL]:
                                keywaspressed = K_QUOTEDBL
                                startinput = False
                            if pygame.key.get_pressed()[K_HASH]:
                                keywaspressed = K_HASH
                                startinput = False
                            if pygame.key.get_pressed()[K_DOLLAR]:
                                keywaspressed = K_DOLLAR
                                startinput = False
                            if pygame.key.get_pressed()[K_AMPERSAND]:
                                keywaspressed = K_AMPERSAND
                                startinput = False
                            if pygame.key.get_pressed()[K_QUOTE]:
                                keywaspressed = K_QUOTE
                                startinput = False
                            if pygame.key.get_pressed()[K_LEFTPAREN]:
                                keywaspressed = K_LEFTPAREN
                                startinput = False
                            if pygame.key.get_pressed()[K_RIGHTPAREN]:
                                keywaspressed = K_RIGHTPAREN
                                startinput = False
                            if pygame.key.get_pressed()[K_ASTERISK]:
                                keywaspressed = K_ASTERISK
                                startinput = False
                            if pygame.key.get_pressed()[K_PLUS]:
                                keywaspressed = K_PLUS
                                startinput = False
                            if pygame.key.get_pressed()[K_COMMA]:
                                keywaspressed = K_COMMA
                                startinput = False
                            if pygame.key.get_pressed()[K_MINUS]:
                                keywaspressed = K_MINUS
                                startinput = False
                            if pygame.key.get_pressed()[K_PERIOD]:
                                keywaspressed = K_PERIOD
                                startinput = False
                            if pygame.key.get_pressed()[K_SLASH]:
                                keywaspressed = K_SLASH
                                startinput = False
                            if pygame.key.get_pressed()[K_0]:
                                keywaspressed = K_0
                                startinput = False
                            if pygame.key.get_pressed()[K_1]:
                                keywaspressed = K_1
                                startinput = False
                            if pygame.key.get_pressed()[K_2]:
                                keywaspressed = K_2
                                startinput = False
                            if pygame.key.get_pressed()[K_3]:
                                keywaspressed = K_3
                                startinput = False
                            if pygame.key.get_pressed()[K_4]:
                                keywaspressed = K_4
                                startinput = False
                            if pygame.key.get_pressed()[K_5]:
                                keywaspressed = K_5
                                startinput = False
                            if pygame.key.get_pressed()[K_6]:
                                keywaspressed = K_6
                                startinput = False
                            if pygame.key.get_pressed()[K_7]:
                                keywaspressed = K_7
                                startinput = False
                            if pygame.key.get_pressed()[K_8]:
                                keywaspressed = K_8
                                startinput = False
                            if pygame.key.get_pressed()[K_9]:
                                keywaspressed = K_9
                                startinput = False
                            if pygame.key.get_pressed()[K_COLON]:
                                keywaspressed = K_COLON
                                startinput = False
                            if pygame.key.get_pressed()[K_SEMICOLON]:
                                keywaspressed = K_SEMICOLON
                                startinput = False
                            if pygame.key.get_pressed()[K_LESS]:
                                keywaspressed = K_LESS
                                startinput = False
                            if pygame.key.get_pressed()[K_EQUALS]:
                                keywaspressed = K_EQUALS
                                startinput = False
                            if pygame.key.get_pressed()[K_GREATER]:
                                keywaspressed = K_GREATER
                                startinput = False
                            if pygame.key.get_pressed()[K_QUESTION]:
                                keywaspressed = K_QUESTION
                                startinput = False
                            if pygame.key.get_pressed()[K_AT]:
                                keywaspressed = K_AT
                                startinput = False
                            if pygame.key.get_pressed()[K_LEFTBRACKET]:
                                keywaspressed = K_LEFTBRACKET
                                startinput = False
                            if pygame.key.get_pressed()[K_BACKSLASH]:
                                keywaspressed = K_BACKSLASH
                                startinput = False
                            if pygame.key.get_pressed()[K_RIGHTBRACKET]:
                                keywaspressed = K_RIGHTBRACKET
                                startinput = False
                            if pygame.key.get_pressed()[K_CARET]:
                                keywaspressed = K_CARET
                                startinput = False
                            if pygame.key.get_pressed()[K_UNDERSCORE]:
                                keywaspressed = K_UNDERSCORE
                                startinput = False
                            if pygame.key.get_pressed()[K_BACKQUOTE]:
                                keywaspressed = K_BACKQUOTE
                                startinput = False
                            if pygame.key.get_pressed()[K_a]:
                                keywaspressed = K_a
                                startinput = False
                            if pygame.key.get_pressed()[K_b]:
                                keywaspressed = K_b
                                startinput = False
                            if pygame.key.get_pressed()[K_c]:
                                keywaspressed = K_c
                                startinput = False
                            if pygame.key.get_pressed()[K_d]:
                                keywaspressed = K_d
                                startinput = False
                            if pygame.key.get_pressed()[K_e]:
                                keywaspressed = K_e
                                startinput = False
                            if pygame.key.get_pressed()[K_f]:
                                keywaspressed = K_f
                                startinput = False
                            if pygame.key.get_pressed()[K_g]:
                                keywaspressed = K_g
                                startinput = False
                            if pygame.key.get_pressed()[K_h]:
                                keywaspressed = K_h
                                startinput = False
                            if pygame.key.get_pressed()[K_i]:
                                keywaspressed = K_i
                                startinput = False
                            if pygame.key.get_pressed()[K_j]:
                                keywaspressed = K_j
                                startinput = False
                            if pygame.key.get_pressed()[K_k]:
                                keywaspressed = K_k
                                startinput = False
                            if pygame.key.get_pressed()[K_l]:
                                keywaspressed = K_l
                                startinput = False
                            if pygame.key.get_pressed()[K_m]:
                                keywaspressed = K_m
                                startinput = False
                            if pygame.key.get_pressed()[K_o]:
                                keywaspressed = K_o
                                startinput = False
                            if pygame.key.get_pressed()[K_p]:
                                keywaspressed = K_p
                                startinput = False
                            if pygame.key.get_pressed()[K_q]:
                                keywaspressed = K_q
                                startinput = False
                            if pygame.key.get_pressed()[K_r]:
                                keywaspressed = K_r
                                startinput = False
                            if pygame.key.get_pressed()[K_s]:
                                keywaspressed = K_s
                                startinput = False
                            if pygame.key.get_pressed()[K_t]:
                                keywaspressed = K_t
                                startinput = False
                            if pygame.key.get_pressed()[K_u]:
                                keywaspressed = K_u
                                startinput = False
                            if pygame.key.get_pressed()[K_v]:
                                keywaspressed = K_v
                                startinput = False
                            if pygame.key.get_pressed()[K_w]:
                                keywaspressed = K_w
                                startinput = False
                            if pygame.key.get_pressed()[K_x]:
                                keywaspressed = K_x
                                startinput = False
                            if pygame.key.get_pressed()[K_y]:
                                keywaspressed = K_y
                                startinput = False
                            if pygame.key.get_pressed()[K_z]:
                                keywaspressed = K_z
                                startinput = False
                            if pygame.key.get_pressed()[K_DELETE]:
                                keywaspressed = K_DELETE
                                startinput = False
                            if pygame.key.get_pressed()[K_KP0]:
                                keywaspressed = K_KP0
                                startinput = False
                            if pygame.key.get_pressed()[K_KP1]:
                                keywaspressed = K_KP1
                                startinput = False
                            if pygame.key.get_pressed()[K_KP2]:
                                keywaspressed = K_KP2
                                startinput = False
                            if pygame.key.get_pressed()[K_KP3]:
                                keywaspressed = K_KP3
                                startinput = False
                            if pygame.key.get_pressed()[K_KP4]:
                                keywaspressed = K_KP4
                                startinput = False
                            if pygame.key.get_pressed()[K_KP5]:
                                keywaspressed = K_KP5
                                startinput = False
                            if pygame.key.get_pressed()[K_KP6]:
                                keywaspressed = K_KP6
                                startinput = False
                            if pygame.key.get_pressed()[K_KP7]:
                                keywaspressed = K_KP7
                                startinput = False
                            if pygame.key.get_pressed()[K_KP8]:
                                keywaspressed = K_KP8
                                startinput = False
                            if pygame.key.get_pressed()[K_KP9]:
                                keywaspressed = K_KP9
                                startinput = False
                            if pygame.key.get_pressed()[K_KP_PERIOD]:
                                keywaspressed = K_BACKSPACE
                                startinput = False
                            if pygame.key.get_pressed()[K_KP_DIVIDE]:
                                keywaspressed = K_KP_DIVIDE
                                startinput = False
                            if pygame.key.get_pressed()[K_KP_MULTIPLY]:
                                keywaspressed = K_KP_MULTIPLY
                                startinput = False
                            if pygame.key.get_pressed()[K_KP_MINUS]:
                                keywaspressed = K_KP_MINUS
                                startinput = False
                            if pygame.key.get_pressed()[K_KP_PLUS]:
                                keywaspressed = K_KP_PLUS
                                startinput = False
                            if pygame.key.get_pressed()[K_KP_ENTER]:
                                keywaspressed = K_KP_ENTER
                                startinput = False
                            if pygame.key.get_pressed()[K_KP_EQUALS]:
                                keywaspressed = K_KP_EQUALS
                                startinput = False
                            if pygame.key.get_pressed()[K_UP]:
                                keywaspressed = K_UP
                                startinput = False
                            if pygame.key.get_pressed()[K_DOWN]:
                                keywaspressed = K_DOWN
                                startinput = False
                            if pygame.key.get_pressed()[K_RIGHT]:
                                keywaspressed = K_RIGHT
                                startinput = False
                            if pygame.key.get_pressed()[K_LEFT]:
                                keywaspressed = K_LEFT
                                startinput = False
                            if pygame.key.get_pressed()[K_INSERT]:
                                keywaspressed = K_INSERT
                                startinput = False
                            if pygame.key.get_pressed()[K_HOME]:
                                keywaspressed = K_HOME
                                startinput = False
                            if pygame.key.get_pressed()[K_END]:
                                keywaspressed = K_END
                                startinput = False
                            if pygame.key.get_pressed()[K_PAGEUP]:
                                keywaspressed = K_PAGEUP
                                startinput = False
                            if pygame.key.get_pressed()[K_PAGEDOWN]:
                                keywaspressed = K_PAGEDOWN
                                startinput = False
                            if pygame.key.get_pressed()[K_F1]:
                                keywaspressed = K_F1
                                startinput = False
                            if pygame.key.get_pressed()[K_F2]:
                                keywaspressed = K_F2
                                startinput = False
                            if pygame.key.get_pressed()[K_F3]:
                                keywaspressed = K_F3
                                startinput = False
                            if pygame.key.get_pressed()[K_F4]:
                                keywaspressed = K_F4
                                startinput = False
                            if pygame.key.get_pressed()[K_F5]:
                                keywaspressed = K_F5
                                startinput = False
                            if pygame.key.get_pressed()[K_F6]:
                                keywaspressed = K_F6
                                startinput = False
                            if pygame.key.get_pressed()[K_F7]:
                                keywaspressed = K_F7
                                startinput = False
                            if pygame.key.get_pressed()[K_F8]:
                                keywaspressed = K_F8
                                startinput = False
                            if pygame.key.get_pressed()[K_F9]:
                                keywaspressed = K_F9
                                startinput = False
                            if pygame.key.get_pressed()[K_F10]:
                                keywaspressed = K_F10
                                startinput = False
                            if pygame.key.get_pressed()[K_F11]:
                                keywaspressed = K_F11
                                startinput = False
                            if pygame.key.get_pressed()[K_F12]:
                                keywaspressed = K_F12
                                startinput = False
                            if pygame.key.get_pressed()[K_F13]:
                                keywaspressed = K_F13
                                startinput = False
                            if pygame.key.get_pressed()[K_F14]:
                                keywaspressed = K_F14
                                startinput = False
                            if pygame.key.get_pressed()[K_F15]:
                                keywaspressed = K_F15
                                startinput = False
                            if pygame.key.get_pressed()[K_NUMLOCK]:
                                keywaspressed = K_NUMLOCK
                                startinput = False
                            if pygame.key.get_pressed()[K_CAPSLOCK]:
                                keywaspressed = K_CAPSLOCK
                                startinput = False
                            if pygame.key.get_pressed()[K_SCROLLOCK]:
                                keywaspressed = K_SCROLLOCK
                                startinput = False
                            if pygame.key.get_pressed()[K_RSHIFT]:
                                keywaspressed = K_RSHIFT
                                startinput = False
                            if pygame.key.get_pressed()[K_LSHIFT]:
                                keywaspressed = K_LSHIFT
                                startinput = False
                            if pygame.key.get_pressed()[K_RCTRL]:
                                keywaspressed = K_RCTRL
                                startinput = False
                            if pygame.key.get_pressed()[K_LCTRL]:
                                keywaspressed = K_LCTRL
                                startinput = False
                            if pygame.key.get_pressed()[K_RALT]:
                                keywaspressed = K_RALT
                                startinput = False
                            if pygame.key.get_pressed()[K_LALT]:
                                keywaspressed = K_LALT
                                startinput = False
                            if pygame.key.get_pressed()[K_RMETA]:
                                keywaspressed = K_RMETA
                                startinput = False
                            if pygame.key.get_pressed()[K_LMETA]:
                                keywaspressed = K_LMETA
                                startinput = False
                            if pygame.key.get_pressed()[K_LSUPER]:
                                keywaspressed = K_LSUPER
                                startinput = False
                            if pygame.key.get_pressed()[K_RSUPER]:
                                keywaspressed = K_RSUPER
                                startinput = False
                font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
                textinput = font.render(pygame.key.name(keywaspressed), True, Yellow)
                DISPLAY.blit(textinput,(910,170))
                if startinput1 == True:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                keywaspressed1 = K_BACKSPACE
                                startinput1 = False
                            if pygame.key.get_pressed()[K_TAB]:
                                keywaspressed1 = K_TAB
                                startinput1 = False
                            if pygame.key.get_pressed()[K_CLEAR]:
                                keywaspressed1 = K_CLEAR
                                startinput1 = False
                            if pygame.key.get_pressed()[K_RETURN]:
                                keywaspressed1 = K_RETURN
                                startinput1 = False  
                            if pygame.key.get_pressed()[K_PAUSE]:
                                keywaspressed1 = K_PAUSE
                                startinput1 = False
                            if pygame.key.get_pressed()[K_ESCAPE]:
                                keywaspressed1 = K_ESCAPE
                                startinput1 = False
                            if pygame.key.get_pressed()[K_SPACE]:
                                keywaspressed1 = K_SPACE
                                startinput1 = False
                            if pygame.key.get_pressed()[K_EXCLAIM]:
                                keywaspressed1 = K_EXCLAIM
                                startinput1 = False
                            if pygame.key.get_pressed()[K_QUOTEDBL]:
                                keywaspressed1 = K_QUOTEDBL
                                startinput1 = False
                            if pygame.key.get_pressed()[K_HASH]:
                                keywaspressed1 = K_HASH
                                startinput1 = False
                            if pygame.key.get_pressed()[K_DOLLAR]:
                                keywaspressed1 = K_DOLLAR
                                startinput1 = False
                            if pygame.key.get_pressed()[K_AMPERSAND]:
                                keywaspressed1 = K_AMPERSAND
                                startinput1 = False
                            if pygame.key.get_pressed()[K_QUOTE]:
                                keywaspressed1 = K_QUOTE
                                startinput1 = False
                            if pygame.key.get_pressed()[K_LEFTPAREN]:
                                keywaspressed1 = K_LEFTPAREN
                                startinput1 = False
                            if pygame.key.get_pressed()[K_RIGHTPAREN]:
                                keywaspressed1 = K_RIGHTPAREN
                                startinput1 = False
                            if pygame.key.get_pressed()[K_ASTERISK]:
                                keywaspressed1 = K_ASTERISK
                                startinput1 = False
                            if pygame.key.get_pressed()[K_PLUS]:
                                keywaspressed1 = K_PLUS
                                startinput1 = False
                            if pygame.key.get_pressed()[K_COMMA]:
                                keywaspressed1 = K_COMMA
                                startinput1 = False
                            if pygame.key.get_pressed()[K_MINUS]:
                                keywaspressed1 = K_MINUS
                                startinput1 = False
                            if pygame.key.get_pressed()[K_PERIOD]:
                                keywaspressed1 = K_PERIOD
                                startinput1 = False
                            if pygame.key.get_pressed()[K_SLASH]:
                                keywaspressed1 = K_SLASH
                                startinput1 = False
                            if pygame.key.get_pressed()[K_0]:
                                keywaspressed1 = K_0
                                startinput1 = False
                            if pygame.key.get_pressed()[K_1]:
                                keywaspressed1 = K_1
                                startinput1 = False
                            if pygame.key.get_pressed()[K_2]:
                                keywaspressed1 = K_2
                                startinput1 = False
                            if pygame.key.get_pressed()[K_3]:
                                keywaspressed1 = K_3
                                startinput1 = False
                            if pygame.key.get_pressed()[K_4]:
                                keywaspressed1 = K_4
                                startinput1 = False
                            if pygame.key.get_pressed()[K_5]:
                                keywaspressed1 = K_5
                                startinput1 = False
                            if pygame.key.get_pressed()[K_6]:
                                keywaspressed1 = K_6
                                startinput1 = False
                            if pygame.key.get_pressed()[K_7]:
                                keywaspressed1 = K_7
                                startinput1 = False
                            if pygame.key.get_pressed()[K_8]:
                                keywaspressed1 = K_8
                                startinput1 = False
                            if pygame.key.get_pressed()[K_9]:
                                keywaspressed1 = K_9
                                startinput1 = False
                            if pygame.key.get_pressed()[K_COLON]:
                                keywaspressed1 = K_COLON
                                startinput1 = False
                            if pygame.key.get_pressed()[K_SEMICOLON]:
                                keywaspressed1 = K_SEMICOLON
                                startinput1 = False
                            if pygame.key.get_pressed()[K_LESS]:
                                keywaspressed1 = K_LESS
                                startinput1 = False
                            if pygame.key.get_pressed()[K_EQUALS]:
                                keywaspressed1 = K_EQUALS
                                startinput1 = False
                            if pygame.key.get_pressed()[K_GREATER]:
                                keywaspressed1 = K_GREATER
                                startinput1 = False
                            if pygame.key.get_pressed()[K_QUESTION]:
                                keywaspressed1 = K_QUESTION
                                startinput1 = False
                            if pygame.key.get_pressed()[K_AT]:
                                keywaspressed1 = K_AT
                                startinput1 = False
                            if pygame.key.get_pressed()[K_LEFTBRACKET]:
                                keywaspressed1 = K_LEFTBRACKET
                                startinput1 = False
                            if pygame.key.get_pressed()[K_BACKSLASH]:
                                keywaspressed1 = K_BACKSLASH
                                startinput1 = False
                            if pygame.key.get_pressed()[K_RIGHTBRACKET]:
                                keywaspressed1 = K_RIGHTBRACKET
                                startinput1 = False
                            if pygame.key.get_pressed()[K_CARET]:
                                keywaspressed1 = K_CARET
                                startinput1 = False
                            if pygame.key.get_pressed()[K_UNDERSCORE]:
                                keywaspressed1 = K_UNDERSCORE
                                startinput1 = False
                            if pygame.key.get_pressed()[K_BACKQUOTE]:
                                keywaspressed1 = K_BACKQUOTE
                                startinput1 = False
                            if pygame.key.get_pressed()[K_a]:
                                keywaspressed1 = K_a
                                startinput1 = False
                            if pygame.key.get_pressed()[K_b]:
                                keywaspressed1 = K_b
                                startinput1 = False
                            if pygame.key.get_pressed()[K_c]:
                                keywaspressed1 = K_c
                                startinput1 = False
                            if pygame.key.get_pressed()[K_d]:
                                keywaspressed1 = K_d
                                startinput1 = False
                            if pygame.key.get_pressed()[K_e]:
                                keywaspressed1 = K_e
                                startinput1 = False
                            if pygame.key.get_pressed()[K_f]:
                                keywaspressed1 = K_f
                                startinput1 = False
                            if pygame.key.get_pressed()[K_g]:
                                keywaspressed1 = K_g
                                startinput1 = False
                            if pygame.key.get_pressed()[K_h]:
                                keywaspressed1 = K_h
                                startinput1 = False
                            if pygame.key.get_pressed()[K_i]:
                                keywaspressed1 = K_i
                                startinput1 = False
                            if pygame.key.get_pressed()[K_j]:
                                keywaspressed1 = K_j
                                startinput1 = False
                            if pygame.key.get_pressed()[K_k]:
                                keywaspressed1 = K_k
                                startinput1 = False
                            if pygame.key.get_pressed()[K_l]:
                                keywaspressed1 = K_l
                                startinput1 = False
                            if pygame.key.get_pressed()[K_m]:
                                keywaspressed1 = K_m
                                startinput1 = False
                            if pygame.key.get_pressed()[K_o]:
                                keywaspressed1 = K_o
                                startinput1 = False
                            if pygame.key.get_pressed()[K_p]:
                                keywaspressed1 = K_p
                                startinput1 = False
                            if pygame.key.get_pressed()[K_q]:
                                keywaspressed1 = K_q
                                startinput1 = False
                            if pygame.key.get_pressed()[K_r]:
                                keywaspressed1 = K_r
                                startinput1 = False
                            if pygame.key.get_pressed()[K_s]:
                                keywaspressed1 = K_s
                                startinput1 = False
                            if pygame.key.get_pressed()[K_t]:
                                keywaspressed1 = K_t
                                startinput1 = False
                            if pygame.key.get_pressed()[K_u]:
                                keywaspressed1 = K_u
                                startinput1 = False
                            if pygame.key.get_pressed()[K_v]:
                                keywaspressed1 = K_v
                                startinput1 = False
                            if pygame.key.get_pressed()[K_w]:
                                keywaspressed1 = K_w
                                startinput1 = False
                            if pygame.key.get_pressed()[K_x]:
                                keywaspressed1 = K_x
                                startinput1 = False
                            if pygame.key.get_pressed()[K_y]:
                                keywaspressed1 = K_y
                                startinput1 = False
                            if pygame.key.get_pressed()[K_z]:
                                keywaspressed1 = K_z
                                startinput1 = False
                            if pygame.key.get_pressed()[K_DELETE]:
                                keywaspressed1 = K_DELETE
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP0]:
                                keywaspressed1 = K_KP0
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP1]:
                                keywaspressed1 = K_KP1
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP2]:
                                keywaspressed1 = K_KP2
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP3]:
                                keywaspressed1 = K_KP3
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP4]:
                                keywaspressed1 = K_KP4
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP5]:
                                keywaspressed1 = K_KP5
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP6]:
                                keywaspressed1 = K_KP6
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP7]:
                                keywaspressed1 = K_KP7
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP8]:
                                keywaspressed1 = K_KP8
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP9]:
                                keywaspressed1 = K_KP9
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP_PERIOD]:
                                keywaspressed1 = K_BACKSPACE
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP_DIVIDE]:
                                keywaspressed1 = K_KP_DIVIDE
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP_MULTIPLY]:
                                keywaspressed1 = K_KP_MULTIPLY
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP_MINUS]:
                                keywaspressed1 = K_KP_MINUS
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP_PLUS]:
                                keywaspressed1 = K_KP_PLUS
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP_ENTER]:
                                keywaspressed1 = K_KP_ENTER
                                startinput1 = False
                            if pygame.key.get_pressed()[K_KP_EQUALS]:
                                keywaspressed1 = K_KP_EQUALS
                                startinput1 = False
                            if pygame.key.get_pressed()[K_UP]:
                                keywaspressed1 = K_UP
                                startinput1 = False
                            if pygame.key.get_pressed()[K_DOWN]:
                                keywaspressed1 = K_DOWN
                                startinput1 = False
                            if pygame.key.get_pressed()[K_RIGHT]:
                                keywaspressed1 = K_RIGHT
                                startinput1 = False
                            if pygame.key.get_pressed()[K_LEFT]:
                                keywaspressed1 = K_LEFT
                                startinput1 = False
                            if pygame.key.get_pressed()[K_INSERT]:
                                keywaspressed1 = K_INSERT
                                startinput1 = False
                            if pygame.key.get_pressed()[K_HOME]:
                                keywaspressed1 = K_HOME
                                startinput1 = False
                            if pygame.key.get_pressed()[K_END]:
                                keywaspressed1 = K_END
                                startinput1 = False
                            if pygame.key.get_pressed()[K_PAGEUP]:
                                keywaspressed1 = K_PAGEUP
                                startinput1 = False
                            if pygame.key.get_pressed()[K_PAGEDOWN]:
                                keywaspressed1 = K_PAGEDOWN
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F1]:
                                keywaspressed1 = K_F1
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F2]:
                                keywaspressed1 = K_F2
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F3]:
                                keywaspressed1 = K_F3
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F4]:
                                keywaspressed1 = K_F4
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F5]:
                                keywaspressed1 = K_F5
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F6]:
                                keywaspressed1 = K_F6
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F7]:
                                keywaspressed1 = K_F7
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F8]:
                                keywaspressed1 = K_F8
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F9]:
                                keywaspressed1 = K_F9
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F10]:
                                keywaspressed1 = K_F10
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F11]:
                                keywaspressed1 = K_F11
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F12]:
                                keywaspressed1 = K_F12
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F13]:
                                keywaspressed1 = K_F13
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F14]:
                                keywaspressed1 = K_F14
                                startinput1 = False
                            if pygame.key.get_pressed()[K_F15]:
                                keywaspressed1 = K_F15
                                startinput1 = False
                            if pygame.key.get_pressed()[K_NUMLOCK]:
                                keywaspressed1 = K_NUMLOCK
                                startinput1 = False
                            if pygame.key.get_pressed()[K_CAPSLOCK]:
                                keywaspressed1 = K_CAPSLOCK
                                startinput1 = False
                            if pygame.key.get_pressed()[K_SCROLLOCK]:
                                keywaspressed1 = K_SCROLLOCK
                                startinput1 = False
                            if pygame.key.get_pressed()[K_RSHIFT]:
                                keywaspressed1 = K_RSHIFT
                                startinput1 = False
                            if pygame.key.get_pressed()[K_LSHIFT]:
                                keywaspressed1 = K_LSHIFT
                                startinput1 = False
                            if pygame.key.get_pressed()[K_RCTRL]:
                                keywaspressed1 = K_RCTRL
                                startinput1 = False
                            if pygame.key.get_pressed()[K_LCTRL]:
                                keywaspressed1 = K_LCTRL
                                startinput1 = False
                            if pygame.key.get_pressed()[K_RALT]:
                                keywaspressed1 = K_RALT
                                startinput1 = False
                            if pygame.key.get_pressed()[K_LALT]:
                                keywaspressed1 = K_LALT
                                startinput1 = False
                            if pygame.key.get_pressed()[K_RMETA]:
                                keywaspressed1 = K_RMETA
                                startinput1 = False
                            if pygame.key.get_pressed()[K_LMETA]:
                                keywaspressed1 = K_LMETA
                                startinput1 = False
                            if pygame.key.get_pressed()[K_LSUPER]:
                                keywaspressed1 = K_LSUPER
                                startinput1 = False
                            if pygame.key.get_pressed()[K_RSUPER]:
                                keywaspressed1 = K_RSUPER
                                startinput1 = False
                font1 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
                textinput1 = font1.render(pygame.key.name(keywaspressed1), True, Yellow)
                DISPLAY.blit(textinput1,(910,270))

                if startinput2 == True:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                keywaspressed2 = K_BACKSPACE
                                startinput2 = False
                            if pygame.key.get_pressed()[K_TAB]:
                                keywaspressed2 = K_TAB
                                startinput2 = False
                            if pygame.key.get_pressed()[K_CLEAR]:
                                keywaspressed2 = K_CLEAR
                                startinput2 = False
                            if pygame.key.get_pressed()[K_RETURN]:
                                keywaspressed2 = K_RETURN
                                startinput2 = False  
                            if pygame.key.get_pressed()[K_PAUSE]:
                                keywaspressed2 = K_PAUSE
                                startinput2 = False
                            if pygame.key.get_pressed()[K_ESCAPE]:
                                keywaspressed2 = K_ESCAPE
                                startinput2 = False
                            if pygame.key.get_pressed()[K_SPACE]:
                                keywaspressed2 = K_SPACE
                                startinput2 = False
                            if pygame.key.get_pressed()[K_EXCLAIM]:
                                keywaspressed2 = K_EXCLAIM
                                startinput2 = False
                            if pygame.key.get_pressed()[K_QUOTEDBL]:
                                keywaspressed2 = K_QUOTEDBL
                                startinput2 = False
                            if pygame.key.get_pressed()[K_HASH]:
                                keywaspressed2 = K_HASH
                                startinput2 = False
                            if pygame.key.get_pressed()[K_DOLLAR]:
                                keywaspressed2 = K_DOLLAR
                                startinput2 = False
                            if pygame.key.get_pressed()[K_AMPERSAND]:
                                keywaspressed2 = K_AMPERSAND
                                startinput2 = False
                            if pygame.key.get_pressed()[K_QUOTE]:
                                keywaspressed2 = K_QUOTE
                                startinput2 = False
                            if pygame.key.get_pressed()[K_LEFTPAREN]:
                                keywaspressed2 = K_LEFTPAREN
                                startinput2 = False
                            if pygame.key.get_pressed()[K_RIGHTPAREN]:
                                keywaspressed2 = K_RIGHTPAREN
                                startinput2 = False
                            if pygame.key.get_pressed()[K_ASTERISK]:
                                keywaspressed2 = K_ASTERISK
                                startinput2 = False
                            if pygame.key.get_pressed()[K_PLUS]:
                                keywaspressed2 = K_PLUS
                                startinput2 = False
                            if pygame.key.get_pressed()[K_COMMA]:
                                keywaspressed2 = K_COMMA
                                startinput2 = False
                            if pygame.key.get_pressed()[K_MINUS]:
                                keywaspressed2 = K_MINUS
                                startinput2 = False
                            if pygame.key.get_pressed()[K_PERIOD]:
                                keywaspressed2 = K_PERIOD
                                startinput2 = False
                            if pygame.key.get_pressed()[K_SLASH]:
                                keywaspressed2 = K_SLASH
                                startinput2 = False
                            if pygame.key.get_pressed()[K_0]:
                                keywaspressed2 = K_0
                                startinput2 = False
                            if pygame.key.get_pressed()[K_1]:
                                keywaspressed2 = K_1
                                startinput2 = False
                            if pygame.key.get_pressed()[K_2]:
                                keywaspressed2 = K_2
                                startinput2 = False
                            if pygame.key.get_pressed()[K_3]:
                                keywaspressed2 = K_3
                                startinput2 = False
                            if pygame.key.get_pressed()[K_4]:
                                keywaspressed2 = K_4
                                startinput2 = False
                            if pygame.key.get_pressed()[K_5]:
                                keywaspressed2 = K_5
                                startinput2 = False
                            if pygame.key.get_pressed()[K_6]:
                                keywaspressed2 = K_6
                                startinput2 = False
                            if pygame.key.get_pressed()[K_7]:
                                keywaspressed2 = K_7
                                startinput2 = False
                            if pygame.key.get_pressed()[K_8]:
                                keywaspressed2 = K_8
                                startinput2 = False
                            if pygame.key.get_pressed()[K_9]:
                                keywaspressed2 = K_9
                                startinput2 = False
                            if pygame.key.get_pressed()[K_COLON]:
                                keywaspressed2 = K_COLON
                                startinput2 = False
                            if pygame.key.get_pressed()[K_SEMICOLON]:
                                keywaspressed2 = K_SEMICOLON
                                startinput2 = False
                            if pygame.key.get_pressed()[K_LESS]:
                                keywaspressed2 = K_LESS
                                startinput2 = False
                            if pygame.key.get_pressed()[K_EQUALS]:
                                keywaspressed2 = K_EQUALS
                                startinput2 = False
                            if pygame.key.get_pressed()[K_GREATER]:
                                keywaspressed2 = K_GREATER
                                startinput2 = False
                            if pygame.key.get_pressed()[K_QUESTION]:
                                keywaspressed2 = K_QUESTION
                                startinput2 = False
                            if pygame.key.get_pressed()[K_AT]:
                                keywaspressed2 = K_AT
                                startinput2 = False
                            if pygame.key.get_pressed()[K_LEFTBRACKET]:
                                keywaspressed2 = K_LEFTBRACKET
                                startinput2 = False
                            if pygame.key.get_pressed()[K_BACKSLASH]:
                                keywaspressed2 = K_BACKSLASH
                                startinput2 = False
                            if pygame.key.get_pressed()[K_RIGHTBRACKET]:
                                keywaspressed2 = K_RIGHTBRACKET
                                startinput2 = False
                            if pygame.key.get_pressed()[K_CARET]:
                                keywaspressed2 = K_CARET
                                startinput2 = False
                            if pygame.key.get_pressed()[K_UNDERSCORE]:
                                keywaspressed2 = K_UNDERSCORE
                                startinput2 = False
                            if pygame.key.get_pressed()[K_BACKQUOTE]:
                                keywaspressed2 = K_BACKQUOTE
                                startinput2 = False
                            if pygame.key.get_pressed()[K_a]:
                                keywaspressed2 = K_a
                                startinput2 = False
                            if pygame.key.get_pressed()[K_b]:
                                keywaspressed2 = K_b
                                startinput2 = False
                            if pygame.key.get_pressed()[K_c]:
                                keywaspressed2 = K_c
                                startinput2 = False
                            if pygame.key.get_pressed()[K_d]:
                                keywaspressed2 = K_d
                                startinput2 = False
                            if pygame.key.get_pressed()[K_e]:
                                keywaspressed2 = K_e
                                startinput2 = False
                            if pygame.key.get_pressed()[K_f]:
                                keywaspressed2 = K_f
                                startinput2 = False
                            if pygame.key.get_pressed()[K_g]:
                                keywaspressed2 = K_g
                                startinput2 = False
                            if pygame.key.get_pressed()[K_h]:
                                keywaspressed2 = K_h
                                startinput2 = False
                            if pygame.key.get_pressed()[K_i]:
                                keywaspressed2 = K_i
                                startinput2 = False
                            if pygame.key.get_pressed()[K_j]:
                                keywaspressed2 = K_j
                                startinput2 = False
                            if pygame.key.get_pressed()[K_k]:
                                keywaspressed2 = K_k
                                startinput2 = False
                            if pygame.key.get_pressed()[K_l]:
                                keywaspressed2 = K_l
                                startinput2 = False
                            if pygame.key.get_pressed()[K_m]:
                                keywaspressed2 = K_m
                                startinput2 = False
                            if pygame.key.get_pressed()[K_o]:
                                keywaspressed2 = K_o
                                startinput2 = False
                            if pygame.key.get_pressed()[K_p]:
                                keywaspressed2 = K_p
                                startinput2 = False
                            if pygame.key.get_pressed()[K_q]:
                                keywaspressed2 = K_q
                                startinput2 = False
                            if pygame.key.get_pressed()[K_r]:
                                keywaspressed2 = K_r
                                startinput2 = False
                            if pygame.key.get_pressed()[K_s]:
                                keywaspressed2 = K_s
                                startinput2 = False
                            if pygame.key.get_pressed()[K_t]:
                                keywaspressed2 = K_t
                                startinput2 = False
                            if pygame.key.get_pressed()[K_u]:
                                keywaspressed2 = K_u
                                startinput2 = False
                            if pygame.key.get_pressed()[K_v]:
                                keywaspressed2 = K_v
                                startinput2 = False
                            if pygame.key.get_pressed()[K_w]:
                                keywaspressed2 = K_w
                                startinput2 = False
                            if pygame.key.get_pressed()[K_x]:
                                keywaspressed2 = K_x
                                startinput2 = False
                            if pygame.key.get_pressed()[K_y]:
                                keywaspressed2 = K_y
                                startinput2 = False
                            if pygame.key.get_pressed()[K_z]:
                                keywaspressed2 = K_z
                                startinput2 = False
                            if pygame.key.get_pressed()[K_DELETE]:
                                keywaspressed2 = K_DELETE
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP0]:
                                keywaspressed2 = K_KP0
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP1]:
                                keywaspressed2 = K_KP1
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP2]:
                                keywaspressed2 = K_KP2
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP3]:
                                keywaspressed2 = K_KP3
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP4]:
                                keywaspressed2 = K_KP4
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP5]:
                                keywaspressed2 = K_KP5
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP6]:
                                keywaspressed2 = K_KP6
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP7]:
                                keywaspressed2 = K_KP7
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP8]:
                                keywaspressed2 = K_KP8
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP9]:
                                keywaspressed2 = K_KP9
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP_PERIOD]:
                                keywaspressed2 = K_BACKSPACE
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP_DIVIDE]:
                                keywaspressed2 = K_KP_DIVIDE
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP_MULTIPLY]:
                                keywaspressed2 = K_KP_MULTIPLY
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP_MINUS]:
                                keywaspressed2 = K_KP_MINUS
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP_PLUS]:
                                keywaspressed2 = K_KP_PLUS
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP_ENTER]:
                                keywaspressed2 = K_KP_ENTER
                                startinput2 = False
                            if pygame.key.get_pressed()[K_KP_EQUALS]:
                                keywaspressed2 = K_KP_EQUALS
                                startinput2 = False
                            if pygame.key.get_pressed()[K_UP]:
                                keywaspressed2 = K_UP
                                startinput2 = False
                            if pygame.key.get_pressed()[K_DOWN]:
                                keywaspressed2 = K_DOWN
                                startinput2 = False
                            if pygame.key.get_pressed()[K_RIGHT]:
                                keywaspressed2 = K_RIGHT
                                startinput2 = False
                            if pygame.key.get_pressed()[K_LEFT]:
                                keywaspressed2 = K_LEFT
                                startinput2 = False
                            if pygame.key.get_pressed()[K_INSERT]:
                                keywaspressed2 = K_INSERT
                                startinput2 = False
                            if pygame.key.get_pressed()[K_HOME]:
                                keywaspressed2 = K_HOME
                                startinput2 = False
                            if pygame.key.get_pressed()[K_END]:
                                keywaspressed2 = K_END
                                startinput2 = False
                            if pygame.key.get_pressed()[K_PAGEUP]:
                                keywaspressed2 = K_PAGEUP
                                startinput2 = False
                            if pygame.key.get_pressed()[K_PAGEDOWN]:
                                keywaspressed2 = K_PAGEDOWN
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F1]:
                                keywaspressed2 = K_F1
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F2]:
                                keywaspressed2 = K_F2
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F3]:
                                keywaspressed2 = K_F3
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F4]:
                                keywaspressed2 = K_F4
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F5]:
                                keywaspressed2 = K_F5
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F6]:
                                keywaspressed2 = K_F6
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F7]:
                                keywaspressed2 = K_F7
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F8]:
                                keywaspressed2 = K_F8
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F9]:
                                keywaspressed2 = K_F9
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F10]:
                                keywaspressed2 = K_F10
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F11]:
                                keywaspressed2 = K_F11
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F12]:
                                keywaspressed2 = K_F12
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F13]:
                                keywaspressed2 = K_F13
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F14]:
                                keywaspressed2 = K_F14
                                startinput2 = False
                            if pygame.key.get_pressed()[K_F15]:
                                keywaspressed2 = K_F15
                                startinput2 = False
                            if pygame.key.get_pressed()[K_NUMLOCK]:
                                keywaspressed2 = K_NUMLOCK
                                startinput2 = False
                            if pygame.key.get_pressed()[K_CAPSLOCK]:
                                keywaspressed2 = K_CAPSLOCK
                                startinput2 = False
                            if pygame.key.get_pressed()[K_SCROLLOCK]:
                                keywaspressed2 = K_SCROLLOCK
                                startinput2 = False
                            if pygame.key.get_pressed()[K_RSHIFT]:
                                keywaspressed2 = K_RSHIFT
                                startinput2 = False
                            if pygame.key.get_pressed()[K_LSHIFT]:
                                keywaspressed2 = K_LSHIFT
                                startinput2 = False
                            if pygame.key.get_pressed()[K_RCTRL]:
                                keywaspressed2 = K_RCTRL
                                startinput2 = False
                            if pygame.key.get_pressed()[K_LCTRL]:
                                keywaspressed2 = K_LCTRL
                                startinput2 = False
                            if pygame.key.get_pressed()[K_RALT]:
                                keywaspressed2 = K_RALT
                                startinput2 = False
                            if pygame.key.get_pressed()[K_LALT]:
                                keywaspressed2 = K_LALT
                                startinput2 = False
                            if pygame.key.get_pressed()[K_RMETA]:
                                keywaspressed2 = K_RMETA
                                startinput2 = False
                            if pygame.key.get_pressed()[K_LMETA]:
                                keywaspressed2 = K_LMETA
                                startinput2 = False
                            if pygame.key.get_pressed()[K_LSUPER]:
                                keywaspressed2 = K_LSUPER
                                startinput2 = False
                            if pygame.key.get_pressed()[K_RSUPER]:
                                keywaspressed2 = K_RSUPER
                                startinput2 = False
                font2 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
                textinput2 = font2.render(pygame.key.name(keywaspressed2), True, Yellow)
                DISPLAY.blit(textinput2,(910,370))

            
                if startinput3 == True:
                            if pygame.key.get_pressed()[K_BACKSPACE]:
                                keywaspressed3 = K_BACKSPACE
                                startinput3 = False
                            if pygame.key.get_pressed()[K_TAB]:
                                keywaspressed3 = K_TAB
                                startinput3 = False
                            if pygame.key.get_pressed()[K_CLEAR]:
                                keywaspressed3 = K_CLEAR
                                startinput3 = False
                            if pygame.key.get_pressed()[K_RETURN]:
                                keywaspressed3 = K_RETURN
                                startinput3 = False  
                            if pygame.key.get_pressed()[K_PAUSE]:
                                keywaspressed3 = K_PAUSE
                                startinput3 = False
                            if pygame.key.get_pressed()[K_ESCAPE]:
                                keywaspressed3 = K_ESCAPE
                                startinput3 = False
                            if pygame.key.get_pressed()[K_SPACE]:
                                keywaspressed3 = K_SPACE
                                startinput3 = False
                            if pygame.key.get_pressed()[K_EXCLAIM]:
                                keywaspressed3 = K_EXCLAIM
                                startinput3 = False
                            if pygame.key.get_pressed()[K_QUOTEDBL]:
                                keywaspressed3 = K_QUOTEDBL
                                startinput3 = False
                            if pygame.key.get_pressed()[K_HASH]:
                                keywaspressed3 = K_HASH
                                startinput3 = False
                            if pygame.key.get_pressed()[K_DOLLAR]:
                                keywaspressed3 = K_DOLLAR
                                startinput3 = False
                            if pygame.key.get_pressed()[K_AMPERSAND]:
                                keywaspressed3 = K_AMPERSAND
                                startinput3 = False
                            if pygame.key.get_pressed()[K_QUOTE]:
                                keywaspressed3 = K_QUOTE
                                startinput3 = False
                            if pygame.key.get_pressed()[K_LEFTPAREN]:
                                keywaspressed3 = K_LEFTPAREN
                                startinput3 = False
                            if pygame.key.get_pressed()[K_RIGHTPAREN]:
                                keywaspressed3 = K_RIGHTPAREN
                                startinput3 = False
                            if pygame.key.get_pressed()[K_ASTERISK]:
                                keywaspressed3 = K_ASTERISK
                                startinput3 = False
                            if pygame.key.get_pressed()[K_PLUS]:
                                keywaspressed3 = K_PLUS
                                startinput3 = False
                            if pygame.key.get_pressed()[K_COMMA]:
                                keywaspressed3 = K_COMMA
                                startinput3 = False
                            if pygame.key.get_pressed()[K_MINUS]:
                                keywaspressed3 = K_MINUS
                                startinput3 = False
                            if pygame.key.get_pressed()[K_PERIOD]:
                                keywaspressed3 = K_PERIOD
                                startinput3 = False
                            if pygame.key.get_pressed()[K_SLASH]:
                                keywaspressed3 = K_SLASH
                                startinput3 = False
                            if pygame.key.get_pressed()[K_0]:
                                keywaspressed3 = K_0
                                startinput3 = False
                            if pygame.key.get_pressed()[K_1]:
                                keywaspressed3 = K_1
                                startinput3 = False
                            if pygame.key.get_pressed()[K_2]:
                                keywaspressed3 = K_2
                                startinput3 = False
                            if pygame.key.get_pressed()[K_3]:
                                keywaspressed3 = K_3
                                startinput3 = False
                            if pygame.key.get_pressed()[K_4]:
                                keywaspressed3 = K_4
                                startinput3 = False
                            if pygame.key.get_pressed()[K_5]:
                                keywaspressed3 = K_5
                                startinput3 = False
                            if pygame.key.get_pressed()[K_6]:
                                keywaspressed3 = K_6
                                startinput3 = False
                            if pygame.key.get_pressed()[K_7]:
                                keywaspressed3 = K_7
                                startinput3 = False
                            if pygame.key.get_pressed()[K_8]:
                                keywaspressed3 = K_8
                                startinput3 = False
                            if pygame.key.get_pressed()[K_9]:
                                keywaspressed3 = K_9
                                startinput3 = False
                            if pygame.key.get_pressed()[K_COLON]:
                                keywaspressed3 = K_COLON
                                startinput3 = False
                            if pygame.key.get_pressed()[K_SEMICOLON]:
                                keywaspressed3 = K_SEMICOLON
                                startinput3 = False
                            if pygame.key.get_pressed()[K_LESS]:
                                keywaspressed3 = K_LESS
                                startinput3 = False
                            if pygame.key.get_pressed()[K_EQUALS]:
                                keywaspressed3 = K_EQUALS
                                startinput3 = False
                            if pygame.key.get_pressed()[K_GREATER]:
                                keywaspressed3 = K_GREATER
                                startinput3 = False
                            if pygame.key.get_pressed()[K_QUESTION]:
                                keywaspressed3 = K_QUESTION
                                startinput3 = False
                            if pygame.key.get_pressed()[K_AT]:
                                keywaspressed3 = K_AT
                                startinput3 = False
                            if pygame.key.get_pressed()[K_LEFTBRACKET]:
                                keywaspressed3 = K_LEFTBRACKET
                                startinput3 = False
                            if pygame.key.get_pressed()[K_BACKSLASH]:
                                keywaspressed3 = K_BACKSLASH
                                startinput3 = False
                            if pygame.key.get_pressed()[K_RIGHTBRACKET]:
                                keywaspressed3 = K_RIGHTBRACKET
                                startinput3 = False
                            if pygame.key.get_pressed()[K_CARET]:
                                keywaspressed3 = K_CARET
                                startinput3 = False
                            if pygame.key.get_pressed()[K_UNDERSCORE]:
                                keywaspressed3 = K_UNDERSCORE
                                startinput3 = False
                            if pygame.key.get_pressed()[K_BACKQUOTE]:
                                keywaspressed3 = K_BACKQUOTE
                                startinput3 = False
                            if pygame.key.get_pressed()[K_a]:
                                keywaspressed3 = K_a
                                startinput3 = False
                            if pygame.key.get_pressed()[K_b]:
                                keywaspressed3 = K_b
                                startinput3 = False
                            if pygame.key.get_pressed()[K_c]:
                                keywaspressed3 = K_c
                                startinput3 = False
                            if pygame.key.get_pressed()[K_d]:
                                keywaspressed3 = K_d
                                startinput3 = False
                            if pygame.key.get_pressed()[K_e]:
                                keywaspressed3 = K_e
                                startinput3 = False
                            if pygame.key.get_pressed()[K_f]:
                                keywaspressed3 = K_f
                                startinput3 = False
                            if pygame.key.get_pressed()[K_g]:
                                keywaspressed3 = K_g
                                startinput3 = False
                            if pygame.key.get_pressed()[K_h]:
                                keywaspressed3 = K_h
                                startinput3 = False
                            if pygame.key.get_pressed()[K_i]:
                                keywaspressed3 = K_i
                                startinput3 = False
                            if pygame.key.get_pressed()[K_j]:
                                keywaspressed3 = K_j
                                startinput3 = False
                            if pygame.key.get_pressed()[K_k]:
                                keywaspressed3 = K_k
                                startinput3 = False
                            if pygame.key.get_pressed()[K_l]:
                                keywaspressed3 = K_l
                                startinput3 = False
                            if pygame.key.get_pressed()[K_m]:
                                keywaspressed3 = K_m
                                startinput3 = False
                            if pygame.key.get_pressed()[K_o]:
                                keywaspressed3 = K_o
                                startinput3 = False
                            if pygame.key.get_pressed()[K_p]:
                                keywaspressed3 = K_p
                                startinput3 = False
                            if pygame.key.get_pressed()[K_q]:
                                keywaspressed3 = K_q
                                startinput3 = False
                            if pygame.key.get_pressed()[K_r]:
                                keywaspressed3 = K_r
                                startinput3 = False
                            if pygame.key.get_pressed()[K_s]:
                                keywaspressed3 = K_s
                                startinput3 = False
                            if pygame.key.get_pressed()[K_t]:
                                keywaspressed3 = K_t
                                startinput3 = False
                            if pygame.key.get_pressed()[K_u]:
                                keywaspressed3 = K_u
                                startinput3 = False
                            if pygame.key.get_pressed()[K_v]:
                                keywaspressed3 = K_v
                                startinput3 = False
                            if pygame.key.get_pressed()[K_w]:
                                keywaspressed3 = K_w
                                startinput3 = False
                            if pygame.key.get_pressed()[K_x]:
                                keywaspressed3 = K_x
                                startinput3 = False
                            if pygame.key.get_pressed()[K_y]:
                                keywaspressed3 = K_y
                                startinput3 = False
                            if pygame.key.get_pressed()[K_z]:
                                keywaspressed3 = K_z
                                startinput3 = False
                            if pygame.key.get_pressed()[K_DELETE]:
                                keywaspressed3 = K_DELETE
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP0]:
                                keywaspressed3 = K_KP0
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP1]:
                                keywaspressed3 = K_KP1
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP2]:
                                keywaspressed3 = K_KP2
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP3]:
                                keywaspressed3 = K_KP3
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP4]:
                                keywaspressed3 = K_KP4
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP5]:
                                keywaspressed3 = K_KP5
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP6]:
                                keywaspressed3 = K_KP6
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP7]:
                                keywaspressed3 = K_KP7
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP8]:
                                keywaspressed3 = K_KP8
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP9]:
                                keywaspressed3 = K_KP9
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP_PERIOD]:
                                keywaspressed3 = K_BACKSPACE
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP_DIVIDE]:
                                keywaspressed3 = K_KP_DIVIDE
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP_MULTIPLY]:
                                keywaspressed3 = K_KP_MULTIPLY
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP_MINUS]:
                                keywaspressed3 = K_KP_MINUS
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP_PLUS]:
                                keywaspressed3 = K_KP_PLUS
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP_ENTER]:
                                keywaspressed3 = K_KP_ENTER
                                startinput3 = False
                            if pygame.key.get_pressed()[K_KP_EQUALS]:
                                keywaspressed3 = K_KP_EQUALS
                                startinput3 = False
                            if pygame.key.get_pressed()[K_UP]:
                                keywaspressed3 = K_UP
                                startinput3 = False
                            if pygame.key.get_pressed()[K_DOWN]:
                                keywaspressed3 = K_DOWN
                                startinput3 = False
                            if pygame.key.get_pressed()[K_RIGHT]:
                                keywaspressed3 = K_RIGHT
                                startinput3 = False
                            if pygame.key.get_pressed()[K_LEFT]:
                                keywaspressed3 = K_LEFT
                                startinput3 = False
                            if pygame.key.get_pressed()[K_INSERT]:
                                keywaspressed3 = K_INSERT
                                startinput3 = False
                            if pygame.key.get_pressed()[K_HOME]:
                                keywaspressed3 = K_HOME
                                startinput3 = False
                            if pygame.key.get_pressed()[K_END]:
                                keywaspressed3 = K_END
                                startinput3 = False
                            if pygame.key.get_pressed()[K_PAGEUP]:
                                keywaspressed3 = K_PAGEUP
                                startinput3 = False
                            if pygame.key.get_pressed()[K_PAGEDOWN]:
                                keywaspressed3 = K_PAGEDOWN
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F1]:
                                keywaspressed3 = K_F1
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F2]:
                                keywaspressed3 = K_F2
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F3]:
                                keywaspressed3 = K_F3
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F4]:
                                keywaspressed3 = K_F4
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F5]:
                                keywaspressed3 = K_F5
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F6]:
                                keywaspressed3 = K_F6
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F7]:
                                keywaspressed3 = K_F7
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F8]:
                                keywaspressed3 = K_F8
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F9]:
                                keywaspressed3 = K_F9
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F10]:
                                keywaspressed3 = K_F10
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F11]:
                                keywaspressed3 = K_F11
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F12]:
                                keywaspressed3 = K_F12
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F13]:
                                keywaspressed3 = K_F13
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F14]:
                                keywaspressed3 = K_F14
                                startinput3 = False
                            if pygame.key.get_pressed()[K_F15]:
                                keywaspressed3 = K_F15
                                startinput3 = False
                            if pygame.key.get_pressed()[K_NUMLOCK]:
                                keywaspressed3 = K_NUMLOCK
                                startinput3 = False
                            if pygame.key.get_pressed()[K_CAPSLOCK]:
                                keywaspressed3 = K_CAPSLOCK
                                startinput3 = False
                            if pygame.key.get_pressed()[K_SCROLLOCK]:
                                keywaspressed3 = K_SCROLLOCK
                                startinput3 = False
                            if pygame.key.get_pressed()[K_RSHIFT]:
                                keywaspressed3 = K_RSHIFT
                                startinput3 = False
                            if pygame.key.get_pressed()[K_LSHIFT]:
                                keywaspressed3 = K_LSHIFT
                                startinput3 = False
                            if pygame.key.get_pressed()[K_RCTRL]:
                                keywaspressed3 = K_RCTRL
                                startinput3 = False
                            if pygame.key.get_pressed()[K_LCTRL]:
                                keywaspressed3 = K_LCTRL
                                startinput3 = False
                            if pygame.key.get_pressed()[K_RALT]:
                                keywaspressed3 = K_RALT
                                startinput3 = False
                            if pygame.key.get_pressed()[K_LALT]:
                                keywaspressed3 = K_LALT
                                startinput3 = False
                            if pygame.key.get_pressed()[K_RMETA]:
                                keywaspressed3 = K_RMETA
                                startinput3 = False
                            if pygame.key.get_pressed()[K_LMETA]:
                                keywaspressed3 = K_LMETA
                                startinput3 = False
                            if pygame.key.get_pressed()[K_LSUPER]:
                                keywaspressed3 = K_LSUPER
                                startinput3 = False
                            if pygame.key.get_pressed()[K_RSUPER]:
                                keywaspressed3 = K_RSUPER
                                startinput3 = False
                font3 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 50)
                textinput3 = font3.render(pygame.key.name(keywaspressed3), True, Yellow)
                DISPLAY.blit(textinput3,(910,470))

                pygame.display.update() 
                if back == True:

                    DISPLAY.blit(background, (0, 0))
                    DISPLAY.blit(textcoin,(screen_height/2.20,screen_width/2.5))
                    DISPLAY.blit(textenemie,(screen_width*1.6, screen_height/2.05))
                    DISPLAY.blit(Playerhealth,(screen_width/13, screen_height/2.05))

                    Enemie.DrawBar(barPos, barSize, borderColor, barColor, Health/max_a)
                    Player.DrawBar(barPos2, barSize2, borderColor2, barColor2, PlayerHealth/max_a2)

                    all_sprites_list.draw(DISPLAY)
                    break
                    

        


    

class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = laserbullet
        self.rect = self.image.get_rect()
        self.speedy = 5
        self.rect.x = playerx + 40
        self.rect.y = playery - 25

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.top < 5:
            self.kill()

class Bulletback(pygame.sprite.Sprite):

    def __init__(self,center):
        super().__init__()

        self.image = bulletred
        self.rect = self.image.get_rect(center=center)
        self.speedy = -5

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.y > screen_height:
            self.kill()

class Explosion(pygame.sprite.Sprite):

    def __init__(self,center):
        super().__init__()

        self.image = explosion
        self.rect = self.image.get_rect(center=center)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100


    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            explosound.play()
            self.last_update = now
            self.frame += 1
        if self.frame == 2:
            self.kill()
        else:
            self.image = explosion
            self.rect = self.image.get_rect(center=self.rect.center)

class ButtonMenu():

    def __init__(self):
        self.image = butMenu
        self.rect = self.image.get_rect()
        self.rect.x = screen_width/2.7
        self.rect.y = screen_height/4.5

    def draw(self):
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

class ButtonSettings():

    def __init__(self):
        self.image = butsettings
        self.rect = self.image.get_rect()
        self.rect.x = screen_width/2.7
        self.rect.y = screen_height/2.5

    def draw(self):
        global Settings
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                Menu.SettingsMenu(self)

class ButtonContinue():

    def __init__(self):
        self.image = butContinue
        self.rect = self.image.get_rect()
        self.rect.x = screen_width/2.7
        self.rect.y = screen_height/1.7

    def draw(self):
        global run
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                run = True 

class SettingsMenu():
    def __init__(self):
        self.image = Settingsmenu
        self.rect = self.image.get_rect()
        self.rect.x = 140
        self.rect.y = 60
    def draw(self):
        DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

class SoundSettings():
    def __init__(self):
        self.image = Sound
        self.rect = self.image.get_rect()
        self.rect.x = 188
        self.rect.y = 134
    def draw(self):
        global soundm
        soundm = False
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                soundm = True
                Menu.Soundmenu(self)

        return soundm

class SoundSettings1():
    def __init__(self):
        self.image = Sound
        self.rect = self.image.get_rect()
        self.rect.x = 188
        self.rect.y = 134
    def draw(self):
        global soundm,breakvideo
        soundm = False
        breakvideo = False
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                soundm = True
                breakvideo = True

        return soundm,breakvideo


class VideoSettings():
    def __init__(self):
        self.image = Video
        self.rect = self.image.get_rect()
        self.rect.x = 517
        self.rect.y = 134
    def draw(self):
        global vidsettings
        vidsettings = False
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                vidsettings = True
                Menu.VideoSettings(self)

        return vidsettings

class VideoSettings1():
    def __init__(self):
        self.image = Video
        self.rect = self.image.get_rect()
        self.rect.x = 517
        self.rect.y = 134
    def draw(self):
        global vidsettings,breaksound
        breaksound = False
        vidsettings = False
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                vidsettings = True
                breaksound = True

        return vidsettings



class ControlsSettings():
    def __init__(self):
        self.image = Controls
        self.rect = self.image.get_rect()
        self.rect.x = 823
        self.rect.y = 134
    def draw(self):
        global control
        pos = pygame.mouse.get_pos()
        control = False
        DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                control = True
                Menu.Conntrolmenu(self)

        return control 

class backSettingsMenu():
    def __init__(self):
        self.image = Back
        self.rect = self.image.get_rect()
        self.rect.x = 967
        self.rect.y = 566 
    def draw(self):
        global back
        back = False
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                back = True

        return back

class Soundback():
    def __init__(self):
        self.image = Back
        self.rect = self.image.get_rect()
        self.rect.x = 967
        self.rect.y = 566 
    def draw(self):
        global back
        back = False
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                back = True

        return back


class Volume():
    def __init__(self):
        self.image = volumepng
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 204
    def draw(self):
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
class Plus():
    def __init__(self):
        self.image = plus
        self.rect = self.image.get_rect()
        self.rect.x = 975
        self.rect.y = 211
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        global volume
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    volume += 10
                    if volume > 100:
                        volume = 100
class Minus():
    def __init__(self):
        self.image = minus
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 211
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        global volume
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:#
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    volume -= 10
                    if volume < 0:
                        volume = 0
class Volume1():
    def __init__(self):
        self.image = musicpng
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 295
    def draw(self):
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
class Plus1():
    def __init__(self):
        self.image = plus
        self.rect = self.image.get_rect()
        self.rect.x = 975
        self.rect.y = 295
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        global musicvolume
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    musicvolume += 10
                    if musicvolume > 100:
                        musicvolume = 100
class Minus1():
    def __init__(self):
        self.image = minus
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 295
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        global musicvolume
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    musicvolume -= 10
                    if musicvolume < 0:
                        musicvolume = 0
class Resolution():
    def __init__(self):
        self.image = reso
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 295
    def draw(self):
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

class dropdown():
    def __init__(self):
        self.image = zeile
        self.rect = self.image.get_rect()
        self.rect.x = 775
        self.rect.y = 286
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        global rahmenmenu,closerahmen
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    rahmenmenu = True
                    closerahmen += 1

class dropdownrahmen():
    def __init__(self):
        self.image = rahmen
        self.rect = self.image.get_rect()
        self.rect.x = 775
        self.rect.y = 335
    def draw(self):
        DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

class currentResolution():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(str(screen_height) +  " x " + str(screen_width), True, Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 785
        self.rect.y = 282

    def draw(self):
        DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

class r1680x1050():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(reso1, True, Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 785
        self.rect.y = 332
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        global screen_height, screen_width, Apply
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    screen_height = int(reso1[7:11])
                    screen_width = int(reso1[0:4])
                    Apply = True
        return Apply
class r1280x1024():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(reso2, True, Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 785
        self.rect.y = 372
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        global screen_height, screen_width, Apply
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    screen_height = int(reso2[7:11])
                    screen_width = int(reso2[0:4])
                    Apply = True
        return Apply
        
class r720x1280():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(reso3, True, Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 805
        self.rect.y = 412
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        global screen_height, screen_width, Apply
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    screen_height = int(reso3[7:12])
                    screen_width = int(reso3[0:4])
                    Apply = True
                    print(screen_height)
        return Apply
class r640x480():
    def __init__(self):
        font = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
        self.text = font.render(reso4, True, Yellow)
        self.rect = self.text.get_rect()
        self.rect.x = 800
        self.rect.y = 452
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        global screen_height, screen_width, Apply
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.text,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            #pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(800,452,32,300))
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    screen_height = int(reso4[7:12])
                    screen_width = int(reso4[0:4])
                    Apply = True
        return Apply
class Fullscreenmode():
    def __init__(self):
        self.image = Fullscreenpng
        self.rect = self.image.get_rect()
        self.rect.x = 181
        self.rect.y = 200
    def draw(self):
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

class Fullscreencheckbox():
    def __init__(self):
        self.image = xkasten
        self.rect = self.image.get_rect()
        self.rect.x = 805
        self.rect.y = 200
        self.cooldown = 300
        self.last = pygame.time.get_ticks()
    def draw(self):
        global toggofull,toggofull2
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            #pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(800,452,32,300))
            if pygame.mouse.get_pressed()[0] == 1:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    toggofull = True
                    toggofull2 += 1
                    pygame.display.toggle_fullscreen()
        return toggofull

class controlesettings():
    def __init__(self):
        self.image = keyspng
        self.rect = self.image.get_rect()       
        self.rect.x = 181
        self.rect.y = 204
    def draw(self):
        DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

class keys():
    def __init__(self):
        self.shootimage = shootpng
        self.moverightimage = moverightpng
        self.moveleftimage = moveleftpng
        self.settingspng = settingspng
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
        DISPLAY.blit(self.shootimage,(self.rect.x,self.rect.y))
        DISPLAY.blit(self.moverightimage,(self.rect1.x,self.rect1.y))
        DISPLAY.blit(self.moveleftimage,(self.rect2.x,self.rect2.y))
        DISPLAY.blit(self.settingspng,(self.rect3.x,self.rect3.y))

class keyinputs():
    def __init__(self):
        self.keyinput = keyinputpng
        self.keyinput1 = keyinputpng
        self.keyinput2 = keyinputpng
        self.keyinput3 = keyinputpng
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
        global startinput,startinput1,startinput2,startinput3
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.keyinput,(self.rect.x,self.rect.y))
        DISPLAY.blit(self.keyinput1,(self.rect1.x,self.rect1.y))
        DISPLAY.blit(self.keyinput2,(self.rect2.x,self.rect2.y))
        DISPLAY.blit(self.keyinput3,(self.rect3.x,self.rect3.y))

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                startinput = True
        if self.rect1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                startinput1 = True
        if self.rect2.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                startinput2 = True
        if self.rect3.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                startinput3 = True





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
player = Player()
player_list.add(player)
all_sprites_list.add(player)


for i in range(10):
    en = Enemie()

    enemie_list.add(en)
    all_sprites_list.add(en)



cooldown = 300
last = pygame.time.get_ticks()
run = True
pauseon = False


while run:
        dt = clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
                
        all_sprites_list.update()

        for i in range(dur):
            now = pygame.time.get_ticks()
            if now - last0 >= cooldown0:
                last0 = now
                Enemie.shootback()

        for bullet in bullet_list:

            now = pygame.time.get_ticks()
            if now - last >= cooldown:
                last = now
                if pygame.sprite.spritecollide(bullet, enemie_list,dokill=False):
                    Health -= 1
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)


            if Health == 0:
                bol = True
                enemie_hit_list = pygame.sprite.spritecollide(bullet, enemie_list, bol)
                Health = 4
                for enemies in enemie_hit_list:
                    expl = Explosion(enemies.rect.center)
                    all_sprites_list.add(expl)
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)
                    coins += 15

            if bullet.rect.y < -5:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)


        for bulletback in bulletback_list:
            now = pygame.time.get_ticks()
            if now - last >= cooldown:
                last = now
                if pygame.sprite.groupcollide(bulletback_list, player_list,False,False):
                    PlayerHealth -= 1
                    bulletback_list.remove(bulletback)
                    all_sprites_list.remove(bulletback)
                    


                if PlayerHealth == 0:
                    Playerhit_list = pygame.sprite.groupcollide(bulletback_list,player_list,True,True)
                    for player in Playerhit_list:
                        expl = Explosion(player.rect.center)
                        all_sprites_list.add(expl)
                        bulletback_list.remove(bulletback)
                        all_sprites_list.remove(bulletback)
                        player_list.remove(player)
                        all_sprites_list.remove(player)
                
                if bulletback.rect.y > screen_height:
                    bulletback_list.remove(bulletback)
                    all_sprites_list.remove(bulletback)

        if not all_sprites_list.has(enemie_list):
            DISPLAY=pygame.display.set_mode((screen_height,screen_width),0,32)

            font_obj5 = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
            textcoin2 = font_obj5.render(str(coins)+"💰", True, Yellow)

            font_obj4 = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
            textwin = font_obj4.render("You won 💪", True, Yellow)


            DISPLAY.blit(textcoin2,(screen_width * 2,screen_height))
            DISPLAY.blit(textwin,(582,290))

        font_obj = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
        textcoin = font_obj.render(str(coins)+"💰", True, Yellow)


        font_obj2 = pygame.font.Font('freesansbold.ttf', 20)
        Playerhealth = font_obj2.render(Playername, True, Lightgrey)
                    
        font_obj3 = pygame.font.Font('freesansbold.ttf', 20)
        textenemie = font_obj3.render(enemiename, True, Lightgrey)                


        DISPLAY.blit(background, (0, 0))
        DISPLAY.blit(textcoin,(screen_width/2.2,screen_height/2.2))
        DISPLAY.blit(textenemie,(screen_width/1.16, screen_height/1.19))
        DISPLAY.blit(Playerhealth,(screen_width/15, screen_height/1.19))
        barPos= (screen_width/1.16, screen_height/1.15)
        barPos2= (screen_width/15, screen_height/1.15)
        Enemie.DrawBar(barPos, barSize, borderColor, barColor, Health/max_a)
        Player.DrawBar(barPos2, barSize2, borderColor2, barColor2, PlayerHealth/max_a2)

        all_sprites_list.draw(DISPLAY)
       

        pygame.display.update()
        