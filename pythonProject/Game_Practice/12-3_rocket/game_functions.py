import sys
import pygame

from bullet import Bullet

def check_events(rocket, bullets, settings, screen):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down(event, rocket, bullets, settings, screen)
        elif event.type == pygame.KEYUP:
            key_up(event, rocket)


def key_down(event, rocket, bullets, settings, screen):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 右移
        rocket.move_right = True
    if event.key == pygame.K_LEFT:
        # 左移
        rocket.move_left = True
    if event.key == pygame.K_UP:
        # 上移
        rocket.move_up = True
    if event.key == pygame.K_DOWN:
        # 下移
        rocket.move_down = True
    if event.key == pygame.K_SPACE:
        # 子弹右移
        fire_bullet(settings, rocket, screen, bullets)


def key_up(event, rocket):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        rocket.move_right = False
    if event.key == pygame.K_LEFT:
        rocket.move_left = False
    if event.key == pygame.K_UP:
        rocket.move_up = False
    if event.key == pygame.K_DOWN:
        rocket.move_down = False


def update_screen(screen, settings, rocket, bullets):
    """刷新屏幕"""

    # 填充屏幕颜色
    screen.fill(settings.bg_color)

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 显示火箭
    rocket.blitme()

    # 刷新屏幕
    pygame.display.flip()


def update_bullets(bullets, rocket):
    """更新子弹"""
    bullets.update()

    # 移除飞出屏幕外的子弹
    for bullet in bullets.copy():
        if bullet.rect.left > rocket.screen_rect.right:
            bullets.remove(bullet)


def fire_bullet(settings, rocket, screen, bullets):
    """发射子弹"""
    if len(bullets) < settings.bullet_allowed:
        new_bullet = Bullet(settings, rocket, screen)
        bullets.add(new_bullet)