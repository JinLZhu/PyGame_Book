# 游戏类Game, 对游戏显示和控制起主要作用的类
import pygame
from hero import Hero

from PyGame.Aircraft.AirCraft.background import Background
from status import Status


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
            pass
        elif self.status.status == Status.RUN:
            # check and respond run button
            pass
        elif self.status.status == Status.PAUSE:
            # check and respond pause/resume button
            pass
        elif self.status.status == Status.GAMEOVER:
            # check and respond restart button
            # check and respond exit button
            pass

    def handle_mousemotion_event(self, event):
        if self.status.status == Status.RUN:
            if event.button(0):
                # update hero
                self.hero.update(event.pos)

            # update pause/resume button

    def update_bullets(self):
        # create bullet:
        # move bullets
        pass

    def update_enemies(self):
        # create enemy:
        # move enemies
        pass

    def handle_collision(self):
        # check bullets & enemies collision
        # check hero & enemies collision
        pass

    def update_screen(self):
        # draw background
        self.bg.draw(self.surface)

        if self.status.status == Status.WELCOME:
            # draw logo
            # draw start button
            pass
        elif self.status.status == Status.RUN or self.status.status == Status.PAUSE:
            # draw hero
            self.hero.draw(self.surface)
            # draw bullets
            # draw enemies
            # draw pause/resume button
            # draw scoreboard
            pass
        elif self.status.status == Status.GAMEOVER:
            # draw end promt rectangle
            # draw restart button
            # draw exit button
            pass

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