
import time
import pygame
from pygame.locals import *
import os
import AllSettings
import Animations
import Enemy
import Player
from threading import Thread
import Database


class game():
    is_running: bool
    time_left: int
    player: Player.Player
    coins_earned: int
    
    def __init__(self,player: Player.Player):
        self.is_running = True
        self.time_left = 10 #time left 
        self.player = player
        self.coins_earned = 0
        
        AllSettings.music.stop()

        self.thread_timer = Thread(target=self.timer)
        self.thread_timer.start()

        self.all_sprites_list = pygame.sprite.Group()
        self.enemie_list = pygame.sprite.Group()
        self.bullet_f_player_list = pygame.sprite.Group()
        self.bullet_f_enemy_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.GroupSingle()
        
        #init player and add to sprite list to draw him
        self.player.add_sprite = self.add_sprites_to_list
        self.player.add_bullet= self.add_bullet_player_to_list
        self.player.stop_game= self.stop_game
        self.player.resume_game= self.resume_game
        
        self.player_list.add(self.player)
        self.all_sprites_list.add(self.player)
        self.player.rect.x = 200
        
        for i in range(10):
            en = Enemy.Enemie(add_sprite= self.add_sprites_to_list, add_bullet= self.add_bullet_enemy_to_list,player= self.player)
            if not self.all_sprites_list.has(en): 
                self.enemie_list.add(en)
                self.all_sprites_list.add(en)
   

    def add_sprites_to_list(self,sprite):
        self.all_sprites_list.add(sprite)

    def add_bullet_player_to_list(self,sprite):
        self.bullet_f_player_list.add(sprite)

    def add_bullet_enemy_to_list(self,sprite):
        self.bullet_f_enemy_list.add(sprite)


    def explode_enemy(self,enemy):
        expl = Animations.Explosion(enemy.rect.center)
        enemy.kill_healthbar()
        enemy.kill()
        self.add_sprites_to_list(expl)
        self.player.add_coins(5)
        self.coins_earned += 5
        self.time_left += 5
        if self.player.health <= 15:
            self.player.health += 1


    def check_for_hit_at_enemy(self,bullet: pygame.sprite.Sprite):
        enemy: Enemy.Enemie
        for enemy in pygame.sprite.spritecollide(bullet, self.enemie_list,dokill=False):
            enemy.health -= 1
            self.bullet_f_player_list.remove(bullet)
            self.all_sprites_list.remove(bullet)
            if enemy.health == 0:
                self.explode_enemy(enemy)


    def explode_player(self,player: Player.Player):
        expl = Animations.Explosion(player.rect.center)
        self.all_sprites_list.add(expl)
        self.bullet_f_enemy_list.empty()
        
        self.player_list.remove(player)
        self.all_sprites_list.remove(player)


    def check_for_hit_at_player(self,bullet: pygame.sprite.Sprite):
        player: Player.Player
        for player in pygame.sprite.spritecollide(bullet, self.player_list,dokill=False):
            player.health -= 1
            self.bullet_f_enemy_list.remove(bullet)
            self.all_sprites_list.remove(bullet)

    def stop_game(self):
        self.is_running = False
        
    def resume_game(self):
        self.is_running = True

 
    def timer(self):
        while self.is_running: 
            time.sleep(1)
            self.time_left -= 1 
    
    def reset(self):
        self.player.health = self.player.standart_health
        self.__init__(self.player)     

    def runit(self):
        while self.is_running: # while loop for game logic 
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.is_running = False
                    pygame.quit()
                    exit()

            # update all sprites
            self.all_sprites_list.update()
            
            # check for bullet hits at enemie
            for bullet in self.bullet_f_player_list:
                self.check_for_hit_at_enemy(bullet=bullet)

                # if bullet out of playground => remove
                if bullet.rect.y < -5: 
                    self.bullet_f_player_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
            
            # check for bullet hits on player
            for bullet in self.bullet_f_enemy_list:
                self.check_for_hit_at_player(bullet=bullet)

                if bullet.rect.y > AllSettings.screen_height: # display high
                    self.bullet_f_enemy_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

            # if time is over player dies            
            if self.time_left <= 0:
                self.player.health = 0

            # if player is dead => remove all from sprite list
            if self.player.health == 0:
                self.explode_player(self.player)

            # canvas drawing shit
            font_obj = pygame.font.Font(os.path.join("data/fonts","OpenSansEmoji.ttf"), 64)
            textcoin = font_obj.render("+"+str(self.player.coins)+"💰", True, AllSettings.Yellow)

            font_obj2 = pygame.font.Font(os.path.join("data/fonts",'freesansbold.ttf'), 20)
            PlayerName = font_obj2.render(self.player.name, True, AllSettings.Lightgrey)

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

            self.all_sprites_list.draw(AllSettings.DISPLAY)
            self.player.DrawHealthBar()
            
            # if sprite list not contains player (player is dead)
            if self.player.health <= 0 or not self.all_sprites_list.has(self.enemie_list): 
                self.is_running = False
                db = Database.Database()
                db.db_add_coins(player=self.player,amount=self.coins_earned)
                end_screen = End_Screen(coins=self.coins_earned,won=self.player.health > 0)
                thread_end_screen = Thread(target=end_screen.show())
                thread_end_screen.start()
                
            
            pygame.display.update()

class End_Screen():
    is_running: bool
    coins: int
    won: bool
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
            AllSettings.DISPLAY.blit(textcoin,(AllSettings.screen_width/2.45,AllSettings.screen_height/2.5))
            
            if self.won:
                AllSettings.DISPLAY.blit(won,(AllSettings.screen_width/6,AllSettings.screen_height/4))
            else: AllSettings.DISPLAY.blit(loose,(AllSettings.screen_width/6,AllSettings.screen_height/4))
            
            end_screen_menu_button.draw(end_screen=self.stop_end_screen)
            pygame.display.flip()
            
            
class End_Screen_Menu_Button():
    image: pygame.Surface
    rect: pygame.Rect
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
                    