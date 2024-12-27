# 游戏类Game, 对游戏显示和控制起主要作用的类
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((480, 852))
        pygame.display.set_caption("AirCraft")

        icon = pygame.image.load("res/image/icon.ico")
        pygame.disply.set_icon(icon)