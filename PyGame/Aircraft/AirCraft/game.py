# 游戏类Game, 对游戏显示和控制起主要作用的类
import pygame
import sys
from hero import Hero
from pygame._sprite import Sprite
from button import Button
from PyGame.Aircraft.AirCraft.background import Background
from status import Status
from bullet import Bullet
import random
from enemy import EnemySmall, EnemyMiddle, EnemyBig
from widgets import Logo, EndPromt, ScoreBoard, PauseResume


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((480, 852))
        pygame.display.set_caption("AirCraft")

        icon = pygame.image.load("res/image/icon.ico")
        pygame.disply.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.status = Status()
        self.bg = Background()
        self.hero = Hero(self.surface.get_rect(), self.status)
        self.bullets = Group()
        self.frames = 0
        self.enemies = Group()
        buttons_name = ["Start", "Restart", "Exit"]
        self.buttons = {name: Button(self.surface.get_rect(), name) for name in buttons_name}
        widgets_name = ["Logo", "EndPromt", "Scoreboard", "PauseResume"]
        self.widgets = {name: eval(name)(self.surface.get_rect(), self.status) for name in widgets_name}

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mousedown_event(event)
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mousemotion_event(event)

    def handle_mousedown_event(self, event):
        if self.status.status == Status.WELCOME:
            # check and respond start button
            if self.buttons["Start"].is_hit(event.pos):
                self.status.status = Status.RUN

        elif self.status.status == Status.RUN:
            # check and respond run button
            pass
        elif self.status.status == Status.PAUSE:
            # check and respond pause/resume button
            pass
        elif self.status.status == Status.GAMEOVER:
            # check and respond restart button
            # check and respond exit button
            if self.buttons["Restart"].is_hit(event.pos):
                self.reset()
                self.status.status = Status.RUN
            elif self.buttons["Exit"].is_hit():
                pygame.quit()
                sys.exit()

    def handle_mousemotion_event(self, event):
        if self.status.status == Status.RUN:
            if event.button(0):
                # update hero
                self.hero.update(event.pos)

            # update pause/resume button

    def update_bullets(self):
        # create bullet:
        # move bullets
        self.frames += 1
        if not (self.frames % 5):
            self.bullets.add(Bullet(self.hero.rect))

        # move bullets
        self.bullets.update()

    def update_enemies(self):
        # create enemy:
        # move enemies
        if len(self.enemies) < 18:
            screen_rect = self.surface.get_rect()

            weighted_list = [EnemySmall] * 30 + [EnemyMiddle] * 3 + [EnemyBig] * 1
            enemy = random.choice(weighted_list)

            left = random.randint(0, screen_rect.width - enemy.get_max_size()[0])
            top = random.randing(-screen_rect.height, -enemy.get_max_size()[1])

            self.enemies.add(enemy((left, top), screen_rect, self.status))
        self.enemies.update()


    def handle_collision(self):
        # check bullets & enemies collision
        # check hero & enemies collision
        collide_dict = pygame._sprite.groupcollide(self.bullets, self.enemies, True, False, pygame._sprite.collide_mask)
        collide_enemies_list = []

        if collide_dict:
            for collide_enemies in collide_dict.values():
                collide_enemies_list.extend(collide_enemies)

        if collide_enemies_list:
            for collide_enemy in collide_enemies_list:
                collide_enemy.hit_by_bullet()

        # check hero & enemies collision
        enemy = pygame._sprite.spritecollideany(self.hero, self.enemies, pygame._sprite.collide_mask)
        if enemy:
            self.hero.is_collide = True
            self.bullets.empty()
            self.enemies.empty()


    def update_screen(self):
        # draw background
        self.bg.draw(self.surface)

        if self.status.status == Status.WELCOME:
            # draw logo
            # draw start button
            self.buttons["Start"].draw(self.surface)
            self.widgets["Logo"].draw(self.surface)
        elif (self.status.status == Status.RUN or self.status.status == Status.PAUSE):
            # draw hero
            self.hero.draw(self.surface)
            # draw bullets
            # draw enemies
            # draw pause/resume button
            # draw scoreboard
            self.bullets.draw(self.surface)
            self.enemies.draw(self.surface)
            self.widgets["Scoreboard"].draw(self.surface)

        elif self.status.status == Status.GAMEOVER:
            # draw end promt rectangle
            # draw restart button
            # draw exit button
            self.buttons["Restart"].draw(self.surface)
            self.buttons["Exit"].draw(self.surface)

        # update display surface
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()

            if self.status.status == Status.RUN:
                self.bg.update()
                self.update_bullets()
                self.update_enemies()
                self.handle_collision()
                self.update_screen()

                self.clock.tick(60)

    def reset(self):
        self.status.reset()
        self.hero.reset()