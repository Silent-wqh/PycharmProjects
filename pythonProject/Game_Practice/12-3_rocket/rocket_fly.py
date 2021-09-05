import pygame
from pygame.sprite import Group

from rocket import Rocket
import game_functions as gf
from settings import Settings


def run_game():
    """运行游戏"""
    pygame.init()

    # 创建设置对象
    settings = Settings()

    # 创建屏幕对象
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Rocket')

    # 背景色

    # 创建火箭对象
    rocket = Rocket(screen, settings)

    # 创建子弹对象组
    bullets = Group()

    # 启动游戏
    while True:

        gf.check_events(rocket, bullets, settings, screen)
        rocket.update()
        gf.update_bullets(bullets, rocket)
        gf.update_screen(screen, settings, rocket, bullets)



# 运行游戏
run_game()
