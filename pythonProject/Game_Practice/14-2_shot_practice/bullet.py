import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹"""
    def __init__(self, settings, screen, ship):

        super().__init__()

        self.settings = settings
        self.screen = screen
        self.ship = ship

        # 创建子弹矩形
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # 设置子弹初始位置
        self.rect.left = self.ship.rect.right
        self.rect.centery = self.ship.rect.centery

        # 增加浮点数速度支持
        self.x = float(self.rect.x)

    def update(self):
        """更新子弹位置"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

        self.screen.fill(self.settings.bullet_color , self.rect)