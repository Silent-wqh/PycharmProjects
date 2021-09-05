import pygame
from pygame.sprite import Group

from settings import Settings
from basket import Basket
import game_functions as gf
from game_stats import GameStats


def run_game():
    """运行游戏"""

    pygame.init()

    settings = Settings()

    stats = GameStats()

    # 创建屏幕
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    # 创建篮子
    basket = Basket(screen, settings)

    # 创建一个球组
    balls = Group()


    # 游戏主循环
    while True:
        # 填充屏幕颜色
        screen.fill(settings.bg_color)
        gf.check_event(basket)

        if stats.game_active:

            gf.update(basket, balls, screen, stats, settings)

        # 刷新surface
        pygame.display.flip()


run_game()