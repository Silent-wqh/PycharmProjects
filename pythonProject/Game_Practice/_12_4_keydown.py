import pygame
import sys


def check_keydown():
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print(f'K_UP  {counter}')
        counter += 1
        screen.fill((100, 100, 100))
        pygame.display.flip()


check_keydown()
