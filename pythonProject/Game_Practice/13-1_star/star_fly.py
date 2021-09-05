import pygame
from pygame.sprite import Group
from time import sleep

import gf
from settings import Settings


def run_game():

    pygame.init()

    settings = Settings()

    # 创建屏幕
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))

    # 背景色
    bg_color = (19, 44, 51)

    # 生成一组星星
    stars = Group()

    while True:

        screen.fill(bg_color)
        gf.create_fleet(screen, settings, stars)
        stars.update()
        gf.check_events()
        pygame.display.flip()
        stars = Group()
        sleep(0.03)


run_game()
