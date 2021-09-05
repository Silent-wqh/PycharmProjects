import pygame


class Basket:
    """篮子"""

    def __init__(self, screen, settings):
        """初始化篮子"""

        self.screen = screen
        self.settings = settings

        # 载入篮子图片
        self.image = pygame.image.load('images/basket.bmp')
        # 创建篮子矩形
        self.rect = self.image.get_rect()
        # 创建屏幕矩形
        self.screen_rect = self.screen.get_rect()

        # 设置篮子初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 篮子移动标志
        self.move_right = False
        self.move_left = False
        # self.move_up = False
        # self.move_down = False

        # 增加浮点数速度支持
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """更新篮子位置"""
        if self.move_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.basket_speed
        if self.move_left and self.rect.left >= 0:
            self.x -= self.settings.basket_speed
        # if self.move_up and self.rect.top >= 0:
        #     self.y -= self.settings.basket_speed
        # if self.move_down and self.rect.bottom <= self.screen_rect.bottom:
        #     self.y += self.settings.basket_speed
        self.rect.x = self.x
        self.rect.y = self.y

        self.screen.blit(self.image, self.rect)
