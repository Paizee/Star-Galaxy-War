
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
    is_running = True
    time_left = 10 #time left 
    
    def __init__(self):
        self.start_it = self.runit()
        

    def timer(self):
        while self.is_running: 
            time.sleep(1)
            self.time_left -= 1 

    def runit(self):
            AllSettings.music.stop()

            thread_timer = Thread(target=self.timer)
            thread_timer.start()

            last0 = pygame.time.get_ticks()
            last = pygame.time.get_ticks()

            all_sprites_list = pygame.sprite.Group()
            explosion_list = pygame.sprite.Group()
            enemie_list = pygame.sprite.Group()
            enemie_list2 = pygame.sprite.Group()
            bullet_f_player_list = pygame.sprite.Group()
            bullet_f_enemy_list = pygame.sprite.Group()
            player_list = pygame.sprite.GroupSingle()

            def add_sprites_to_list(sprite):
                all_sprites_list.add(sprite)

            def add_bullet_player_to_list(sprite):
                bullet_f_player_list.add(sprite)

            def add_bullet_enemy_to_list(sprite):
                bullet_f_enemy_list.add(sprite)

            def explode_enemy(enemy: Enemy.Enemie):
                enemy.kill
                expl = Animations.Explosion(enemy.rect.center)
                add_sprites_to_list(expl)
                bullet_f_player_list.remove(bullet)
                all_sprites_list.remove(bullet)
                coins.own_coins.add(5)
                self.time_left += 5
                if player.health <= 15:
                    player.health += 1

            def check_for_hit_at_enemy(bullet: pygame.sprite.Sprite):
                enemy: Enemy.Enemie
                for enemy in pygame.sprite.spritecollide(bullet, enemie_list,dokill=False):
                    enemy.health -= 1
                    bullet_f_player_list.remove(bullet)
                    all_sprites_list.remove(bullet)
                    if enemy.health == 0:
                        explode_enemy(enemy)

            def explode_player(player: Player.Player):
                expl = Animations.Explosion(player.rect.center)
                all_sprites_list.add(expl)
                bullet_f_enemy_list.empty()
                
                player_list.remove(player)
                all_sprites_list.remove(player)

            def check_for_hit_at_player(bullet: pygame.sprite.Sprite):
                player: Player.Player
                for player in pygame.sprite.spritecollide(bullet, player_list,dokill=False):
                    player.health -= 1
                    player.DrawHealthBar()
                    bullet_f_enemy_list.remove(bullet)
                    all_sprites_list.remove(bullet)

            def stop_game():
                self.is_running = False
            
            #init player and add to sprite list to draw him
            player = Player.Player(add_sprite= add_sprites_to_list, add_bullet= add_bullet_player_to_list, stop_game=stop_game)
            player_list.add(player)
            all_sprites_list.add(player)
            player.rect.x = 200

            #spawn enemies
            for i in range(10):
                en = Enemy.Enemie(add_sprite= add_sprites_to_list, add_bullet= add_bullet_enemy_to_list)
                if all_sprites_list.has(en) == False: 
                    enemie_list.add(en)
                    all_sprites_list.add(en)

            

            while self.is_running: # while loop for game logic 
                for event in pygame.event.get():
                    if event.type==QUIT:
                        self.is_running = False
                        pygame.quit()
                        exit()
                

                # update all sprites
                all_sprites_list.update()
                
                # check for bullet hits at enemie
                for bullet in bullet_f_player_list:
                    check_for_hit_at_enemy(bullet=bullet)

                    # if bullet out of playground => remove
                    if bullet.rect.y < -5: 
                        bullet_f_player_list.remove(bullet)
                        all_sprites_list.remove(bullet)
                
                # check for bullet hits on player
                for bullet in bullet_f_enemy_list:
                    check_for_hit_at_player(bullet=bullet)

                    if bullet.rect.y > AllSettings.screen_height: # display high
                        bullet_f_enemy_list.remove(bullet)
                        all_sprites_list.remove(bullet)

                # if time is over player dies            
                if self.time_left <= 0:
                    player.health = 0

                # if player is dead => remove all from sprite list
                if player.health == 0:
                    explode_player(player)

                # canvas drawing shit
                font_obj = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
                textcoin = font_obj.render("+"+str(coins.own_coins.amount)+"💰", True, AllSettings.Yellow)

                font_obj2 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
                PlayerName = font_obj2.render(AllSettings.Playername, True, AllSettings.Lightgrey)
                            
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
                AllSettings.DISPLAY.blit(PlayerName,(AllSettings.screen_width/15, AllSettings.screen_height/1.195))

                all_sprites_list.draw(AllSettings.DISPLAY)

                # if sprite list not contains player (player is dead)
                if all_sprites_list.has(player_list) == False:
                    self.is_running = False
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
                if all_sprites_list.has(enemie_list) == False:
                    self.is_running = False
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

