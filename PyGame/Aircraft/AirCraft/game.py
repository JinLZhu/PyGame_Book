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