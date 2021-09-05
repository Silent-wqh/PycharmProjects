import pygame


class Sunflower:

    def __init__(self, screen):
        """初始化向日葵和屏幕位置"""
        self.screen = screen

        # 载入向日葵图片
        self.image = pygame.image.load('images/sunflower.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将向日葵放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """在屏幕指定位置绘制向日葵"""
        self.screen.blit(self.image, self.rect)