import pygame
import sys
from random import randint

from star import Star

def check_events():

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           sys.exit()

def create_fleet(screen, settings, stars):
    """创建星星群"""
    for rows_y in range(get_rows_y(screen, settings)):
        for rows_x in range(get_rows_x(screen, settings)):
            create_star(stars, screen, rows_x, rows_y)


def create_star(stars, screen, rows_x, rows_y):
    """创建一个星星"""
    star = Star(screen)
    star.rect.x = star.rect.width + 2 * rows_x * star.rect.width + randint(-10, 10)
    star.rect.y = star.rect.height + 2 * rows_y * star.rect.height + randint(-10, 10)
    stars.add(star)

def get_rows_x(screen, settings):
    """返回一行可容纳的星星数"""
    star = Star(screen)
    available_space_x = settings.screen_width - star.rect.width
    star_number = int((available_space_x / (2 * star.rect.width)))
    return star_number

def get_rows_y(screen, settings):
    """返回一列可容纳的星星数"""
    star = Star(screen)
    available_space_y = settings.screen_height - star.rect.height
    star_number = int((available_space_y / (2 * star.rect.width)))
    return star_number