import pygame.image
from pygame.sprite import Sprite


class Star(Sprite):
    """小星星"""
    def __init__(self, screen):

        super().__init__()

        self.screen = screen

        # 载入图像
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 设置出生位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储星星准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """绘制星星"""
        self.screen.blit(self.image, self.rect)