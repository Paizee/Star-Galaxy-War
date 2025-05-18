
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


class game():
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
                expl = Animations.Explosion(enemy.rect.center)
                enemy.kill_healthbar()
                enemy.kill()
                add_sprites_to_list(expl)
                player.add_coins(5)
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
                textcoin = font_obj.render("+"+str(player.coins)+"💰", True, AllSettings.Yellow)

                font_obj2 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
                PlayerName = font_obj2.render(player.name, True, AllSettings.Lightgrey)

                font_obj1 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 64)
                won = font_obj1.render("Congrats you won!", True, AllSettings.Yellow)

                font_obj4 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 48)
                loose = font_obj4.render("imagine you Loose in this Game!", True, AllSettings.Yellow)

                font_obj5 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 32)
                timer = font_obj5.render("Time Left: "+str(self.time_left)+" s", True, AllSettings.Yellow)


                AllSettings.DISPLAY.blit(AllSettings.background, (0, 0))
                AllSettings.DISPLAY.blit(timer,(AllSettings.screen_width/1.5, AllSettings.screen_height/36))
                AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.2))
                AllSettings.DISPLAY.blit(PlayerName,(AllSettings.screen_width/15, AllSettings.screen_height/1.195))

                all_sprites_list.draw(AllSettings.DISPLAY)
                player.DrawHealthBar()
                
                # if sprite list not contains player (player is dead)
                if not all_sprites_list.has(player_list) or not all_sprites_list.has(enemie_list): 
                    self.is_running = False
                    end_screen = End_Screen(coins=player.coins,won=all_sprites_list.has(player_list))
                    thread_lev1 = Thread(target=end_screen.show())
                    thread_lev1.start()
                    

                pygame.display.update()

class End_Screen():
    def __init__(self,coins,won):
        self.is_running = True
        self.coins = coins
        self.won = won
        
    def stop_end_screen(self):
        self.is_running = False  

    def show(self):
        if self.won:
            font_obj1 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 64)
            won = font_obj1.render("Congrats you won!", True, AllSettings.Yellow)
        else: 
            font_obj4 = pygame.font.Font(os.path.join("data/fonts","Starjedi.ttf"), 48)
            loose = font_obj4.render("imagine you Loose in this Game!", True, AllSettings.Yellow)
        
        font_obj = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
        textcoin = font_obj.render(f"+ {self.coins} 💰", True, AllSettings.Yellow)
        
        end_screen_menu_button = End_Screen_Menu_Button()
        while self.is_running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                    
            pos = pygame.mouse.get_pos()
            if not end_screen_menu_button.rect.collidepoint(pos):
                    pygame.mouse.set_system_cursor(SYSTEM_CURSOR_ARROW)
             
                                
            AllSettings.DISPLAY.blit(AllSettings.background,(0,0))
            AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/2.2,AllSettings.screen_height/2.4))
            
            if self.won:
                AllSettings.DISPLAY.blit(won,(AllSettings.screen_width/6,AllSettings.screen_height/4))
            else: AllSettings.DISPLAY.blit(loose,(AllSettings.screen_width/6,AllSettings.screen_height/4))
            
            end_screen_menu_button.draw(end_screen=self.stop_end_screen)
            pygame.display.update()
            
            
class End_Screen_Menu_Button():

    def __init__(self):
        self.image = AllSettings.butMenu1
        self.rect = self.image.get_rect()
        self.rect.x = AllSettings.screen_width/2.5
        self.rect.y = AllSettings.screen_height/1.5

    def draw(self,end_screen):
        AllSettings.DISPLAY.blit(self.image,(self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                AllSettings.click.play()
                end_screen()
                    