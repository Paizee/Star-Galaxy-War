
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
import coins


class rungame():
    def __init__(self):
        self.cooldown0 = 1200 #bullet
        self.cooldown = 300 #bullet
        self.dur = 60 #bullet
        self.time_left = 10 #time left 
        self.start_it = self.runit()
        self.all_sprites_list = pygame.sprite.Group()
        self.explosion_list = pygame.sprite.Group()
        self.enemie_list = pygame.sprite.Group()
        self.enemie_list2 = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.bulletback_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.GroupSingle()

    def timer(self):
        while not AllSettings.kill: 
            time.sleep(1)
            self.time_left -= 1 

    def add_sprites_to_list(self, sprite):
        self.all_sprites_list.add(sprite)

    def add_bullet_to_list(self, sprite):
        self.bullet_list.add(sprite)

    def runit(self):
            AllSettings.music.stop()

            thread_timer = Thread(target=self.timer)
            thread_timer.start()

            last0 = pygame.time.get_ticks()
            last = pygame.time.get_ticks()

            #init player and add to sprite list to draw him
            player = Player.Player(game=self)
            self.player_list.add(player)
            self.all_sprites_list.add(player)

            player.rect.x = 200
            #spawn enemies
            for i in range(10):
                en = Enemy.Enemie()
                if self.all_sprites_list.has(en) == False: 
                    self.enemie_list.add(en)
                    self.all_sprites_list.add(en)

            

            while not AllSettings.level1run: # while loop for game logic 
                for event in pygame.event.get():
                    if event.type==QUIT:
                        AllSettings.kill = True
                        pygame.quit()
                        exit()
                

                # update all sprites
                self.all_sprites_list.update()

                # timer for enemy to shoot back
                for i in range(self.dur):
                    now = pygame.time.get_ticks()
                    if now - last0 >= self.cooldown0:
                        last0 = now
                        Enemy.Enemie.shootback()
                
                # check for bullet hits at enemie
                for bullet in self.bullet_list:
                    now = pygame.time.get_ticks()
                    if now - last >= self.cooldown:
                        last = now
                        if pygame.sprite.spritecollide(bullet, self.enemie_list,dokill=False):
                            AllSettings.Health -= 1
                            self.bullet_list.remove(bullet)
                            self.all_sprites_list.remove(bullet)

                    # if last bullet hits => enemie explodes and add coins
                    if AllSettings.Health == 0:
                        bol = True
                        enemie_hit_list = pygame.sprite.spritecollide(bullet, self.enemie_list, bol)
                        AllSettings.Health = 4
                        for enemies in enemie_hit_list:
                            expl = Animations.Explosion(enemies.rect.center)
                            self.all_sprites_list.add(expl)
                            self.bullet_list.remove(bullet)
                            self.all_sprites_list.remove(bullet)
                            coins.own_coins.add(5)
                            self.time_left += 5
                            if AllSettings.PlayerHealth <= 15:
                                AllSettings.PlayerHealth += 1

                    # if bullet out of playground => remove
                    if bullet.rect.y < -5: 
                        self.bullet_list.remove(bullet)
                        self.all_sprites_list.remove(bullet)
                
                # check for bullet hits on player
                for bulletback in self.bulletback_list:
                    now = pygame.time.get_ticks()
                    if now - last >= self.cooldown:
                        last = now
                        if pygame.sprite.groupcollide(self.bulletback_list, self.player_list,False,False):
                            AllSettings.PlayerHealth -= 1
                            self.bulletback_list.remove(bulletback)
                            self.all_sprites_list.remove(bulletback)

                # if time is over player dies            
                if self.time_left <= 0:
                    AllSettings.PlayerHealth = 0

                # if player is dead => remove all from sprite list
                if AllSettings.PlayerHealth == 0:
                    Playerhit_list = pygame.sprite.groupcollide(self.bulletback_list,self.player_list,True,True)
                    for player in Playerhit_list:
                        expl = Animations.Explosion(player.rect.center)
                        self.all_sprites_list.add(expl)
                        self.bulletback_list.remove(bulletback)
                        self.all_sprites_list.remove(bulletback)
                        self.player_list.remove(player)
                        self.all_sprites_list.remove(player)
                        
                        if bulletback.rect.y > AllSettings.screen_height:
                            self.bulletback_list.remove(bulletback)
                            self.all_sprites_list.remove(bulletback)

                # canvas drawing shit
                font_obj = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
                textcoin = font_obj.render("+"+str(coins.own_coins.amount)+"💰", True, AllSettings.Yellow)

                font_obj2 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
                Playerhealth = font_obj2.render(AllSettings.Playername, True, AllSettings.Lightgrey)
                            
                font_obj3 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
                textenemie = font_obj3.render(AllSettings.enemiename, True, AllSettings.Lightgrey)

                font_obj1 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 64)
                won = font_obj1.render("Congrats you won!", True, AllSettings.Yellow)

                font_obj4 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 48)
                loose = font_obj4.render("imagine you Loose in this Game!", True, AllSettings.Yellow)

                font_obj5 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
                timer = font_obj5.render("Time Left: "+str(self.time_left)+" s", True, AllSettings.Yellow)


                AllSettings.DISPLAY.blit(AllSettings.background, (0, 0))
                AllSettings.DISPLAY.blit(timer,(AllSettings.screen_width/1.5, AllSettings.screen_height/36))
                AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.2))
                AllSettings.DISPLAY.blit(textenemie,(AllSettings.screen_width/1.16, AllSettings.screen_height/1.195))
                AllSettings.DISPLAY.blit(Playerhealth,(AllSettings.screen_width/15, AllSettings.screen_height/1.195))
                barPos= (AllSettings.screen_width/1.16, AllSettings.screen_height/1.15)
                barPos2= (AllSettings.screen_width/15, AllSettings.screen_height/1.15)
                Enemy.Enemie.DrawBar(barPos, AllSettings.barSize, AllSettings.borderColor, AllSettings.barColor, AllSettings.Health/AllSettings.max_a)
                Player.Player.DrawBar(barPos2, AllSettings.barSize2, AllSettings.borderColor2, AllSettings.barColor2, AllSettings.PlayerHealth/AllSettings.max_a2)
                self.all_sprites_list.draw(AllSettings.DISPLAY)

                # if sprite list not contains player (player is dead)
                if self.all_sprites_list.has(self.player_list) == False:
                    AllSettings.kill = True
                    winmenu = Settingwindow.ButtonwinMenu()
                    if AllSettings.login == True:
                        #dbcoins = str(AllSettings.collection.find_one({"Name":"Admin"},{ "_id": 0,"Coins": 1}))
                        dbcoins = dbcoins.strip("{'Coins': }")
                        #AllSettings.collection.find_one_and_update({"Name":"Admin"}, {"$set" : {"Coins": Coins}})
                    AllSettings.DISPLAY.blit(AllSettings.background,(0,0))
                    AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.4))
                    AllSettings.DISPLAY.blit(loose,(AllSettings.screen_width/6,AllSettings.screen_height/4))
                    
                    winmenu.draw()
                # if sprite lsit not contains enemie (player won)
                if self.all_sprites_list.has(self.enemie_list) == False:
                    AllSettings.kill = True
                    winmenu = Settingwindow.ButtonwinMenu()
                    if AllSettings.login == True:
                        #dbcoins = str(AllSettings.collection.find_one({"Name":"Admin"},{ "_id": 0,"Coins": 1}))
                        dbcoins = dbcoins.strip("{'Coins': }")
                        #AllSettings.collection.find_one_and_update({"Name":"Admin"}, {"$set" : {"Coins": Coins}})
                    AllSettings.DISPLAY.blit(AllSettings.background,(0,0))
                    AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.4))
                    AllSettings.DISPLAY.blit(won,(AllSettings.screen_width/4,AllSettings.screen_height/4))
                    

                    winmenu.draw()
                pygame.display.update()

