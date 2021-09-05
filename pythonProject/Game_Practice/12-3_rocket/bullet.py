import pygame
from pygame.sprite import Sprite
from random import randint


class Bullet(Sprite):
    """子弹类"""
    def __init__(self, ai_settings, ship, screen):

        super().__init__()
        self.screen = screen

        # 创建子弹矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)

        # 校准子弹位置
        self.rect.centerx = ship.rect.right
        self.rect.centery = ship.rect.centery

        # 增加速度浮点数支持
        self.centery = float(self.rect.centery)
        self.centerx = float(self.rect.centerx)

        # 子弹颜色
        if ai_settings.bullet_color == 'random':
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        else:
            self.color = ai_settings.bullet_color

        self.bullet_speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """移动子弹"""
        self.centerx += self.bullet_speed_factor
        self.rect.centerx = self.centerx

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
