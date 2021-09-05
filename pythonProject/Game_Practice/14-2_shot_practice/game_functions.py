import pygame
import sys

from bullet import Bullet


def check_events(play_button, stats, ship, settings, screen, bullets):
    """响应键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 按键函数
            get_keydown(event, ship, settings, screen, bullets, stats)
        elif event.type == pygame.KEYUP:
            # 松开函数
            get_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标按键函数
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, mouse_x, mouse_y, stats,bullets, settings)


def get_keydown(event, ship, settings, screen, bullets, stats):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    if event.key == pygame.K_UP:
        ship.move_up = True
    if event.key == pygame.K_DOWN:
        ship.move_down = True
    if event.key == pygame.K_SPACE:
        create_bullet(settings, screen, bullets, ship, stats)


def get_keyup(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False
    if event.key == pygame.K_UP:
        ship.move_up = False
    if event.key == pygame.K_DOWN:
        ship.move_down = False


def check_play_button(play_button, mouse_x, mouse_y, stats, bullets, settings):
    """play按钮响应鼠标"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 开始游戏
        start_game(stats, bullets, settings)



def start_game(stats, bullets, settings):
    """开始游戏"""
    stats.game_active = True

    # 重置游戏信息
    stats.ship_live = 3
    stats.not_shot = 0
    bullets.empty()
    settings.initialize_dynamic_settings()

def create_bullet(settings, screen, bullets, ship, stats):
    """创建子弹"""
    bullet = Bullet(settings, screen, ship)
    bullets.add(bullet)
    stats.not_shot += 1
    for bullet in bullets.copy():
        if bullet.rect.left >= settings.screen_width:
            bullets.remove(bullet)


def bullet_rect_collision(bullets, rect, stats, settings):
    """子弹和矩形碰撞"""
    for bullet in bullets.copy():
        if (bullet.rect.left < rect.rect.right) and (bullet.rect.right > rect.rect.left) \
                and (bullet.rect.top < rect.rect.bottom) and (bullet.rect.bottom > rect.rect.top):
            bullets.remove(bullet)
            stats.not_shot -= 1
            settings.increase_speed()
        if stats.not_shot > settings.not_shot:
            stats.game_active = False


def update(rect, ship, bullets, stats, settings):
    """更新画面"""
    rect.update()
    ship.update()
    bullets.update()
    bullet_rect_collision(bullets, rect, stats,settings)
