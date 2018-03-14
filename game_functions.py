# coding=utf-8
# @Time   : 2018/2/3 19:02
# @Author : XinZhewu_568580410@qq.com

"""此文件包含一系列函数,负责游戏的大部分工作
"""

import sys  # 使用sys为玩家退出游戏
import pygame
from time import sleep
from alien import Alien
from bullet import Bullet


def change_fleet_direction(ai_settings, aliens):
    """将外星人群下移,改变方向"""

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人到达屏幕底端"""

    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def check_bullet_alien_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""

    # 删除
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 清空子弹,加快游戏节奏
        bullets.empty()
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        sb.prep_level()

        # 创建新外星人群
        create_fleet(ai_settings, screen, ship, aliens)


def check_events(
        ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """响应键盘按键和鼠标事件"""

    # 方法event.get()访问pygame检测到的事件
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            # save_high_score()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(
                event, ai_settings, screen, ship, bullets, stats, sb, aliens)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        # 方法mouse.get_pos()返回一个元组:玩家鼠标点击的坐标
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(
                ai_settings, screen, stats, sb, play_button,
                ship, aliens, bullets, mouse_x, mouse_y
            )


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取措施"""

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_high_score(stats, sb):
    """检查是否诞生了新的最高分"""

    with open('highest.txt', 'r+') as hst:
        highest = int(hst.read().rstrip())
        if stats.score > highest:
            highest = stats.score
            hst.write(str(highest))
            sb.prep_high_score()


def check_keydown_events(
        event, ai_settings, screen, ship, bullets, stats, sb, aliens):
    """附属于check_events()"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_F4:
        sys.exit()

    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, stats, sb, aliens, bullets, screen, ship)


def check_keyup_events(event, ship):
    """附属于check_events()"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def start_game(ai_settings, stats, sb, aliens, bullets, screen, ship):
    """使游戏开始"""

    # 重置游戏设置
    ai_settings.initialize_dynamic_settings()

    # 隐藏光标
    pygame.mouse.set_visible(False)

    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # 清空外星人`子弹列表
    aliens.empty()
    bullets.empty()

    # 创建新外星人群,飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def check_play_button(
        ai_settings, screen, stats, sb, play_button,
        ship, aliens, bullets, mouse_x, mouse_y
):
    """在玩家点击按钮时开始新游戏,方法检查鼠标点击位置与矩形是否重叠"""

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    # 当玩家点击Play按钮且游戏处于非活动状态时,游戏才重新开始
    if button_clicked and not stats.game_active:
        start_game(ai_settings, stats, sb, aliens, bullets, screen, ship)


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人放在当前行"""

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height + (2 * alien.rect.height * row_number))
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""

    # 外星人群间距为一个外星人的宽度,获取宽度,计算一行可容纳多少个,
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens,
                         alien_number, row_number)


def fire_bullet(ai_settings, screen, ship, bullets):
    """附属于check_keydown_events();创建一颗子弹,加入到编组bullets中"""

    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""

    available_space_x = ai_settings.screen_width - (2 * alien_width)

    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""

    available_space_y = (
            ai_settings.screen_height - (3 * alien_height) - ship_height)

    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows

# def read_high_score():
# def save_high_score():


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应被撞到的飞船"""

    if stats.ships_left > 0:

        # 飞船生命值减1
        stats.ships_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人`子弹列表
        aliens.empty()
        bullets.empty()

        # 创建新外星人群,将飞船放到屏幕底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人处于屏幕边缘,更新外星人群的位置"""

    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞;精灵为飞船,编组为外星人群;
    # 检查编组的元素是否碰撞精灵,找到元素后停止遍历编组;如否返回None
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):

    # 更新子弹位置
    bullets.update()

    # 删除屏幕外的子弹,但不应从列表或编组中删除,所以遍历副本
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_screen(
        ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """更新屏幕上的图像,屏切换到新屏幕,每次循环都重绘游戏元素,此方法用背景色填充屏幕,
    只接受一种实参(某个颜色).
    """

    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如游戏处于非活动状态,绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
