# coding=utf-8
# @Time   : 2018/2/6 17:23
# @Author : XinZhewu_568580410@qq.com

"""此文件管理游戏中的按钮
"""

import pygame.font  # 使Pygame将文本渲染到屏幕上


class Button:

    def __init__(self, ai_settings, screen, msg):
        """用于初始化按钮属性"""

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 133, 233)
        self.text_color = (233, 233, 233)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮rect对象,使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将 msg 渲染为图像,使其在按钮上居中,布尔实参True可开启反锯齿"""

        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮`文本"""

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
