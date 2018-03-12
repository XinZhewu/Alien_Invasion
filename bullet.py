# coding=utf-8
# @Time   : 2018/2/3 22:59
# @Author : XinZhewu_568580410@qq.com

"""此文件管理飞船子弹的设置`移动`绘制
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """继承模块的类:可将游戏中相关的元素编组,进而同时操作编组中所有元素"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处位置创建子弹对象"""

        super().__init__()
        self.screen = screen

        # 在原点创建子弹的矩形,而后设置正确位置
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 储存用小数表示的子弹位置,微调子弹速度
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""

        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor

        # 更新表示子弹rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""

        pygame.draw.rect(self.screen, self.color, self.rect)
