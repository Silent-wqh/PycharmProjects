import pygame


class Ship:
    """飞船"""

    def __init__(self, settings, screen):

        self.screen = screen

        self.settings = settings

        # 载入飞船图片
        self.image = pygame.image.load('images/胜利飞燕.bmp')
        # 创建飞船矩形
        self.rect = self.image.get_rect()
        # 创建屏幕矩形
        self.screen_rect = self.screen.get_rect()

        # 设置飞船初始位置
        self.rect.left = 0
        self.rect.centery = self.screen_rect.centery

        # 增加浮点数速度支持
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动开关
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        """更新飞船位置"""
        if self.move_right and (self.rect.right <= self.screen_rect.right):
            self.x += self.settings.ship_speed
        if self.move_left and (self.rect.left >= 0):
            self.x -= self.settings.ship_speed
        if self.move_up and (self.rect.top >= 0):
            self.y -= self.settings.ship_speed
        if self.move_down and (self.rect.bottom <= self.screen_rect.bottom):
            self.y += self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

        self.screen.blit(self.image, self.rect)
