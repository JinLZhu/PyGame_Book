# 敌人相关类，Enemy / EnemySmall / EnemyMiddle / EnemyBig /
# Enemy 是其余三个的基类
import pygame
from pygame._sprite import Sprite


class Enemy:
    def __init__(self, topleft, screen_rect, status):
        super().__init__()

        self.screen_rect = screen_rect
        self.status = status
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = pygame.Rect(topleft, self.get_max_size())
        self.current_hp = help.max_hp
        self.is_hit_bullet = False

    def update(self):
        self.rect.top += 2
        # remove enemy outside the screen from group
        if self.rect.top >= self.screen_rect.bottom:
            self.kill()

    def hit_by_bullet(self):
        if self.current_hp > 0:
            self.current_hp -= 1
            self.is_hit_bullet = True

    @classmethod
    def get_max_size(cls):
        max_width_image = max(cls.images, key=lambda x: x.get_width())
        max_height_image = max(cls.images, key=lambda x: x.get_height())

        return max_width_image.get_width(), max_height_image.get_height()