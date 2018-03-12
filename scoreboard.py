# coding=utf-8
# @Time   : 2018/2/7 23:43
# @Author : XinZhewu_568580410@qq.com

"""此文件管理游戏的得分,显示得分信息
"""

import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (0, 133, 233)
        self.font = pygame.font.SysFont(None, 30)

        # 准备图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_high_score(self):
        """将最高分转换为渲染的图像"""

        high_score = int(round(self.stats.high_score, -1))
        high_score_str = '{:,}'.format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将最高分放于屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""

        self.level_image = self.font.render(
            str(self.stats.level), True, self.text_color,
            self.ai_settings.bg_color
        )

        # 把等级放在当前得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        """将得分转换为一副渲染的图像"""

        # 函数round()让小数精确到小数点后几位,由第二实参指定
        # 设置为负数则变为正整数倍
        rounded_score = int(round(self.stats.score, -1))

        # 字符串格式设置指令,将数值转换为字符串时在其中插入逗号
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放于屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_ships(self):
        """显示余下多少艘飞船"""

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示历史最高得分`当前得分"""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # 绘制飞船
        self.ships.draw(self.screen)
