# 游戏类Game, 对游戏显示和控制起主要作用的类
import pygame
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
                pass

            # update pause/resume button


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