import pygame
import sys

from rain import Rain


def check_events():
    """响应键盘"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def get_rain_number_x(rain):
    """获取横行可排列雨滴数"""
    available_space_x = rain.screen_rect.width - 2 * rain.rect.width
    rain_number_x = int(available_space_x / (2 * rain.rect.width))
    return rain_number_x


def get_rain_number_y(rain):
    """获取横行可排列雨滴数"""
    available_space_y = rain.screen_rect.height - 2 * rain.rect.height
    rain_number_y = int(available_space_y / (2 * rain.rect.height))
    return rain_number_y


def create_rain(rains, screen, settings, rain_number_x, rain_number_y):
    """创建单个雨滴"""
    rain = Rain(screen, settings)
    set_rain_location(rain, rain_number_x, rain_number_y)
    rains.add(rain)


def create_rain_group(rains, screen, settings):
    """创建雨滴群"""
    rain = Rain(screen, settings)
    for rows_y in range(get_rain_number_y(rain)):
        for rows_x in range(get_rain_number_x(rain)):
            create_rain(rains, screen, settings, rows_x, rows_y)


def set_rain_location(rain, rain_number_x, rain_number_y):
    """设置雨滴位置"""
    rain.rect.x = rain.rect.width + 2 * rain.rect.width * rain_number_x
    rain.rect.y = rain.rect.height + 2 * rain.rect.height * rain_number_y
