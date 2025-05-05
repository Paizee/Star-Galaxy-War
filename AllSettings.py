import importlib
from tkinter import Menu
import pygame.gfxdraw
import time
import pygame, pygame.mixer
from pygame.locals import *
import os
import random

pygame.init()
pygame.mixer.init()
screen_height = 720
screen_width = 1280
DISPLAY=pygame.display.set_mode((screen_width,screen_height),0,64)
pygame.display.set_caption("Pilot Galaxy War")
logoiconpng = pygame.image.load(os.path.join("data/images","logoicon.png"))
pygame.display.set_icon(logoiconpng)
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
butMenu1 = pygame.transform.smoothscale(butMenu,(250,75))
Settingsmenu = pygame.image.load(os.path.join("data/images", "Settingsmenu.png"))
Back = pygame.image.load(os.path.join("data/images", "Back.png"))
Sound = pygame.image.load(os.path.join("data/images", "Sound.png"))
Video = pygame.image.load(os.path.join("data/images", "Video.png"))
Controls = pygame.image.load(os.path.join("data/images", "Controls.png"))
plus = pygame.image.load(os.path.join("data/images","plus.png"))
minus = pygame.image.load(os.path.join("data/images","minus.png"))
volumepng = pygame.image.load(os.path.join("data/images", "volume.png"))
music = pygame.mixer.Sound(os.path.join("data/sounds","music.mp3"))
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
leaderboardpng = pygame.image.load(os.path.join("data/images","Leaderboardwindow.png"))
userimagepng = pygame.image.load(os.path.join("data/images","c3po.png"))
registerimagepng = pygame.image.load(os.path.join("data/images","register.png"))
registerimageinputpng = pygame.image.load(os.path.join("data/images","reginput.png"))
Submitpng = pygame.image.load(os.path.join("data/images","Submit.png"))
loginuserimagepng = pygame.image.load(os.path.join("data/images","LoginUser.png"))
registeruserimagepng = pygame.image.load(os.path.join("data/images","RegisterUser.png"))
Loginimagepng = pygame.image.load(os.path.join("data/images","Login.png"))
logoutimagepng = pygame.image.load(os.path.join("data/images","Logout.png"))
shiptostart = pygame.image.load(os.path.join("data/images","ship.png"))
Playtostart = pygame.image.load(os.path.join("data/images","Play.png"))
click = pygame.mixer.Sound(os.path.join("data/sounds","click.wav"))
font_objcoins = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
font_objnotlogged = pygame.font.Font(os.path.join("data/fonts","Rubik-Bold.TTF"), 16)




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
PlayerHealth = 15
Health = 4

clock = pygame.time.Clock()
bol = False
Settings = True
rahmenmenu = False
Apply = False
toggofull = False
start = True
run = True
hjah = False
nameinput = False
emailinput = False
passwordinput = False
password2input = False
Emailsubmitcheck = False
Passwordsubmitcheck = False
Namesubmitcheck = False
Usershow  = False
Userclicked = 0
Emailcheckfinish = False
Passwordcheckfinish = False 
Namecheckfinish = False
login = False
keywaspressed = K_SPACE
keywaspressed1 = K_a
keywaspressed2 = K_d
keywaspressed3 = K_ESCAPE
startinput = False
startinput1 = False
startinput2 = False
startinput3 = False
breakcontrol = False
toggofull2 = 0
closerahmen = 0
rand = random.randrange(10,17)

volume = 100
musicvolume = 100
reso1 = "1680 x 1050"
reso2 = "1280 x 1024"
reso3 = "720  x  1280"
reso4 = "640  x  480"
LoginName = ""
kill = False
Leader = False
level1run = False
reg = False
log = False
