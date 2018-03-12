# coding=utf-8
# @Time   : 2018/2/2 18:22
# @Author : XinZhewu_568580410@qq.com

"""此文件创建游戏对象:
ai_settings负责设置; screen创建屏幕; 创建一个标题; ship创建飞船; 创建子弹编组
主循环调用:
check_events(); ship.update(); update_bullets(); update_aliens();
update_screen()
"""

import pygame
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from button import Button
from ship import Ship
import game_functions as gf


def run_game():

    # 初始化Pygame与设置
    pygame.init()
    ai_settings = Settings()

    # 定义显示窗口到变量;surface是屏幕的一部分
    # 此变量`外星人`飞船等元素都是surface
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))

    # 设置一个标题
    pygame.display.set_caption(
        'Alien Invasion by XinZhewu_568580410@qq.com')

    # 创建Play按钮;整个游戏只需要一个,故放到此文件
    play_button = Button(ai_settings, screen, 'Play')

    # 创建储存游戏统计信息的实例`记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船`子弹编组`外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环,此循环控制游戏
    while True:
        gf.check_events(
            ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(
                ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(
                ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(
            ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
