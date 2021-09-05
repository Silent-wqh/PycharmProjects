import pygame
from random import randint
from pygame.sprite import Sprite

class Ball(Sprite):
    """球"""
    def __init__(self, screen, settings, basket, stats):

        super().__init__()

        self.screen = screen

        self.settings = settings

        self.basket = basket

        self.stats = stats

        # 载入球的图片
        self.image = pygame.image.load('images/ball.bmp')
        # 创建球的矩形
        self.rect = self.image.get_rect()
        # 创建屏幕矩形
        self.screen_rect = self.screen.get_rect()

        # 设置球的初始位置
        self.rect.right = randint(self.rect.width, self.settings.screen_width)
        self.rect.top = 0

        # 增加浮点数支持
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """更新球的位置"""
        self.y += self.settings.ball_speed
        self.rect.y = self.y

        if self.rect.bottom >= self.screen_rect.bottom:
            self.stats.ball_reach_bottom = True

        if (self.rect.bottom == self.basket.rect.top) \
                and (self.rect.left <= self.basket.rect.right)\
                and (self.rect.right >= self.basket.rect.left):
            self.stats.ball_reach_basket = True

        self.screen.blit(self.image, self.rect)

