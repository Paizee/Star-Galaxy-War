

from tkinter import Menu
from turtle import back
import pygame.gfxdraw
import time
import pygame, pygame.mixer
from pygame.locals import *
import os
import random
import AllSettings
import Animations
import Enemy
import level1
import Player
import Settingwindow
class rungame():
    def runit():

            pygame.init
            pygame.mixer.init

            DISPLAY=pygame.display.set_mode((AllSettings.screen_width,AllSettings.screen_height),0,64)
            pygame.display.set_caption("Pilot Galaxy War")
            pygame.display.set_icon(AllSettings.logoiconpng)

            cooldown0 = 1200
            last0 = pygame.time.get_ticks()
            player = Player.Player()
            AllSettings.player_list.add(player)
            AllSettings.all_sprites_list.add(player)
            coins = 0
            Health = 4
            PlayerHealth = 15
            for i in range(10):
                en = Enemy.Enemie()

                AllSettings.enemie_list.add(en)
                AllSettings.all_sprites_list.add(en)

            cooldown = 300
            last = pygame.time.get_ticks()
            while AllSettings.run:
                dt = AllSettings.clock.tick(60)
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        exit()
                AllSettings.all_sprites_list.update()
                for i in range(AllSettings.dur):
                    now = pygame.time.get_ticks()
                    if now - last0 >= cooldown0:
                        last0 = now
                        Enemy.Enemie.shootback()

                for bullet in AllSettings.bullet_list:

                    now = pygame.time.get_ticks()
                    if now - last >= cooldown:
                        last = now
                        if pygame.sprite.spritecollide(bullet, AllSettings.enemie_list,dokill=False):
                            Health -= 1
                            AllSettings.bullet_list.remove(bullet)
                            AllSettings.all_sprites_list.remove(bullet)


                    if Health == 0:
                        bol = True
                        enemie_hit_list = pygame.sprite.spritecollide(bullet, AllSettings.enemie_list, bol)
                        Health = 4
                        for enemies in enemie_hit_list:
                            expl = Animations.Explosion(enemies.rect.center)
                            AllSettings.all_sprites_list.add(expl)
                            AllSettings.bullet_list.remove(bullet)
                            AllSettings.all_sprites_list.remove(bullet)
                            coins += 15

                    if bullet.rect.y < -5:
                        AllSettings.bullet_list.remove(bullet)
                        AllSettings.all_sprites_list.remove(bullet)


                for bulletback in AllSettings.bulletback_list:
                    now = pygame.time.get_ticks()
                    if now - last >= cooldown:
                        last = now
                        if pygame.sprite.groupcollide(AllSettings.bulletback_list, AllSettings.player_list,False,False):
                            PlayerHealth -= 1
                            AllSettings.bulletback_list.remove(bulletback)
                            AllSettings.all_sprites_list.remove(bulletback)
                            


                if PlayerHealth == 0:
                    Playerhit_list = pygame.sprite.groupcollide(AllSettings.bulletback_list,AllSettings.player_list,True,True)
                    for player in Playerhit_list:
                        print("fefdsf")
                        expl = Animations.Explosion(player.rect.center)
                        AllSettings.all_sprites_list.add(expl)
                        AllSettings.bulletback_list.remove(bulletback)
                        AllSettings.all_sprites_list.remove(bulletback)
                        AllSettings.player_list.remove(player)
                        AllSettings.all_sprites_list.remove(player)
                        
                        if bulletback.rect.y > AllSettings.screen_height:
                            AllSettings.bulletback_list.remove(bulletback)
                            AllSettings.all_sprites_list.remove(bulletback)


                font_obj = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
                textcoin = font_obj.render(str(coins)+"💰", True, AllSettings.Yellow)


                font_obj2 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
                Playerhealth = font_obj2.render(AllSettings.Playername, True, AllSettings.Lightgrey)
                            
                font_obj3 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
                textenemie = font_obj3.render(AllSettings.enemiename, True, AllSettings.Lightgrey)

                font_obj1 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 64)
                won = font_obj1.render("Congrats you won!", True, AllSettings.Yellow)

                font_obj4 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 48)
                loose = font_obj4.render("imagine you Loose in this Game!", True, AllSettings.Yellow)



                DISPLAY.blit(AllSettings.background, (0, 0))
                DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.2))
                DISPLAY.blit(textenemie,(AllSettings.screen_width/1.16, AllSettings.screen_height/1.19))
                DISPLAY.blit(Playerhealth,(AllSettings.screen_width/15, AllSettings.screen_height/1.19))
                barPos= (AllSettings.screen_width/1.16, AllSettings.screen_height/1.15)
                barPos2= (AllSettings.screen_width/15, AllSettings.screen_height/1.15)
                Enemy.Enemie.DrawBar(barPos, AllSettings.barSize, AllSettings.borderColor, AllSettings.barColor, Health/AllSettings.max_a)
                Player.Player.DrawBar(barPos2, AllSettings.barSize2, AllSettings.borderColor2, AllSettings.barColor2, PlayerHealth/AllSettings.max_a2)

                AllSettings.all_sprites_list.draw(DISPLAY)

                if AllSettings.all_sprites_list.has(AllSettings.player_list) == False:

                    winmenu = Settingwindow.ButtonwinMenu()
                    DISPLAY.blit(AllSettings.background,(0,0))
                    DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.4))
                    DISPLAY.blit(loose,(AllSettings.screen_width/6,AllSettings.screen_height/4))


                    winmenu.draw()
                if AllSettings.all_sprites_list.has(AllSettings.enemie_list) == False:

                    winmenu = Settingwindow.ButtonwinMenu()
                    DISPLAY.blit(AllSettings.background,(0,0))
                    DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.4))
                    DISPLAY.blit(won,(AllSettings.screen_width/4,AllSettings.screen_height/4))


                    winmenu.draw()
                pygame.display.update()