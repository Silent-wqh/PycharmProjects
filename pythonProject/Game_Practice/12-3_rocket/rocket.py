import pygame


class Rocket:
    """火箭"""
    def __init__(self, screen, settings):
        """初始化火箭和屏幕位置"""
        self.screen = screen
        self.settings = settings

        # 载入火箭图片
        # self.images = pygame.image.load('images/rocket.bmp')
        self.images = pygame.image.load('images/rocket_right.bmp')
        self.rect = self.images.get_rect()
        self.screen_rect = screen.get_rect()

        # # 火箭出生在底部中央
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom

        # 火箭出生在右侧中央
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # 响应按键
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        # 增加浮点数速度支持，貌似float()加不加都行
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blitme(self):
        """将火箭显示在屏幕上"""
        self.screen.blit(self.images, self.rect)

    def update(self):
        """移动火箭"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.move_speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.settings.move_speed
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.settings.move_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.move_speed

        # 更新坐标
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
