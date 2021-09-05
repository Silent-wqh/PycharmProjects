import sys
from time import sleep

import pygame

from sunflower import Sunflower


def run_game():
    """初始化屏幕为蓝色"""
    pygame.init()

    screen = pygame.display.set_mode((1024, 768))

    bg_color_1 = (147, 181, 207)

    bg_color_2 = (173, 101, 152)

    color_sign = True

    # 创建sunflower对象
    sunflower = Sunflower(screen)

    while True:
        """绘制屏幕"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if color_sign:
            screen.fill(bg_color_1)
        else:
            screen.fill(bg_color_2)

        color_sign = bool(1-color_sign)
        sunflower.blitme()
        pygame.display.flip()
        sleep(0.9)


run_game()
