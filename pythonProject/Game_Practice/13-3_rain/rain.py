import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """雨滴"""
    def __init__(self, screen, settings):

        super().__init__()

        self.screen = screen

        # 载入雨滴图像，创建雨滴矩形，创建屏幕矩形
        self.image = pygame.image.load('images/rain.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 设置雨滴初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # # 增加对浮点数速度支持
        # self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

        # 设置雨滴速度
        self.rain_speed = settings.rain_speed

    def update(self, settings):
        """更新雨滴位置并绘制雨滴"""
        self.rect.y += self.rain_speed
        self.screen.blit(self.image, self.rect)
        if self.rect.top >= self.screen_rect.bottom:
            self.rect.bottom = 0
