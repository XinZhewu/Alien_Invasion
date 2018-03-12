# coding=utf-8
# @Time   : 2018/2/2 23:03
# @Author : XinZhewu_568580410@qq.com

"""此文件管理飞船的设置`绘制
Pygame中,原点在左上角,终点在右下角
处理对象的位置时属性有:center`centerx`centery`top`bottom`left`right
"""

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""

        super(Ship, self).__init__()

        # 指定将飞船绘制在何处
        self.screen = screen

        # 使飞船获取速度设置,储存到一个属性方便函数使用
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')

        # 函数获取surface的属性rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        # 将飞船中心的X坐标设置为屏幕矩形的属性centerx
        self.rect.centerx = self.screen_rect.centerx

        # 将飞船下边缘的Y坐标设置为屏幕矩形的属性bottom
        self.rect.bottom = self.screen_rect.bottom

        # 定义新的属性:在飞船属性center中储存小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置,为True时移动飞船"""

        # 读取矩形右边的X坐标,如坐标点小于屏幕右边坐标则执行;否则停止,以防止越过屏幕
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        # 最左边的X坐标为0,如坐标点大于原点则执行;否则停止,以防止越过屏幕
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船,据给出的参数将图像绘制到屏幕"""

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""

        self.center = self.screen_rect.centerx
