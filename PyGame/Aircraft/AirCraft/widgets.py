# 定义界面上的小部件类，
# Logo类显示“飞机大战”Logo;
# EndPromt类用来显示结束界面上的提示方框
# Scoreboard类用来显示记分牌
# PauseResume类用来显示和控制暂停/恢复按钮
import pygame

from image import Image


class Logo:
    def __init__(self, *args):
        screen_rect = args[0]
        self.image = Image.logo
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.centery - 150

    def draw(self, display_surface):
        display_surface.blit(self.image, self.rect)


class ScoreBoard:
    def __init__(self, *args):
        self.status = args[1]
        self.score_color = (0, 0, 0)
        self.font = pygame.font.Font("res/font/comici.ttf, 35")

    def draw(self, display_surface):
        score_image = self.font.render(str(self.status.score), True, self.score_color)



class PauseResume:
    def __init__(self, *args):
        pass


class EndPromt:
    def __init__(self, *args):
        pass