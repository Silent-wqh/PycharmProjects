import pygame


class Rect:
    """矩形"""

    def __init__(self, settings, screen):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings

        self.width, self.height = self.settings.rect_width, self.settings.rect_height

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # 设置矩形初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.right = self.screen_rect.right

        # 增加浮点数速度支持
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """更新矩形位置，并绘制矩形"""
        self.y += self.settings.rect_speed
        self.rect.y = self.y
        if self.rect.top == 0 or self.rect.bottom == self.screen_rect.bottom:
            self.settings.rect_speed = -self.settings.rect_speed
        self.screen.fill(self.settings.rect_color, self.rect)