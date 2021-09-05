import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from rect import Rect
from game_stats import GameStats
import game_functions as gf
from button import Button


def run_game():
    """运行游戏"""

    pygame.init()

    settings = Settings()
    stats = GameStats(settings)

    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    # 创建一个飞船
    ship = Ship(settings, screen)
    # 创建一个矩形
    rect = Rect(settings, screen)
    # 创建一个按钮
    play_button = Button(screen, settings, 'play')
    # 创建一个子弹组
    bullets = Group()

    # 游戏主循环
    while True:

        gf.check_events(play_button, stats, ship, settings, screen, bullets)
        screen.fill(settings.bg_color)
        if stats.game_active:
            gf.update(rect, ship, bullets, stats, settings)
        else:
            play_button.draw_button()
        pygame.display.flip()


run_game()
