from re import S, X
from turtle import width
from pygame_menu.widgets.core.widget import Widget
from pygame_menu.widgets.core.selection import Selection
import pygame.gfxdraw
import pygame_menu
import sys, pygame, pygame.mixer
from pygame.locals import *
import os
import random
pygame.init()
screen_height = 720
screen_width = 1281
DISPLAY=pygame.display.set_mode((screen_width,screen_height),0,64)
pygame.display.set_caption("Pilot Galaxy War")
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
        if keys[pygame.K_a]:
            self.rect.x  -=7
        elif keys[pygame.K_d]:
            self.rect.x  +=7
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown:
                self.last = now
                player.shoot()
                shot.play()
        if keys[pygame.K_ESCAPE]:
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
        global soundm
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
                SettingsVideo.draw()
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
    def VideoSettings(self):
        global reso1,reso2,reso3,reso4,Apply,DISPLAY,closerahmen,screen_height,screen_width,toggofull2,toggofull,soundm
        if vidsettings == True: 
            while True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        exit()
                SettingsSound.draw()
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
        global soundm,breakvideo
        soundm = False
        breakvideo = False
        pos = pygame.mouse.get_pos()
        DISPLAY.blit(self.image,(self.rect.x, self.rect.y))


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                soundm = True
                breakvideo = True
                Menu.Soundmenu(self)

        return soundm

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

class ControlsSettings():
    def __init__(self):
        self.image = Controls
        self.rect = self.image.get_rect()
        self.rect.x = 823
        self.rect.y = 134
    def draw(self):
        DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

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





cooldown0 = 1200
last0 = pygame.time.get_ticks()
Fullcheckbox = Fullscreencheckbox()
Fullscreenmodepng = Fullscreenmode()
SettingsSound = SoundSettings()
SettingsVideo = VideoSettings()
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
        