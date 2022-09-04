
import pygame.gfxdraw
import time
import pygame, pygame.mixer
from pygame.locals import *
import os
import random
import AllSettings
import Animations
import Enemy
import Player
import Settingwindow
from threading import Thread
class rungame():
    def timer():
        while not AllSettings.kill:
            time.sleep(1)
            AllSettings.zeit -= 1
            print(AllSettings.zeit)

    def runit():
            AllSettings.music.stop()
            thread_timer = Thread(target=rungame.timer)
            thread_timer.start()
            cooldown0 = 1200
            last0 = pygame.time.get_ticks()
            player = Player.Player()
            AllSettings.player_list.add(player)
            AllSettings.all_sprites_list.add(player)
            for i in range(10):
                en = Enemy.Enemie()
                if AllSettings.all_sprites_list.has(en) == False: 

                    AllSettings.enemie_list.add(en)
                    AllSettings.all_sprites_list.add(en)

            cooldown = 300
            last = pygame.time.get_ticks()
            while not AllSettings.level1run:
                dt = AllSettings.clock.tick(60)
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type==QUIT:
                        AllSettings.kill = True
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
                            AllSettings.Health -= 1
                            AllSettings.bullet_list.remove(bullet)
                            AllSettings.all_sprites_list.remove(bullet)


                    if AllSettings.Health == 0:
                        bol = True
                        enemie_hit_list = pygame.sprite.spritecollide(bullet, AllSettings.enemie_list, bol)
                        AllSettings.Health = 4
                        for enemies in enemie_hit_list:
                            expl = Animations.Explosion(enemies.rect.center)
                            AllSettings.all_sprites_list.add(expl)
                            AllSettings.bullet_list.remove(bullet)
                            AllSettings.all_sprites_list.remove(bullet)
                            AllSettings.coins += 5
                            AllSettings.zeit += 5
                            if AllSettings.PlayerHealth <= 15:
                                AllSettings.PlayerHealth += 1
                    if bullet.rect.y < -5: 
                        AllSettings.bullet_list.remove(bullet)
                        AllSettings.all_sprites_list.remove(bullet)


                for bulletback in AllSettings.bulletback_list:
                    now = pygame.time.get_ticks()
                    if now - last >= cooldown:
                        last = now
                        if pygame.sprite.groupcollide(AllSettings.bulletback_list, AllSettings.player_list,False,False):
                            AllSettings.PlayerHealth -= 1
                            AllSettings.bulletback_list.remove(bulletback)
                            AllSettings.all_sprites_list.remove(bulletback)
                            
                if AllSettings.zeit <= 0:
                    AllSettings.PlayerHealth = 0

                if AllSettings.PlayerHealth == 0:
                    Playerhit_list = pygame.sprite.groupcollide(AllSettings.bulletback_list,AllSettings.player_list,True,True)
                    for player in Playerhit_list:
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
                textcoin = font_obj.render("+"+str(AllSettings.coins)+"💰", True, AllSettings.Yellow)

                font_obj2 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
                Playerhealth = font_obj2.render(AllSettings.Playername, True, AllSettings.Lightgrey)
                            
                font_obj3 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
                textenemie = font_obj3.render(AllSettings.enemiename, True, AllSettings.Lightgrey)

                font_obj1 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 64)
                won = font_obj1.render("Congrats you won!", True, AllSettings.Yellow)

                font_obj4 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 48)
                loose = font_obj4.render("imagine you Loose in this Game!", True, AllSettings.Yellow)

                font_obj5 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
                timer = font_obj5.render("Time Left: "+str(AllSettings.zeit)+" s", True, AllSettings.Yellow)


                AllSettings.DISPLAY.blit(AllSettings.background, (0, 0))
                AllSettings.DISPLAY.blit(timer,(AllSettings.screen_width/1.5, AllSettings.screen_height/36))
                AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.2))
                AllSettings.DISPLAY.blit(textenemie,(AllSettings.screen_width/1.16, AllSettings.screen_height/1.195))
                AllSettings.DISPLAY.blit(Playerhealth,(AllSettings.screen_width/15, AllSettings.screen_height/1.195))
                barPos= (AllSettings.screen_width/1.16, AllSettings.screen_height/1.15)
                barPos2= (AllSettings.screen_width/15, AllSettings.screen_height/1.15)
                Enemy.Enemie.DrawBar(barPos, AllSettings.barSize, AllSettings.borderColor, AllSettings.barColor, AllSettings.Health/AllSettings.max_a)
                Player.Player.DrawBar(barPos2, AllSettings.barSize2, AllSettings.borderColor2, AllSettings.barColor2, AllSettings.PlayerHealth/AllSettings.max_a2)

                AllSettings.all_sprites_list.draw(AllSettings.DISPLAY)

                if AllSettings.all_sprites_list.has(AllSettings.player_list) == False:
                    AllSettings.kill = True
                    winmenu = Settingwindow.ButtonwinMenu()
                    if AllSettings.login == True:
                        dbcoins = str(AllSettings.collection.find_one({"Name":"Admin"},{ "_id": 0,"Coins": 1}))
                        dbcoins = dbcoins.strip("{'Coins': }")
                        Coins = int(dbcoins) + AllSettings.coins
                        AllSettings.collection.find_one_and_update({"Name":"Admin"}, {"$set" : {"Coins": Coins}})
                    AllSettings.DISPLAY.blit(AllSettings.background,(0,0))
                    AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.4))
                    AllSettings.DISPLAY.blit(loose,(AllSettings.screen_width/6,AllSettings.screen_height/4))
                    
                    winmenu.draw()

                if AllSettings.all_sprites_list.has(AllSettings.enemie_list) == False:
                    AllSettings.kill = True
                    winmenu = Settingwindow.ButtonwinMenu()
                    if AllSettings.login == True:
                        dbcoins = str(AllSettings.collection.find_one({"Name":"Admin"},{ "_id": 0,"Coins": 1}))
                        dbcoins = dbcoins.strip("{'Coins': }")
                        Coins = int(dbcoins) + AllSettings.coins
                        AllSettings.collection.find_one_and_update({"Name":"Admin"}, {"$set" : {"Coins": Coins}})
                    AllSettings.DISPLAY.blit(AllSettings.background,(0,0))
                    AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.4))
                    AllSettings.DISPLAY.blit(won,(AllSettings.screen_width/4,AllSettings.screen_height/4))
                    

                    winmenu.draw()
                pygame.display.update()

