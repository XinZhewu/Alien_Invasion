# coding=utf-8
# @Time   : 2018/2/2 22:32
# @Author : XinZhewu_568580410@qq.com

"""此文件储存且初始化游戏的所有设置
"""


class Settings:

    def __init__(self):
        """初始化游戏静态设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (33, 33, 33)

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3  # 子弹宽度
        self.bullet_height = 15  # 子弹长度
        self.bullet_color = 233, 233, 233
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 此条属性正数向右,
        # 负数位于game_functions,经判断后启动
        # 以何种速度加快游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高游戏速度设置`外星人点数"""

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
