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
        self.font = pygame.font.Font("res/font/comici.ttf", 35)

    def draw(self, display_surface):
        score_image = self.font.render(str(self.status.score), True, self.score_color)



class PauseResume:
    # Pause and resume status
    PAUSE_NORMAL, PAUSE_PASSED, RESUME_NORMAL, RESUME_PRESSED = range(4)

    def __init__(self, *args):
        self.images = Image.pause_resume
        self.status = PauseResume.PAUSE_NORMAL

        self.rect = self.images[self.status].get_rect()
        self.rect.topleft = (0, 5)

    def reset(self):
        self.status = PauseResume.PAUSE_NORMAL

    def draw(self, display_surface):
        display_surface.blit(self.images[self.status], self.rect)

    def is_hit(self, pos):
        return self.rect.collidepoint(pos)

    def update_click(self):
        if self.status == PauseResume.PAUSE_NORMAL or self.status == PauseResume.PAUSE_PASSED:
            self.status == PauseResume.RESUME_NORMAL
        else:
            self.status == PauseResume.PAUSE_NORMAL

    def update_mouse_motion(self, pos):
        is_mouse_on = self.is_hit(pos)

        if is_mouse_on:
            if self.status == PauseResume.PAUSE_NORMAL:
                self.status = PauseResume.PAUSE_PASSED
            elif self.status == PauseResume.RESUME_NORMAL:
                self.status = PauseResume.RESUME_PRESSED
        else:
            if self.status == PauseResume.PAUSE_PASSED:
                self.status = PauseResume.PAUSE_NORMAL
            elif self.status == PauseResume.RESUME_PRESSED:
                self.status = PauseResume.RESUME_NORMAL


class EndPromt:
    def __init__(self, *args):
        screen_rect = args[0]
        self.status = args[1]

        # outside border
        self.border_color = (96, 96, 96)
        self.border_rect = pygame.Rect(0, 0, 350, 300)
        self.border_rect.centerx = screen_rect.centerx
        self.border_rect.centery = screen_rect.centery + 40

        # score
        self.score_color = self.border_color
        self.font = pygame.font.SysFont(None, 40)

        # score text
        self.score_text_image = self.font.render("Score: ", True, self.score_color)
        self.score_text_top = self.border_rect.top + 30
        self.score_text_left = self.border_rect + 30

        # score number
        self.update_score_num()

    def update_score_num(self):
        self.socre_num_image = self.font.render(str(self.status.score), True, self.score_color)
        self.socre_num_rect = self.score_num_image.get_rect()
        self.socre_num_rect.centerx = self.border_rect.centerx
        self.score_num_rect.centery = self.border_rect.top + 80

    def draw(self, display_surface):
        # draw border
        pygame.draw.rect(display_surface, self.border_color, self.border_rect, 3)

        # draw socre text
        display_surface.blit(self.score_text_image, (self.score_text_left,self.score_text_top))

        # draw score number
        display_surface.blit(self.score_num_image, self.score_num_rect)