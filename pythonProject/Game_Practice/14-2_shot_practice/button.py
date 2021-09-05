import pygame.font


class Button:
    """按钮"""
    def __init__(self, screen, settings, msg):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # 设置按钮尺寸和颜色
        self.width, self.height = self.settings.button_width, self.settings.button_height
        self.button_color = self.settings.button_color
        self.text_color = self.settings.text_color
        self.font = pygame.font.SysFont(None, 48)

        # 创建rect对象，并居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮标签
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg文本渲染为图像，并居中"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                         self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮， 再绘制文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
