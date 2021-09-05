import pygame
import sys

from settings import Settings
from basket import Basket
from ball import Ball


def check_event(basket):
    """响应键盘"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # 调用按键函数
            get_keydown(event, basket)
        if event.type == pygame.KEYUP:
            # 调用松开函数
            get_keyup(event, basket)


def get_keydown(event, basket):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        basket.move_right = True
    if event.key == pygame.K_LEFT:
        basket.move_left = True
    # if event.key == pygame.K_UP:
    #     basket.move_up = True
    # if event.key == pygame.K_DOWN:
    #     basket.move_down = True


def get_keyup(event, basket):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        basket.move_right = False
    if event.key == pygame.K_LEFT:
        basket.move_left = False
    # if event.key == pygame.K_UP:
    #     basket.move_up = False
    # if event.key == pygame.K_DOWN:
    #     basket.move_down = False


def update(basket, balls, screen, stats, settings):
    """更新篮子和球的位置"""
    basket.update()
    balls.update()
    create_ball(balls, screen, stats, basket, settings)


def create_ball(balls, screen, stats, basket, settings):
    """创建一个球并加入球组，删除超出屏幕下界的球"""
    if stats.ball_reach_bottom:
        balls.empty()
        stats.ball_reach_bottom = False
        if settings.accept_fail > 0:
            settings.accept_fail -= 1
        else:
            stats.game_active = False
        print('555')
    if stats.ball_reach_basket:
        balls.empty()
        stats.ball_reach_basket= False
        print('666')
    if bool(1-bool(len(balls))):
        ball = Ball(screen, settings, basket, stats)
        balls.add(ball)


