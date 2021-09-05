import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf

def run_game():
    """运行游戏"""

    pygame.init()

    settings = Settings()

    # 创建屏幕
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    # 创建雨滴组
    rains = Group()

    # 创建雨滴群
    gf.create_rain_group(rains, screen, settings)

    # 游戏主循环
    while True:

        # 填充屏幕颜色
        screen.fill(settings.bg_color)

        # 检测键盘
        gf.check_events()

        # 绘制雨滴
        rains.update(screen)

        # 更新屏幕
        pygame.display.flip()


run_game()